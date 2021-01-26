# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# write a function 'can_sum(target_sum,numbers)' that takes in a target sum and an array of numbers as arguments.
# The function shuld return a boolean indicating wether or not it is possible to generate the target_sum using numbers from the array.
# constraints:
# - You may use an element of the array as many times as needed.
# - You may assume that all inpot numbers are nonnegative.

# Una forma de pensar el problema es ir restando, a numero objetivo, todos los elementos de la lista. De esta forma si con alguna combinacion
# llego a cero quiere decir que hay una combinacion que suma el numero objetivo.

def can_sum_recursive(target_sum, numbers):
    # Un caso base es cuando el numero objetivo de la suma es cero. En ese caso devuelvo true ya que
    # llegue a una resta de numeros que llega al numero objetivo
    if target_sum == 0:
        return True
    # Otro caso base es cuando el numero objetivo es negativo. En ese caso devuelvo false ya que como todos los numero de la lista son
    # positivos al restarlos nunca voy a llegar a cero.
    if target_sum < 0:
        return False

    # Por ultimo recorro la lista de numeros para restarlos al numero objetivo recursivamente
    for num in numbers:
        remainder = target_sum - num
        if(can_sum_recursive(remainder, numbers) == True):
            return True

    return False


print(f"Can sum 7 the list [2,3]: {can_sum_recursive(7,[2,3])}")  # True
# True
print(f"Can sum 7 the list [5,3,4,7]: {can_sum_recursive(7,[5,3,4,7])}")
print(f"Can sum 7 the list [2,4]: {can_sum_recursive(7,[2,4])}")  # False
print(f"Can sum 8 the list [2,3,5]: {can_sum_recursive(8,[2,3,5])}")  # True
print(f"Can sum 300 the list [7,14]: {can_sum_recursive(300,[7,14])}")  # False
