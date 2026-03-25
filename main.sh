#!/bin/bash
[[ ! -e users.tsv ]] && touch users.tsv
cond(){if [[ "$username2" != "$username1" ]];then
        python3 game.py $username1 $username2
else
        {authentication
       username2=$username
       cond
}

register(){
        echo "user do not exist  do you want to register(yes/no)?"
        read -r response
        if [[ "$response" == "yes" ]]; then
                echo "set a password: "
                read -r -s passwordn
                echo "$username$'\t'$(echo "$passwordn" | sha256sum)" >> users.tsv
                echo "updated user"
		authentication
        elif [[ "$response" == "no" ]];then
         func
        else
                echo "input either yes or no"
                register
        fi
	}

authentication(){
echo "enter username: "
read -r username

if [[ "$(awk -F "\t" -v user=$username ' $1 == user {print $1}')" == "$username" ]];then
        awk -F "\t" -v user=$username ' $1 == user {print $2}' users.tsv > pass.txt
	echo "enter password: "
        read -r -s password
	if [[ "$( $password | sha256sum )" == "$(cat pass.txt)" ]];then
		echo "user authenticated"
		rm pass.txt
	else 
		{echo "incorrect password"
		rm pass.txt
		authentication}
	fi
else
	register
fi
}
authentication
username1=$username
authentication
username2=$username
cond
	





        


