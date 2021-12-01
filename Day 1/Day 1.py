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

higher_numbers = 0
prev_rolling_sum = 0
for i in range(0,len(submarine_depths)):
    if i >= 2 and i <= len(submarine_depths)-2:
        rolling_sum = submarine_depths[i] + submarine_depths[i-1] + submarine_depths[i-2]
        if rolling_sum > prev_rolling_sum:
            print(f"{rolling_sum} is higher than {prev_rolling_sum}")
            higher_numbers += 1
        else:
            print(f"{rolling_sum} is NOT higher than {prev_rolling_sum}")
        prev_rolling_sum = rolling_sum

print(higher_numbers)
        
