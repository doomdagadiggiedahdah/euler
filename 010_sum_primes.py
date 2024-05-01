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

## (10:39:26) -- (10:42:42) damn. really?
## find the primes below a number, add them together. Loop through nums upto a limit, append to list, sum.

ls = []
lim = 2000000
for i in range(1, lim+1):
    if find_primes(i):
        ls.append(i)
print(sum(ls))
