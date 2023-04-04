# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

list_of_even = []                       #Q1
for num in numbers:
    if num%2 == 0:
        list_of_even.append(num)
print(list_of_even)

print(max(numbers) - min(numbers))              #Q2

for num in numbers:                             #Q3
    if num == 2:
        if numbers.index(num)+1 or numbers.index(num)-1 == 2:
            print(True)
            break

sum_of_num = 0                              #Q4
add_num = True
for num in numbers:
    if num == 6:
        add_num = False
    elif num == 7:
        add_num = True
    else:
        if add_num:
            sum_of_num += num
        
print(sum_of_num)

sum_of_num_q5 = 0                                       #Q5
flag_num = True
for num in  numbers:
        if num == 13 and flag_num ==  True :
            flag_num = False
        elif num != 13 and  flag_num == False:
            flag_num = True
        else:
            sum_of_num_q5 += num
print(sum_of_num_q5)








