#pipeline
import os
import subprocess
import argparse
import sys
from subprocess import call

def eol_conv_unix(filename):
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'
    with open(filename, 'rb') as open_file:
        content = open_file.read()
    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(filename, 'wb') as open_file:
        open_file.write(content)
        
def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))
        
def main():
    #parser = argparse.ArgumentParser(description='Enter 1 to generate counts. Following that, enter 2 to genarate DESeq2 results of your counts')
    parser = argparse.ArgumentParser()
    parser.add_argument("type", help="Pass in the type of pipeline to run. counts=generate counts, Deseq2=generate DESeq2 results")
    args = parser.parse_args()
    print(args.type)
    currentDir = get_script_path()
    work_path = os.path.join(currentDir, 'fastqFiles')
    if args.type == "counts":
        if os.listdir(work_path) == []:
            print "fastq Files are not found, please upload them to start the pipeline"
        else:
            print "Generating counts"
            eol_conv_unix('star.sh')
            #os.system('runAsPipeline star.sh "sbatch -p short -t 20:0 -n 1" noTmp run')
    elif args.type == "DESeq2":
        print "Running DESeq2"
        os.system("Rscript "+ "readtoR.R Conditions.txt out.txt")
        
  
if __name__ == '__main__':
	main()