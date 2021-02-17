'''
- Write a function 'all_construct(target,word_bank) that accept a target string and an array of strings.
- The function should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements
  of the word_bank array. Each Element of the 2D array should reresent one combination that constructs the target.
- We may reuse elements of word_bank as many times as needed

Primero tengo que entender el problema viendo algunos ejemplos:
all_construct(purple,[purp,p,ur,le,purp])-> [                   -> representa la coleccion de todas las combinaciones
                                                [purp, le],     -> Representa una de las combinaciones
                                                [p,ur,p,le]
                                            ]

all_construct(abcdef,[ab,abc,cd,def,abcd,ef,c]) ->  [ 
                                                        [ab,cd,ef],
                                                        [ab,c,def],
                                                        [abc,def],
                                                        [abcd,ef]
                                                    ]

Segundo busco que responder en los escenarios base:
all_construct(hello,[cat,dog,mouse]) 
En este caso no es posible formar la palabra por lo que deberia responder una coleccion vacia indicando que la cantidad de combinaciones es cero => return []

all_construct('',[cat,dog,mouse])
En este caso es posible crear el target array, por lo que debemos devolver un array 2D, pero sin tomar ningun elemento => return [[]]

Tercero represento un ejemplo en un diagrama de arbol para entender como procesar las respuestas
Ej: all_construct(abcdef,[ab,abc,cd,def,abcd,ef,c])

                                          abcdef->[[ab,cd,ef],[ab,c,def]] + [[abc,def]] + [[abcd,ef]] -> [[ab,cd,ef],[ab,c,def],[abc,def],[abcd,ef]]
             _______________________________|_______________
             |ab                            |abc            |abcd
             |                              |               |
           cdef->[[cd,ef],[c,def]]          def->[[def]]    ef->[[ef]]
        _____|____                          |               |
        |cd       |c                        |def            |ef
        |         |                         |               |
[[ef]]<-ef       def->[[def]]               ''->[[]]        ''->[[]]
        |         |
        |ef       |def
        |         |
        ''->[[]]  ''->[[]]
'''


def all_construct(target, word_bank):
    if target == '':
        return [[]]

    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = map(lambda way: [word] + way, suffix_ways)
            result.extend(target_ways)

    return result


def all_construct_memoized(target, word_bank, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct_memoized(suffix, word_bank, memo)
            target_ways = map(lambda way: [word] + way, suffix_ways)
            result.extend(target_ways)

    memo[target] = result
    return result


# [['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(
    f"Count construct 'purple' ['purp','p','ur','le','purpl']: {all_construct_memoized('purple',['purp','p','ur','le','purpl'],{})}")
# [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(
    f"Count construct 'abcdef' ['ab','abc','cd','def','abcd','ef','c']: {all_construct_memoized('abcdef',['ab','abc','cd','def','abcd','ef','c'],{})}")
# []
print(
    f"Count construct 'skateboard' ['bo','rd','ate','t','ska','sk','boar']: {all_construct_memoized('skateboard',['bo','rd','ate','t','ska','sk','boar'],{})}")
# [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
print(
    f"Count construct 'enterapotentpot' ['a','p','ent','enter','ot','o','t']: {all_construct_memoized('enterapotentpot',['a','p','ent','enter','ot','o','t'],{})}")
# []
print(
    f"Count construct 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef' ['e','ee','eee','eeee','eeeee','eeeeee']: {all_construct_memoized('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee'],{})}")
# NOTA: Para este ejercicio, este ultimo ejemplo, ya no es el peor escenario. El pero escenario seria un string sin la f final para el cual tendria que
# devolver una gran cantidad de combinaciones posibles.
''' Analizando la complejidad del ejercicio:
Siendo:     m = len(target)
            n = len(word_bank)

*La cantidad de hojas (ultimos nodos del arbol) me indicara cuantos posibles subarrays voy a tener en mi lista. En el peor de los casos sera n, que es la 
cantidad maxima de ramas que pueden salir de un nodo (branching factor), a la m que es el alto maximo del arbol en el peor de los casos.
Por esto tendremos n^m hojas => n^m combinaciones diferentes => n^m subarrays => la solucion es exponencial en tamaño => no se puede hacer mejor que exponencial en este caso

Por esto, la complejidad de tiempo: O(n^m) time -> En este caso, la complejidad de tiempo, no se puede mejorar de exponencial ya que tengo que devolver y copiar todos 
                                                    los subarrays para dar todas las respuestas posibles que son las hoyas finales.
Por esto, la complejidad de espacio: O(m) Space -> En la complejidad de ezspacio siempre nos referimos al stack para las llamadas recursivas. Por esto no la ponemos
                                                    exponencial. En general siempre es el alto del arbol en el peor de los casos. Si consideramos los arrays que
                                                    tenemos que crear, si seria exponencial.

'''
