class Solution(object):
    def spiralOrder(self,matrix):
        rowstart, colstart = 0, 0
        rowend, colend = len(matrix) - 1, len(matrix[0]) - 1
        tot = (rowend + 1) * (colend + 1)
        count = 0
        res = []

        while count < tot:
            # left → right
            for col in range(colstart, colend + 1):
                res.append(matrix[rowstart][col])
                count += 1
                if count >= tot: break
            rowstart += 1

            # top → bottom
            for row in range(rowstart, rowend + 1):
                res.append(matrix[row][colend])
                count += 1
                if count >= tot: break
            colend -= 1

            # right → left
            if rowstart <= rowend:
                for col in range(colend, colstart - 1, -1):
                    res.append(matrix[rowend][col])
                    count += 1
                    if count >= tot: break
                rowend -= 1

            # bottom → top
            if colstart <= colend:
                for row in range(rowend, rowstart - 1, -1):
                    res.append(matrix[row][colstart])
                    count += 1
                    if count >= tot: break
                colstart += 1

        
        return res





            
