# find smallest number
# can be divided by 1-20 with no remainder
# note: I already have a test case to check if it's right.
# (11:21:23) -- stopping for now (11:44:30) 
# it needs to be divisible by ALL numbers. try
# start from 0 and see if divisible. Maybe I'm getting ahead of myself.

def sml(rng):
    count = 252
    for i in range(2432902008176640000):
        for i in range(1, rng + 1):
            if count % i != 0:
                count += 1
                print(count)
                continue
print(sml(10))



# need a number to check. count.
# needs to be divisible by the numbers through range
# how do I check if a number is k
# now I'm getting the correct result, but not passing it back correctly.
# I could just hack it with this to get the right answer.
# maybe a less computationally expensive way would be to take 20! and then go down from there.
# damn, 20! == 2432902008176640000. shows even a shallow need for thinking correctly before running.
# I also don't know how to stop this thing. with the test I don't know how to say "all values
# are divisible, 
