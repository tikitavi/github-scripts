import sys

def make_dict(repo):
    print 'Preparing results for ' + repo
    gitlog = open('gitlog-' + repo, 'r')
    commits = open('commits-' + repo, 'w')
    for line in gitlog:
        if line.startswith('commit') or line.startswith('Author:') or line.startswith('Date:') or 'insertion' in line:
            commits.write(line)
    gitlog.close()
    commits.close()

    commits = open('commits-' + repo, 'r')
    result = open(repo, 'w')
    result.write('Repository: ' + repo + '\n')
    result.write('------------------------\n')
    lines = commits.readlines()
    for l in range(0, len(lines)):
        line = lines[l]
        if (line.startswith('commit') and 'files changed' in lines[l+3]):
            stats = lines[l+3].split(" ")
            idx = [i for i, s in enumerate(stats) if 'insertion' in s]
            insertions = stats[idx[0]-1]
            if int(insertions) >= 5000:
                loc = stats[idx[0]-1]
                result.write(line)
                result.write(lines[l+1])
                result.write(lines[l+2])
                result.write(loc + ' insertions\n')
                result.write('---\n')
    result.close()
    commits.close()

if __name__ == "__main__":
    make_dict(sys.argv[1])