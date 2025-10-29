class Solution(object):
    def rotate(self, matrix):
        if len(matrix)==1:
            return matrix
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(n):
            for j in range(n//2):
                temp=matrix[i][n-j-1]
                matrix[i][n-j-1]=matrix[i][j]
                matrix[i][j]=temp
        return matrix
