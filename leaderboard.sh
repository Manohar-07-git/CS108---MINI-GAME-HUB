#!/bin/bash
stat=$1
n=$(wc -l users.tsv | awk 'print{$1}')
for k in {tic-tac-toe,othello,connect4}
do
echo "$k"
for i in `seq 1 $n`
do
	a=$(awk 'NR==$i {print $1}' users.tsv)
        wins=$(awk -F ',' -v ka=$k '$4==$ka print{$1}' history.csv | grep -c "$a")
	loss=$(awk -F ',' -v ka=$k '$4==$ka print{$3}' history.csv | grep -c "$a")
       if [[ "$loss"="0" ]]
	       wlratio="$wins"
       else
	       wlratio=$(( $wins/$loss ))
       fi
	echo "$a,$wins,$loss,$wlratio" >> leaderboard.txt
done
if [[ "$stat"=="wins" ]]; then
   sort -t ',' -k2,2 leaderboard.txt
fi
if [[ "$stat"=="loss" ]]; then
   sort -t ',' -k3,3 leaderboard.txt
 fi
if [[ "$stat"=="wlr" ]]; then
   sort -t ',' -k4,4 -k2,2r leaderboard.txt
fi
done
	
	


