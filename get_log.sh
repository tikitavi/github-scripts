for repo in $(cat repos) ; do
    cd ..
    cd $repo
    git log --stat > ../statistics/gitlog-$repo
    cd ../statistics
    python make_dict.py $repo
done