#!/bin/bash  

read -p "Enter file name: " filename
read -p "Enter your comment: " com
echo " you entered $filename"
#read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

git rm $filename
git commit -m "$com"
git push origin
