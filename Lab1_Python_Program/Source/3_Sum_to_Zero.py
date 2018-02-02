import sys

print("Please enter few numbers to find sum of three number is zero :")
number = sys.stdin.readline().strip('\n').split(" ")

'''
Loop alround list to find three number so that it sum to zero
'''
for a in range(0,len(number)):
    for b in range(a+1,len(number)):
        for c in range (b+1,len(number)):
            if(int(number[a])+int(number[b])+int(number[c]) == 0):
                print("Three number that sums up to Zero :: [",number[a],number[b],number[c],"]")