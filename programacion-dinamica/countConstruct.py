'''
- Write a function 'count_construct(target,word_bank) that accept a target string and an array of strings.
- The function should return the number of ways that the target can be constructed by concatenating elements
  of the word_bank array.
- We may reuse elements of word_bank as many times as needed
'''


def count_construct(target, word_bank):
    if target == '':
        return 1

    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            count += count_construct(suffix, word_bank)
    return count


# 2
print(
    f"Count construct 'purple' ['purp','p','ur','le','purpl']: {count_construct('purple',['purp','p','ur','le','purpl'])}")
# 1
print(
    f"Count construct 'abcdef' ['ab','abc','cd','def','abcd']: {count_construct('abcdef',['ab','abc','cd','def','abcd'])}")
# 0
print(
    f"Count construct 'skateboard' ['bo','rd','ate','t','ska','sk','boar']: {count_construct('skateboard',['bo','rd','ate','t','ska','sk','boar'])}")
# 4
print(
    f"Count construct 'enterapotentpot' ['a','p','ent','enter','ot','o','t']: {count_construct('enterapotentpot',['a','p','ent','enter','ot','o','t'])}")
# False
print(
    f"Count construct 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef' ['e','ee','eee','eeee','eeeee','eeeeee']: {count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee'])}")
