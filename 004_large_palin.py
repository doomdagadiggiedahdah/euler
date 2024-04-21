## need to get the palindrome of the numbers, easy str(num) == str(num)[::-1]
## now getting the highest value. I can see that the numbers need to be computed to see if palin

# I'm uncertain how to go about finding the highest value of products in a set of numbers.
## do I minus by one from each? or just by one side?
## what if I did 99 * 99, 99 * 98, 99 * 97, ...and then 98 * 98, 98 * 97, 98 * 96...
## computed all of them until -100 or something, and then returned the highest num?

## ok check it: 99X * (matches, then descending) and if palin, append to list and then
## go to 99(X-1) * (matches, descending), etc.
## I don't really like this, but it should provide the answer.

## (14:15:50) -- (14:24:17) 
## I actually did take longer than this, maybe another 10?

pals = []

up_lim = 999
dw_lim = 100

## oh, the b loop needs to be diff; otherwise it's just computing the same thing each time.
## 

for a in range(up_lim, dw_lim, -1):
    for b in range(a, dw_lim, -1):
        if str(a*b) == str(a*b)[::-1]:
            pals.append(a*b)
            break
pals.sort()
print(pals[-1])
