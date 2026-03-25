#!/bin/bash

FILE="users.tsv"
[[ ! -f "$FILE" ]] && touch "$FILE"

hash_fun(){
    echo -n "$1" | sha256sum | awk '{print $1}'
}

register(){
    echo "user do not exist do you want to register(yes/no)?"
    read -r response
    if [[ "$response" == "yes" ]]; then
        echo "set a password: "
        read -r -s passwordn
        echo -e "$username\t$(hash_fun "$passwordn")" >> "$FILE"
        echo "updated user"
    elif [[ "$response" == "no" ]]; then
        authentication
    else
        echo "input either yes or no"
        register
    fi
}

authentication(){
    echo "enter username: "
    read -r username
    stored_hash=$(awk -F "\t" -v user="$username" '$1 == user {print $2}' "$FILE")
    if [[ -n "$stored_hash" ]]; then
        while true; do
            echo "enter password: "
            read -r -s password
            if [[ "$(hash_fun "$password")" == "$stored_hash" ]]; then
                echo "user authenticated"
                break
            else
                echo "incorrect password"
            fi
        done
    else
        register
        authentication
    fi
}

cond(){
    authentication
    username1=$username
    authentication
    username2=$username
    if [[ "$username2" == "$username1" ]]; then
        echo "both usernames cannot be same enter user2 again"
        authentication
        username2=$username
        cond
    fi
    python3 game.py "$username1" "$username2"
}

cond
