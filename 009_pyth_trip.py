## a couple functions here: make sure a pyth trip, add the trip together to see if 1000, then take product of abc
## (10:43:28) -- (11:07:04) taking a break
## (10:09:26) -- (10:29:02) 
## finding the trip will be the hardest. rather, generating will be. Checking shouldn't be difficult.
## validating it's a trip...
    ## return a < b < c
## I could iterate like 1 * 2.3.4.5... then 2 * 3.4.5.6... and check if c's a good num. If so, then they're added together to see if sum is 1000. If so, take product of the three.

def make_pairs():
   upper_lim = 301
   for a in range(1, upper_lim ):
        for b in range(a+1, a+upper_lim ): 
            c = (a**2 + b**2)**.5
            if c.is_integer():
                if a + b + c == 1000:
                    return print(a * b * c)
make_pairs()



## what do I have an issue with actually?
## generating pairs / trips to test.
## if I can take a square root and see if it's a whole number then that's an easier test
## and easier generation. Cool. (6**.5).is_integer() is the way. That's how I get c.
## so now generating pairs for a and b. a brute force way would be to nested iterate through a range
    ## I have an aversion to brute forcing, maybe that's why I'm looking for other methods.
    ## but for now we'll see if it works.
## no zeros, and need to make sure b is always starts +1 of a, and then increases.
## beautiful, got it. Next, need to get c and then add together to see if sum is 1000
## what were my issues here? outside of the logic, I kept testing the wrong things. final if statement was testing the wrong 
## operation (a**2, b**2,etc). I think I'm scared of brute forcing and keep trying to be clever, for rn I think BF is ok.
## writing out the 1 * 2.3.4.5... examples was a good move, I focused on a simple implementation that would always produce
## numbers that would work, (sim to what Thor had said about only allowing correct inputs with enums rather than
## trying to check for them later and ending up mishandling them. No bueno. 
## I really liked the `range(a+1...` move, slight iteration that shifted the window a smidge. That's what allowed the 1 * 2.3.4...
