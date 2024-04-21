# (12:24:58) -- (13:07:00) 
## first question, how do I get factors at all?
## then find which are prime, then find the biggest one.

## this finds the answer, but isn't completely correct.
## I'm finding the factors up to the square root, but I'm not adding the corresponding upper mul
## Maybe what I could do is search from the square root to the lim instead of starting at 1

def find_primes(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

lim = 600851475143
factors = [i for i in range(1, int(lim**0.5) + 1) if lim % i == 0]
primes = [i for i in factors if find_primes(i)]
print(primes[-1])
