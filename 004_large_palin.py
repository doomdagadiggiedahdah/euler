# need to check if the product is a palindrome
# start with the highest numbers and go down from there.
# two 3-digit numbers.
# check if palindrome
# (strated late) (10:34:18) -- (10:36:59) 
# also got wrong... (10:49:36) -- (11:18:04) stopped :,(
# I think it's that I'm only adjusting one value at a time.
# I'm confused at the None return. it was because I had changed the range to 10.


def nice():
    a = 999
    b = 999
    count = 0

    while True:
        num = a * b 
        if str(num) == str(num)[::-1]:
            print(a,b)
            return num 

        if count % 2 == 1:
            a -= 1
        else:
            b -= 1

        count += 1
print(nice())



# so now what am I thinking? how should I do this?
# what the hell.
# shouldn't get frustrated. take it step by step.
# wnat to find the largest number, 
# I'm definitely getting the palindrome right.
# gonna come back to this.
