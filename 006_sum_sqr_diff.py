# get the sum of sqrs, and the sqr of sums for a num.
# sub sQ_sum from sum_sQ
# then do the big number.
# (11:50:28) -- (11:52:20) 

def yup(rng):
    sQ_sum = 0
    sum_sQ = 0

    for i in range(1, rng+1):
        sQ_sum += i**2
        sum_sQ += i
    sum_sQ = sum_sQ**2 
    return sum_sQ - sQ_sum

print(yup(100))
