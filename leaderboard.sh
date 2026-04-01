#!/bin/bash

metric=$1

echo "User       Game         Wins  Losses  Ratio"
echo "---------------------------------------------------"

awk -F',' '

# Skip header row
NR > 1 {

    # Count wins and losses
    wins[$1","$4]++
    losses[$2","$4]++
}

END {

    # First: print users who have wins
    for (key in wins) {

        split(key, arr, ",")

        user = arr[1]
        game = arr[2]

        w = wins[key]

        # If no losses, set to 0
        if (key in losses) {
            l = losses[key]
        } else {
            l = 0
        }

        # Avoid division by zero
        if (l == 0) {
            ratio = w
        } else {
            ratio = w / l
        }

        print user "," game "," w "," l "," ratio
    }

    # Now: handle users who only lost (never won)
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

' history.csv |

# Sorting part (easy to read)
{
    if [ "$metric" = "wins" ]; then
        sort -t',' -k3 -nr
    elif [ "$metric" = "losses" ]; then
        sort -t',' -k4 -nr
    elif [ "$metric" = "ratio" ]; then
        sort -t',' -k5 -nr
    else
        cat
    fi
} |

awk -F',' '{
    printf "%-10s %-12s %-5d %-7d %.2f\n", $1, $2, $3, $4, $5
}'
