import sys,time
import os.path

p = open("needed.txt", "a")
p.write(sys.argv[1] + '\n')
p.close()

results = "searchResults.txt"

time.sleep(0.07)

k = open(results, "r")
l = k.read().split("\n")
k.close()

for i in l:
    if i.startswith(sys.argv[1]):
        print i[len(sys.argv[1])+2:]
        sys.exit()
