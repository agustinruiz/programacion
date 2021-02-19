# Sos un viajero en una grilla 2D. Empezas en la esquina superior izquierda y tu objetivo es ir a la esquina
# inferior derecha. Solo te podes mover hacia abajo o a la derecha.
# ¿De cuantas formas podes viajar en una grilla de m x n?

def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0

    '''
        Hay dos formas de acrear un array unidimensional tipicas:
            1a) arr = [0]*N
            1b) arr = [0 for i in range(N)]
        In method 1a, Python doesn’t create 5 integer objects but creates only one integer object and all the indices of the array arr point to the same int object.
        If we assign the 0th index to a another integer say 1, then a new integer object is created with the value of 1 and then the 0th index now points to this new int object.

        Haciendo las formas extensivas a arrays 2D:
            2a) arr = [[0]*cols]*rows
            2b) arr = [[0 for i in range(cols)] for j in range(rows)]
        
        Similarly, when we create a 2d array as “arr = [[0]*cols]*rows” we are essentially the extending the above analogy.
            1. Only one integer object is created.
            2. A single 1d list is created and all its indices point to the same int object in point 1.
            3. Now, arr[0], arr[1], arr[2] …. arr[n-1] all point to the same list object above in point 2.
        
        Now lets change the first element in first row of “arr” as arr[0][0] = 1
            => arr[0] points to the single list object we created we above.(Remember arr[1], arr[2] …arr[n-1] all point to the same list object too)
            => The assignment of arr[0][0] will create a new int object with the value 1 and arr[0][0] will now point to this new int object.(and so will arr[1][0], arr[2][0] …arr[n-1][0])
        So when 2d arrays are created like this, changing values at a certain row will effect all the rows since there is essentially only one integer object and only one list object being referenced by the all the rows of the array.

        Example:
            # Python 3 program to demonstrate working  
            # of method 1 and method 2. 
            
            rows, cols = (5, 5) 
            
            # method 2a 
            arr = [[0]*cols]*rows 
            
            # lets change the first element of the  
            # first row to 1 and print the array 
            arr[0][0] = 1
            
            for row in arr: 
                print(row) 
            # outputs the following 
            #[1, 0, 0, 0, 0] 
            #[1, 0, 0, 0, 0] 
            #[1, 0, 0, 0, 0] 
            #[1, 0, 0, 0, 0] 
            #[1, 0, 0, 0, 0] 
            
            # method 2b 
            arr = [[0 for i in range(cols)] for j in range(rows)] 
            
            # again in this new array lets change 
            # the first element of the first row  
            # to 1 and print the array 
            arr[0][0] = 1
            for row in arr: 
                print(row) 
            
            # outputs the following as expected 
            #[1, 0, 0, 0, 0] 
            #[0, 0, 0, 0, 0] 
            #[0, 0, 0, 0, 0] 
            #[0, 0, 0, 0, 0] 
            #[0, 0, 0, 0, 0]

        IMPORTANTE: De esta forma la mejor forma para crear arrays 2d es: arr = [[0 for i in range(cols)] for j in range(rows)] 

        NOTA: Con el operador is se puede comprobar que apuntan al mismo array
    '''
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    table[1][1] = 1

    for i in range(m+1):
        for j in range(n+1):
            if i < m:
                table[i+1][j] += table[i][j]
            if j < n:
                table[i][j+1] += table[i][j]

    return table[m][n]


print(f"Recorridos 1x1: {grid_traveler(1,1)}")  # 1
print(f"Recorridos 2x2: {grid_traveler(2,2)}")  # 2
print(f"Recorridos 2x3: {grid_traveler(2,3)}")  # 3
print(f"Recorridos 3x2: {grid_traveler(3,2)}")  # 3
print(f"Recorridos 3x3: {grid_traveler(3,3)}")  # 6
print(f"Recorridos 18x18: {grid_traveler(18,18)}")  # 2333606220
