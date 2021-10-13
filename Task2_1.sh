touch out.txt
echo "time: " $(date) >> out.txt
#echo $'\n' >> out.txt
echo "user: " $USER >> out.txt
pp=$(pwd) 
echo "os:" $OSTYPE
echo "dirs in $pp"  >> out.txt
find * -maxdepth 0 -type d -print | wc -l | tee -a out.txt
echo "dirs in $pp  rec" >> out.txt
find * -type d -print | wc -l | tee -a out.txt

