# ugh, primes. how primes.
# also, we have a test for primes.
# so we make the is_prime func
# then we can append to a list, check list length if 10001 long, return final num
# jeez, way late on this (12:05:53) -- (12:10:59) 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gettem():
    list_primes = []
    count = 2
    lim = 10001
    #lim = 6

    while len(list_primes) != lim:
        if is_prime(count):
            list_primes.append(count)
        count += 1
    return list_primes[-1]
print(gettem())

# getting this right makes me want to do this for a few hours. that feels nice.
