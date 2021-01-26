# Sos un viajero en una grilla 2D. Empezas en la esquina superior izquierda y tu objetivo es ir a la esquina
# inferior derecha. Solo te podes mover hacia abajo o a la derecha. Es
# ¿De cuantas formas podes viajar en una grilla de m x n?

def grid_traveler_recursive(m, n):
    ''' Solucion recursiva '''
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler_recursive(m-1, n) + grid_traveler_recursive(m, n-1)


def grid_traveler_recursive_memo(m, n, memo={}):
    ''' Solucion recursiva con memoizacion para optimizar el tiempo '''
    #La clave es la combinacion de ambos argumentos. Los separamos por coma porque si dejamos solo los 
    # numeros por ej una clave 2,42 seria igual que 24,2 
    key = str(m) + ',' + str(n) 
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler_recursive_memo(
        m-1, n, memo) + grid_traveler_recursive_memo(m, n-1, memo)
    return memo[key]


print(f"Recorridos 2x2: {grid_traveler_recursive_memo(2,2)}")
print(f"Recorridos 2x3: {grid_traveler_recursive_memo(2,3)}")
print(f"Recorridos 3x3: {grid_traveler_recursive_memo(3,3)}")
