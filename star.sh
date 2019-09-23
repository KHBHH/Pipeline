for fastq in $PWD/fastqFiles/*.fastq

do

#create a prefix
base=`basename $fastq .fastq`
#@1,0,star,,sbatch -p short -n 1 -t 20:0 --mem 30G -c 13
STAR --runThreadN 12 --genomeDir $PWD/Index/ --outFileNamePrefix $PWD/STAR_results/$base. --readFilesIn $fastq



#@2,1,Samt,,sbatch -p short -n 1 -t 20:0 --mem 5G -c 1
samtools sort -n $PWD/STAR_results/$base.Aligned.out.sam -o $PWD/Sorted_results/$base.sorted.sam

#@3,2,htseqcount,,sbatch -p short -n 1 -t 20:0 --mem 5G
htseq-count -m union -r name -i gene_name -a 10 --stranded=no $PWD/Sorted_results/$base.sorted.sam $PWD/genome/Mus_musculus.GRCm38.97.gtf > $PWD/counts/$base.counts


done


