## (10:01:57) 
## if it makes past all these numbers, then it's the winner, right? just return that.
## how do I tell if goes through all of these though? 

optimized_nums = [2,3,5,7,11,13,17,19] # huh, the primes?
optimized_nums = [2,3,5,7,10] # huh, the primes?

def get_it():
    #answer = 2520
    answer = 1
    while True:
        for i in optimized_nums:
            if answer % i != 0:
                answer += 1
                continue
            else:
                return answer

print(get_it())



## a naive and expensive way would be to: i % range(1,21) == 0 then append results
## but we should be able to remove computations to get rid of numbers to run
## like if a number is divisible by 10, it's also divisible by 2 and 5, so you can remove dividing by 10. That would be a thing to solve at first.
## let's get the example to work first

## num = 2520 # because we know that the limit of last one
## for i in range(1,21):
    ## if num % i != 0:
        ## continue
## but if it makes it past....

## so how do I test if it goes through all of the numbers? right now it's getting stoppd at a single number. I should be able to do a list comp, right?
