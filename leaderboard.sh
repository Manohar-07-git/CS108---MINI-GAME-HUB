#!/bin/bash
stat=$1
> leaderboard.txt
n=$(wc -l users.tsv | awk '{print $1}')
for k in tic-tac-toe othello connect4
do
echo "$k"
> leaderboard.txt
for i in $(seq 1 $n)
do
	a=$(awk 'NR==$i {print $1}' users.tsv)
        wins=$(awk -F ',' -v ka="$k" '$4==ka {print $1}' history.csv | grep -wc "$a")
	loss=$(awk -F ',' -v ka="$k" '$4==ka {print $3}' history.csv | grep -wc "$a")
	if [[ "$loss" == "0" ]]; then
		wlratio="$wins"
       else
	       wlratio=$(( $wins/$loss ))
       fi
	echo "$a,$wins,$loss,$wlratio" >> leaderboard.txt
done
if [[ "$stat" == "wins" ]]; then
   sort -t ',' -k2,2nr leaderboard.txt
fi
if [[ "$stat" == "loss" ]]; then
   sort -t ',' -k3,3nr leaderboard.txt
 fi
if [[ "$stat" == "wlr" ]]; then
   sort -t ',' -k4,4nr -k2,2n leaderboard.txt
fi
done
	
	


