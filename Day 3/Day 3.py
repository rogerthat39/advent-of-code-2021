#part 1
#diagnostic report (input) is list of binary
#gamma rate is most common bit in each position
#epsilon rate is least common bit in each position
#result should be in decimal not binary

from statistics import mode, multimode

def part_one():
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(0, len(binary[0])):
        #get all digits in position i
        bit_list_in_position = [digit[i] for digit in binary]
        #mode finds the most common value
        gamma_rate += mode(bit_list_in_position) 

    #flip all bits to find least common
    epsilon_rate = gamma_rate.replace('1', '2').replace('0', '1').replace('2', '0')

    #int('',2) converts binary to int
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


#part two
def find_O2(binary):
    for i in range(0, len(binary[0])):
        #get digits in position i
        bit_list_in_position = [digit[i] for digit in binary]

        #find the most common value
        #multimode will return [0,1] if there are 2 equal nodes
        #if there is a tie, for O2 generated we want to pick '1' (by sorting it desc)
        most_common_bit = sorted(multimode(bit_list_in_position), reverse=True)[0] 

        #remove items from list that don't have bit in that position
        binary = [line for line in binary if line[i] == most_common_bit]
        
        #only keep checking as long as there's more than 1 item in the list
        if(len(binary) == 1):
            return int(binary[0], 2)

def find_CO2(binary):
    for i in range(0, len(binary[0])):
        #get digits in position i
        bit_list_in_position = [digit[i] for digit in binary]

        #find the least common value (flip of most_common bit)
        most_common_bit = sorted(multimode(bit_list_in_position), reverse=True)[0]
        least_common_bit = '0' if most_common_bit == '1' else '1'

        #remove items from list that don't have bit in that position
        binary = [line for line in binary if line[i] == least_common_bit]
        
        #only keep checking as long as there's more than 1 item in the list
        if(len(binary) == 1):
            return int(binary[0], 2)

#main routine
with open("input.txt", "r") as fp:
    diagnostic_report = [line.strip() for i, line in enumerate(fp)]
fp.close()

#print(part_one())
print(find_O2(diagnostic_report)*find_CO2(diagnostic_report))
