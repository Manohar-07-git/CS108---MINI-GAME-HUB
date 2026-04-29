#!/bin/bash

metric=${1:-none}

printf "%-10s %-12s %-5s %-7s %-5s %-5s\n" "User" "Game" "Wins" "Losses" "Ties" "Ratio"
echo "---------------------------------------------------"

tr -d '\r' < history.csv | awk -F',' '
{
    key1 = $2","$5   # player1,game
    key2 = $3","$5   # player2,game

    if ($1 == "Tie") {
        ties[key1]++
        ties[key2]++
    } else {
        wins[$1","$5]++
        losses[$2","$5]++
    }
}
END {
    # collect all unique keys
    for (k in wins) all[k]
    for (k in losses) all[k]
    for (k in ties) all[k]

    # process each user-game pair
    for (key in all) {
        split(key, arr, ",")
        user = arr[1]
        game = arr[2]

        w = (key in wins) ? wins[key] : 0
        l = (key in losses) ? losses[key] : 0
        t = (key in ties) ? ties[key] : 0

        # consistent ratio calculation
        ratio = (l == 0) ? w : w / l

        print user "," game "," w "," l "," t "," ratio
    }
}
' | {
    if [[ "$metric" = "wins" ]]; then
        sort -t',' -k3 -nr
    elif [[ "$metric" = "losses" ]]; then
        sort -t',' -k4 -nr
    elif [[ "$metric" = "ratio" ]]; then
        sort -t',' -k6 -nr
    else
        cat
    fi
} | awk -F',' '{
    printf "%-10s %-12s %-5d %-7d %-5d %.2f\n", $1, $2, $3, $4, $5, $6
}'