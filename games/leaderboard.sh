#!/bin/bash

metric=${1:-none}

echo "User       Game         Wins  Losses  Ratio"
echo "---------------------------------------------------"

awk -F',' '

NR > 1 {

    wins[$1","$4]++
    losses[$2","$4]++
}

END {

    for (key in wins) {

        split(key, arr, ",")
        user = arr[1]
        game = arr[2]

        w = wins[key]

        if (key in losses) {
            l = losses[key]
        } else {
            l = 0
        }

        if (l == 0) {
            ratio = w
        } else {
            ratio = w / l
        }

        print user "," game "," w "," l "," ratio
    }

    for (key in losses) {

        if (!(key in wins)) {

            split(key, arr, ",")
            user = arr[1]
            game = arr[2]

            w = 0
            l = losses[key]
            ratio = 0

            print user "," game "," w "," l "," ratio
        }
    }
}
' history.csv | {

    if [ "$metric" = "wins" ]; then
        sort -t',' -k3 -nr
    elif [ "$metric" = "losses" ]; then
        sort -t',' -k4 -nr
    elif [ "$metric" = "ratio" ]; then
        sort -t',' -k5 -nr
    else
        cat
    fi

} | awk -F',' '{
    printf "%-10s %-12s %-5d %-7d %.2f\n", $1, $2, $3, $4, $5
}'