def best_sum_recursive(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        result_remainder = best_sum_recursive(remainder, numbers)
        if result_remainder is not None:
            # armo la combinacion que resuelve el target_sum
            result_remainder.append(num)
            # Si la combinacion es mas corta que el "mas corto" hago el update
            if shortest_combination is None or len(shortest_combination) > len(result_remainder):
                shortest_combination = result_remainder
    return shortest_combination


# [7]
print(f"Best sum 7 the list [5,3,4,7]: {best_sum_recursive(7,[5,3,4,7])}")
# [3,5]
print(
    f"Best sum 8 the list [2,3,5]: {best_sum_recursive(8,[2,3,5])}")
# [4,4]
print(f"Best sum 8 the list [1,4,5]: {best_sum_recursive(8,[1,4,5])}")
# [25, 25, 25, 25]
print(
    f"Best sum 8 the list [2,3,5]: {best_sum_recursive(100,[1,2,5,25])}")
