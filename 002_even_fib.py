# get your fib
# take all teh even values below 4 million
# sum together
# (10:00:10) -- (10:09:45) 
# didn't get it right :,( (10:43:54) -- (10:47:02) 
# forgot about two!

def gen_fib():
    upper_lim = 4000001
    #upper_lim = 100
    a = 1
    b = 2
    
    summm = 2
    fib = 0
    while fib <= upper_lim:
        if fib % 2 == 0:
            summm += fib

        fib = a + b 
        a = b
        b = fib
        print(fib)
    print(f"final: {summm}")
    
gen_fib()
