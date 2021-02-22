# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# write a function 'can_sum(target_sum,numbers)' that takes in a target sum and an array of numbers as arguments.
# The function shuld return a boolean indicating wether or not it is possible to generate the target_sum using numbers from the array.
# constraints:
# - You may use an element of the array as many times as needed.
# - You may assume that all inpot numbers are nonnegative.

def can_sum(target_sum, numbers):
    table = [False]*(target_sum+1)
    table[0] = True

    for i in range(target_sum+1):
        if table[i] == True:
            for num in numbers:
                if i+num <= target_sum:
                    table[i+num] = True
    return table[target_sum]


# True
print(f"Can sum 7 the list [2,3]: {can_sum(7,[2,3])}")
# True
print(
    f"Can sum 7 the list [5,3,4,7]: {can_sum(7,[5,3,4,7])}")
# False
print(f"Can sum 7 the list [2,4]: {can_sum(7,[2,4])}")
# True
print(
    f"Can sum 8 the list [2,3,5]: {can_sum(8,[2,3,5])}")
# False
print(
    f"Can sum 300 the list [7,14]: {can_sum(300,[7,14])}")
