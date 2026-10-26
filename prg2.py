def mapper(A,B):
    pairs = []
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                pairs.append(((i,j),A[i][k]*B[k][j]))
    return pairs

def map_reducer(A,B):
    groups = {}
    for key , value in mapper(A,B):
        groups.setdefault(key,[]).append(value)
    return {key: sum(values) for key,values in groups.items()}

def result_to_matrix(result,rows,cols):
    matrix = [[0]*cols for _ in range(rows)]
    for (i,j), value in result.items():
        matrix[i][j] = value
    return matrix

A = [[1,2,3],[4,5,6]]
B = [[7,8],[9,10],[11,12]]

result = map_reducer(A,B)
matrix = result_to_matrix(result,len(A),len(B[0]))

for row in matrix:
    print(row)