## (18:30:23) -- (18:50:49) 

## there's a couple of rules that you give to a starting num
## apply based on odd / even, it'll go until it reaches one.
## everytime it hits a rule, add one to the count

## how will this work?
## take in a number, if even apply rule, if odd...
## look when when the number is == 1; if yes then break.
## each time a rule is applied, add one to the count
## ahh which number, not which has the longest step.
    ## so I need to save a dict, with the 


mxm = [0,0]

def get_coll(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    return count    

for i in range(1, 1000001):
    cur = get_coll(i)
    if cur > mxm[1]:
        mxm = [i,cur]
print(mxm)
