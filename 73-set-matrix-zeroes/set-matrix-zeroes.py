class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    self.makechange(matrix,[row,col])
        print('updated matrix ',matrix)
        for row in range(m):
            for col in range(n):
                if 'A' in  str(matrix[row][col]):
                    matrix[row][col]=0
        
        return matrix
    
    def makechange(self,matrix,index):
        i=index[0]
        j=index[1]

        for row in range(len(matrix)):
            if row != i and matrix[row][j]!=0 :
                val=str(matrix[row][j])
                matrix[row][j]=val+'A'
        for col in range(len(matrix[0])):
            if col!=j and matrix[i][col]!=0:
                val=str(matrix[i][col])
                matrix[i][col]=val+'A'




        