'''
- Write a function 'count_construct(target,word_bank) that accept a target string and an array of strings.
- The function should return the number of ways that the target can be constructed by concatenating elements
  of the word_bank array.
- We may reuse elements of word_bank as many times as needed
'''


def count_construct(target, word_bank):
    ''' Solucion recursiva
        m = len(target)
        n = len(word_bank)
        time complexity: O(n^m * m) ) -> Complejidad de tiempo exponencial. la ultima multiplicacion por m la agrega "target[len(word):]" ya que estoy 
                                          copiando la lista casi completa y en el peor de los casos es m.
        space complexity: O(m*m) = O(m^2)
    '''
    if target == '':
        return 1

    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            count += count_construct(suffix, word_bank)
    return count


def count_construct_memoized(target, word_bank, memo):
    ''' Solucion recursiva con memoizacion
        m = len(target)
        n = len(word_bank)
        time complexity: O(n*m*m) = O(n * m^2) -> la ultima multiplicacion por m la agrega "target[len(word):]" ya que estoy copiando la lista casi completa
                                                    y en el peor de los casos es m. Complejidad polinomica no exponencial
        space complexity: O(m*m) = O(m^2)
    '''
    if target in memo:
        return memo[target]
    if target == '':
        return 1

    count = 0
    for word in word_bank:
        if target.startswith(word):
            count += count_construct_memoized(
                target[len(word):], word_bank, memo)
    memo[target] = count
    return count


# 2
print(
    f"Count construct 'purple' ['purp','p','ur','le','purpl']: {count_construct_memoized('purple',['purp','p','ur','le','purpl'],{})}")
# 1
print(
    f"Count construct 'abcdef' ['ab','abc','cd','def','abcd']: {count_construct_memoized('abcdef',['ab','abc','cd','def','abcd'],{})}")
# 0
print(
    f"Count construct 'skateboard' ['bo','rd','ate','t','ska','sk','boar']: {count_construct_memoized('skateboard',['bo','rd','ate','t','ska','sk','boar'],{})}")
# 4
print(
    f"Count construct 'enterapotentpot' ['a','p','ent','enter','ot','o','t']: {count_construct_memoized('enterapotentpot',['a','p','ent','enter','ot','o','t'],{})}")
# False
print(
    f"Count construct 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef' ['e','ee','eee','eeee','eeeee','eeeeee']: {count_construct_memoized('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee'],{})}")
