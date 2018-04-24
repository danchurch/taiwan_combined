#! /usr/bin/env bash

#SBATCH --job-name=trim_leaves
#SBATCH --output=trim_leaves.out
#SBATCH --error=trim_leaves.err
#SBATCH --time=0-01:00:00
#SBATCH --nodes=1

leafdir=/projects/xylaria/dthomas/leaf/

module load racs-eb
module load FASTX-Toolkit/0.0.14-foss-2016b

fastx_trimmer -l 263 -i $leafdir"reLeafR1.fastq" -o Roo_R1_trimmed.fastq
fastx_trimmer -l 170 -i $leafdir"reLeafR2.fastq" -o Roo_R2_trimmed.fastq

