# import pdb

'''
Write a function 'how_sum(target_sum,numbers) that takes in a target sum and an array of numbers as arguments.

The function shuld return an array containing eny combination eff elements that adds up to exactly the target_sum.
If there is no combination that adds up to the target sum, then return null.

If are multiple combination possible, you may return eny single one.
'''


def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
#        pdb.set_trace()
        remainder_result = how_sum(remainder, numbers)

        if remainder_result is not None:
            remainder_result.append(num)
            return remainder_result

    return None


# [3, 2, 2]
print(f"How sum 7 the list [2,3]: {how_sum(7,[2,3])}")
# [4, 3]
print(
    f"How sum 7 the list [5,3,4,7]: {how_sum(7,[5,3,4,7])}")
# None
print(f"How sum 7 the list [2,4]: {how_sum(7,[2,4])}")
# [2, 2, 2, 2]
print(
    f"How sum 8 the list [2,3,5]: {how_sum(8,[2,3,5])}")
# None
# print(
#    f"How sum 300 the list [7,14]: {how_sum(300,[7,14])}")
