#!/bin/bash
metric=${1:-none}
printf "%-10s %-12s %-5s %-7s %-5s %-5s\n" "User" "Game" "Wins" "Losses" "Ties" "Ratio"
echo "---------------------------------------------------"
tr -d '\r' < history.csv | awk -F',' '
NR > 1 {
    if ($1 == "Tie") {
        ties[$2","$5]++
        ties[$3","$5]++
    } else {
        wins[$1","$5]++
        losses[$2","$5]++
    }
}
END {
    for (key in wins) {
        split(key, arr, ",")
        user = arr[1]
        game = arr[2]
        w = wins[key]
        l = (key in losses) ? losses[key] : 0
        t = (key in ties) ? ties[key] : 0
        ratio = (l == 0) ? w : w / l
        print user "," game "," w "," l "," t "," ratio
    }
    for (key in losses) {
        if (!(key in wins)) {
            split(key, arr, ",")
            user = arr[1]
            game = arr[2]
            l = losses[key]
            t = (key in ties) ? ties[key] : 0
            print user "," game ",0," l "," t ",0"
        }
    }
    for (key in ties) {
        if (!(key in wins) && !(key in losses)) {
            split(key, arr, ",")
            print arr[1] "," arr[2] ",0,0," ties[key] ",0"
        }
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
