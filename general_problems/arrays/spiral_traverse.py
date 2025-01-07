def spiralTraverse(array):
    # Print the spiral of a m x n array 

    sol = []

    while array:
        sol += array.pop(0)
        array = list(zip(* array))[::-1]

    return sol