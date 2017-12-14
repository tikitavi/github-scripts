#!/bin/bash -e

username=$1
password=$2

if [[ $password ]] ; then
  github_login="-u $username:$password"
  echo $github_login
fi

rm -rf ./contributors
mkdir contributors
while read LINE ; do
    to_cut="https://github.com/Juniper/"
    repo="${LINE/$to_cut/}"
    echo $repo
    i=1
    NUMOFLINES=0
    touch ./contributors/${repo}
    while [ $NUMOFLINES -eq $((($i-1)*30)) ] ; do
      current_page=`curl -i $guthub_login https://api.github.com/repos/Juniper/${repo}/contributors?page=$i`
      echo "${current_page//}" | grep login | awk '{print $2}' | sed -e "s/\"//" -e "s/\",//" >> ./contributors/${repo}
      NUMOFLINES=$(wc -l < "./contributors/$repo")
      echo $NUMOFLINES
      let i=i+1
    done
    
done < ./repos