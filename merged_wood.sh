#! usr/bin/env bash

#SBATCH --job-name=merge_wood
#SBATCH --output=merge_wood.out
#SBATCH --error=merge_wood.err
#SBATCH --time=0-04:00:00
#SBATCH --nodes=1

module load usearch/8.0

cd projects/xylaria/dthomas/

R1d=/projects/xylaria/dthomas/trimmed_wood/R1/

for forward in $R1d*; do
    echo $forward
    reverse=${forward//R1/R2}
    aa=$(basename $forward); output="/projects/xylaria/dthomas/merged_wood/"${aa/_R1_trimmed.fastq/_merged.fastq}
    usearch -fastq_mergepairs $forward -reverse $reverse -fastqout $output
done


