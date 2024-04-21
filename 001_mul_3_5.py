# get all numbers that are multiples of 3 or 5 below X, sum together.
# (09:54:22) -- (09:57:21)

def get_sum(limit):
   to_sum = 0
   for i in range(limit):
        if (i % 3 == 0) or (i % 5 == 0):
            to_sum += i
   return to_sum
print(get_sum(1000))
