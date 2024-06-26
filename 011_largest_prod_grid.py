## (10:45:52) -- (10:56:04) (taking break, need to take care of stuff).
## (13:00:01) -- (13:22:17) (not pretty, but it works)
## immediately running into uncertainty how to check for bounds. I remember doing something sim for Advent of Code.
## bounds check, then compute.
## I think there could be an optimization here if the multiples are too low, but lets get it working first.
## how bounds check? up down are same, (I'm reminded of "only input correct values, don't rely on err handling")
    ## there are three types here: u/d, l/r, diagonal.
    ## for each there would be bounds on where they could act. Verbose, but works.
## how compute the vert?
    ## for ls in ls_ls: mul 08 02 22 97, if > max, that prod == max
## maybe this is too slow, how about have a method for each of the bounds checks that need to be active (if hori, are there four spaces? if no, skip. if yes, calc and compare.)
## the way that I'm going feels like wya too much and will be suuuuper long. It'll work but I think there's a much easier way to go about it.

import numpy as np

nums = """\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

dirty_rows = nums.strip().splitlines()
rows = [row.split(" ") for row in dirty_rows]
rows = [[int(i) for i in row ] for row in rows]
len_row = len(rows[0])
mxm = 0
count = 0

## make the checks, each is run on each index

def get_diag_d():
    ls = []
    adj = 0
    for i in range(4):
        ls.append(rows[row+adj][col+adj])
        adj += 1
    return ls

def get_diag_u():
    ls = []
    adj = 0
    for i in range(4):
        ls.append(rows[row-adj][col+adj])
        adj += 1
    return ls

for row in range(len(rows)):
    for col in range(len_row):
        l_r = np.prod(rows[row][col:col+4])
        u_d = np.prod([row[col] for row in rows[row:row+4]])
        try:
            diag_d = np.prod(get_diag_d())
        except IndexError:
            pass
        try:
            diag_u = np.prod(get_diag_u())
        except IndexError:
            pass

        max_round = max([l_r, u_d, diag_d, diag_u])
        if max_round > mxm:
            mxm = max_round 
        
print(mxm)

## needs u/d, l/r, diag (u/d)

## how tf do I get a diagonal. I'm sure there's a nice looking way for it... basically increase r and c by 1 and take that value.
## also can just go through it with a func and take care of it.
## values: rows[row][col] rows[row+1][col+1] rows[row+2][col+2] rows[row+3][col+3]
## or    : rows[row][col] rows[row-1][col+1] rows[row-2][col+2] rows[row-3][col+3]
## is there a way to add the 
## append to a list, have a count 

## ok, I've gotten all the values, can it run across the entire thing
## It does, now to compare and store top value.

# Hey, nice job taking the first imp of this as "write out a pass for each of the types of lines to be drawn" and finding the 
# simpler way of "all on one pass, create a test for each line and if pass compute / compare (/ store)"
# second one is way less code, and may be simpler. I do wonder if the "only input correct values" thinking I took from Thor has been washed with this new approach.


## Ideas for optimization:
    ## combine the two diag functions
    ## make the try except statements less ugly
    ## combine the rows lines into one, I'm sure this can be done.
