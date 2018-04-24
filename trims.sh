
wooddir=/home/daniel/Documents/taiwan/woodreads/

cd /home/daniel/Documents/taiwan/taiwan_combined_biom

R1trimdir='/home/daniel/Documents/taiwan/taiwan_combined_biom/trimmed_wood/R1/'

for i in $wooddir*_R1_*; do
    echo $i
    out=$R1trimdir$(basename ${i/_001\.fastq/_trimmed\.fastq}) 
    fastx_trimmer -l 255 -i $i -o $out && echo $out 
done

R2trimdir='/home/daniel/Documents/taiwan/taiwan_combined_biom/trimmed_wood/R2/'

for j in $wooddir*_R2_*; do
    echo $j
    out=$R2trimdir$(basename ${j/_001\.fastq/_trimmed\.fastq}) 
    fastx_trimmer -l 210 -i $j -o $out && echo $out 
done

