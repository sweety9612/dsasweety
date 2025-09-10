from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        cube1,cube2,cube3=set(),set(),set()
        cube4,cube5,cube6=set(),set(),set()
        cube7,cube8,cube9=set(),set(),set()
        colsets = defaultdict(set)

        for row in range(len(board)):
            row1=set()
            for col in range(len(board[0])):
                val = board[row][col]
                if val in row1 and str(val)!='.':
                    print("row exit ",val,' ',row1)
                    return False
                row1.add(board[row][col])
                colname='col'+str(col+1)
                
                if val in colsets[colname] and str(val)!='.':
                    print("colset exit ",val,' ',colname,' ',colsets[colname])
                    return False
                if str(val) != '.':
                    colsets[colname].add(val)
                #print('val :',val,' row,col: ',[row,col],' colname: ',colname)
                

                #1st row cube
                if row<3 and col<3:
                    if val in cube1 and str(val)!='.':
                        return False
                    cube1.add(board[row][col])


                if row<3 and col>2 and col<6:
                    if val in cube2 and str(val)!='.':
                        return False
                    cube2.add(board[row][col])
                if row<3 and col>5 and col<9:
                    if val in cube3 and str(val)!='.':
                        return False
                    cube3.add(board[row][col])
                # second row cube
                if row>2 and row<6 and col<3:
                    if val in cube4 and str(val)!='.':
                       return False
                    cube4.add(board[row][col])
                if row>2 and row<6 and col>2 and col<6:
                    if val in cube5 and str(val)!='.':
                        return False
                    cube5.add(board[row][col])
                if row>2 and row<6 and col>5 and col<9:
                    if board[row][col] in cube6 and str(val)!='.':
                        return False
                    cube6.add(board[row][col])

                # third row cube
                if row>5 and row<9 and col<3:
                    if board[row][col] in cube7 and str(val)!='.':
                        return False
                    cube7.add(board[row][col])
                if row>5 and row<9 and col>2 and col<6:
                    if board[row][col] in cube8 and str(val)!='.':
                        return False
                    cube8.add(board[row][col])
                if row>5 and row<9 and col>5 and col<9:
                    if board[row][col] in cube9 and str(val)!='.':
                        return False
                    cube9.add(board[row][col])
        #print(colsets)
        print(cube1)
        return True

        

        
        