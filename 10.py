def transpose(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    t=[[None]*rows for _ in range(cols)] #create a new matrix with rows&cols and initialize with None
    for i in range(rows):
        for j in range(cols):
            t[j][i]=matrix[i][j]
    return t
def get_input():
    rows=int(input("Enter the number of rows:"))
    cols=int(input("Enter the number of cols:"))
    matrix=[] #initialize an empty matrix
    for _ in range(rows):
        row=list(map(int,input().split()))
        if len(row)!=cols:
            print(f"Each row must have {cols} elements.")#Check the row has correct number of elements or not
            return None
        matrix.append(row)#add the row to the matrix
    return matrix
matrix=get_input() #call the function
if matrix: #if the matrix is valid
    t=transpose(matrix) #Transpose the matrix
    print("Transposed matrix is:")
    for row in t:
        print(row)
