#part 1
##prev = 0
##higher_numbers = 0
##with open("input.txt", "r") as fp:
##    for i, line in enumerate(fp):
##        if int(line) > prev:
##            #print(f"{int(line)} is higher than {prev}")
##            higher_numbers += 1
##        #else:
##            #print(f"{int(line)} is NOT higher than {prev}")
##        prev = int(line)
##fp.close()
##print(higher_numbers-1)

#part 2
with open("input.txt", "r") as fp:
    submarine_depths = [int(line) for i, line in enumerate(fp)]
fp.close()

#since two numbers are the same in the rolling average, should be able to just compare if
#lst[i] < lst[i+3]
higher_numbers = 0
for i in range(0,len(submarine_depths)-3):
    if submarine_depths[i+3] > submarine_depths[i]:
        higher_numbers += 1

assert higher_numbers == 1739
print(higher_numbers)
