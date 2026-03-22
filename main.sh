#!/bin/bash

FILE="users.tsv"

	if [[ ! -f $FILE ]]; then
	touch users.tsv
	fi

 hash_fun(){
	 echo -n "$1" | sha256sum | awk '{print $1}'
	 }
 
 auth_player(){
	 	local p_v="$1"
		local user
		local pwd
		local h_in
		local stored_hash
		local stored_name
		local fstored_hash 
		local line

		while true; do
		read -p "enter username for $p_v " user

		stored_hash=""
		while read -r line; do
			stored_name=$(echo "$line" | awk '{print $1}')
			
			fstored_hash=$(echo "$line" | awk '{print $2}')
			
			if [[ "$stored_name" = "$user" ]]; then
				stored_hash="$fstored_hash"
				break
			fi
                        done < "$FILE"
	        

		}


