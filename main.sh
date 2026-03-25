#!/bin/bash
[[ ! -e users.tsv ]] && touch users.tsv
cond(){
	authentication
	username1=$username
	authentication
	username2=$username
	if [[ "$username2" != "$username1" ]];then
        python3 game.py $username1 $username2
else
	echo "both usernames cannot be same repeat the process again"
       cond
	fi
}
register(){
        echo "user do not exist  do you want to register(yes/no)?"
        read -r response
        if [[ "$response" == "yes" ]]; then
                echo "set a password: "
                read -r -s passwordn
                echo -e "$username\t$(echo -n "$passwordn" | sha256sum | awk '{print $1}')" >> users.tsv
                echo "updated user"
        elif [[ "$response" == "no" ]];then
         authentication
        else
                echo "input either yes or no"
                register
        fi
	}

authentication(){
echo "enter username: "
read -r username

if [[ "$(awk -F "\t" -v user="$username" ' $1 == user {print $1}' users.tsv)" == "$username" ]];then
	hpass=$(awk -F "\t" -v user="$username" ' $1 == user {print $2}' users.tsv)
	echo "enter password: "
        read -r -s password
	if [[ "$( echo -n "$password" | sha256sum | awk '{print $1}' )" == "$hpass" ]];then
		echo "user authenticated"
	else 
			echo "incorrect password"
		authentication
	fi
else
	register
fi
}
cond
	





        


