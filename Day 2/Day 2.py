#part 1
##total_forward = 0
##total_depth = 0
##
##with open("input.txt", "r") as fp:
##    for i, line in enumerate(fp):
##        direction, quantity = line.strip().split(" ")
##        if direction == "forward":
##            total_forward += int(quantity)
##        elif direction == "down":
##            total_depth += int(quantity)
##        elif direction == "up":
##            total_depth -= int(quantity)
##        else:
##            print("oops")
##fp.close()
##
##print(total_forward*total_depth)

#part 2 - adding aim
total_forward = 0
total_depth = 0
aim = 0

with open("input.txt", "r") as fp:
    for i, line in enumerate(fp):
        direction, quantity = line.strip().split(" ")
        if direction == "forward":
            total_forward += int(quantity)
            total_depth += aim * int(quantity)
        elif direction == "down":
            aim += int(quantity)
        elif direction == "up":
            aim -= int(quantity)
        else:
            print("oops")
        #print(f"forward:{total_forward} depth:{total_depth} aim:{aim}")
fp.close()

print(total_forward*total_depth)
