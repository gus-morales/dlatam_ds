echo "SCRIPT START"
echo ""

echo "(1) Download TXT files"
python3.7 src/download_txt.py
echo ""

echo "(2) MapReduce Word Count"
for file in *.txt; do
    [ -f "$file" ] || continue
    echo "$file"
    cat $file | python3.7 src/wordcount_primitivo.py > word_count_$file
done
echo ""

echo "(*) Copy files into my S3 bucket"
mv clarissa*.txt richardson_clarissa/.
mv word*.txt richardson_clarissa_wordcount/.

#aws s3 cp richardson_clarissa/ s3://adlbigdatadesafio4/richardson_clarissa --recursive
echo ""