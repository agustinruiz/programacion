import pdb


def best_sum_recursive(target_sum, numbers):
    ''' Solucion recursiva
        m = target_sum
        n = len(numbers)
        time complexity: O(n^m)
        space complexity: O(m*m) = O(m^2)
    '''
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


def best_sum_recursive_memoized(target_sum, numbers, memo):
    ''' Solucion recursiva con memoizacion
        m = target_sum
        n = len(numbers)
        time complexity: O(n*m*m) = O(n * m^2) -> la ultima multiplicacion por m la agrega el crear la lista combination ya que copia
                                                    todos los elementos de la lista y en el peor de los casos es m.
        space complexity: O(m*m) = O(m^2)
    '''
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        result_remainder = best_sum_recursive_memoized(
            remainder, numbers, memo)
        if result_remainder is not None:
            # armo la combinacion que resuelve el target_sum
            # Tengo que concatenar dos listas y generar una nueva
            # combination = [y for x in [result_remainder, [num]] for y in x] # usando comprehencion es + dificil de entender
            # combination = [*result_remainder, *[num]] # Con el nuevo operador *. a partir de python 3.6
            # la clasica concatenacion con el operados suma
            combination = result_remainder + [num]
            # Si la combinacion es mas corta que el "mas corto" hago el update
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination

            '''
            # Antes lo habia resuelto asi:
            result_remainder.append(num)
            if (shortest_combination is None) or (len(result_remainder) < len(shortest_combination)):
               shortest_combination = result_remainder[:]
            #Pero esto me daba error en el ultimo test ya que agregaba el numero al result_remainder en lugar de crear una lista nueva para
            # evaluar la combinacion. Esto generaba que se agreguen numeros a la lista que no correspondian.
            '''

    memo[target_sum] = shortest_combination

    return shortest_combination


# [7]
print(
    f"Best sum 7 the list [5,3,4,7]: {best_sum_recursive_memoized(7,[5,3,4,7],{})}")
# [3,5]
print(
    f"Best sum 8 the list [2,3,5]: {best_sum_recursive_memoized(8,[2,3,5],{})}")
# [4,4]
# pdb.set_trace()
print(
    f"Best sum 8 the list [1,4,5]: {best_sum_recursive_memoized(8,[1,4,5],{})}")
# [25, 25, 25, 25]
print(
    f"Best sum 100 the list [1,2,5,25]: {best_sum_recursive_memoized(100,[1,2,5,25],{})}")
