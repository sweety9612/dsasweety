class Solution(object):
    def rotate(self, matrix):
        for row in range(len(matrix)):
            for col  in range(row,len(matrix[0])):
                temp=matrix[row][col]
                matrix[row][col]=matrix[col][row]
                matrix[col][row]=temp
        print(matrix)

        for row in range(len(matrix)):
            matrix[row]=matrix[row][::-1]
        
        return matrix

        