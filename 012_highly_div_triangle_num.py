## (17:11:57) -- (17:15:44)
## we generate the triangle numbers
## factorize and get len of factors
    # I'm reminded of a previous factorizing problem, needed to use sqrt
    ## I need to optimize this though. This is taking way too long.
## find the tri_num that has len(tri_factors) >500 

def factors(n):
    res = []
    sqrt_n = int(n**0.5)
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            res.append(n)
            if i != n // i:
                res.append(n // i)
    return len(res)

for num in range(100000000000000000):
    tri_num = sum(range(num+1))
    if factors(tri_num) > 500:
        break
print(f"{tri_num = }")

## CoT
## I could do this with a single list comp, but let's get it done first.
#factors = [i for i in range(1, int(tri_num**0.5) + 1) if tri_num % i == 0]
