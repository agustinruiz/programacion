'''
- Write a function 'can_construct(target,word_bank) that accept a target string and an array of strings.
- The function should return a boolean indicating whether or not the target can be constructed by concatenating elements
  of the word_bank array.
- We may reuse elements of word_bank as many times as needed
'''


def can_construct(target, word_bank):
    if target == '':
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            # Si puedo construir el substring devuelvo True
            if can_construct(suffix, word_bank):
                return True
    return False


# True
print(
    f"Can construct 'abcdef' ['ab','abc','cd','def','abcd']: {can_construct('abcdef',['ab','abc','cd','def','abcd'])}")
# False
print(
    f"Can construct 'skateboard' ['bo','rd','ate','t','ska','sk','boar']: {can_construct('skateboard',['bo','rd','ate','t','ska','sk','boar'])}")
# True
print(
    f"Can construct 'enterapotentpot' ['a','p','ent','enter','ot','o','t']: {can_construct('enterapotentpot',['a','p','ent','enter','ot','o','t'])}")
# False
print(
    f"Can construct 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef' ['e','ee','eee','eeee','eeeee','eeeeee']: {can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee'])}")
