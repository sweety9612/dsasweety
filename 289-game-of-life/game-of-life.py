from collections import defaultdict
class Solution(object):
    def gameOfLife(self, board):
        m=len(board)
        n=len(board[0])
        neighbourdict=defaultdict(list)
        count=0
        for row in range(m):
            for col in range(n):
                arr=[]
                neighbourList=self.neghbours([row,col])
                for neighbour in neighbourList:
                    i,j=neighbour[0],neighbour[1]
                    if i>=0 and i<m and j>=0 and j<=n:
                        try:
                            arr.append(board[i][j])
                        except:
                            continue
                count+=1
                name=str([row,col])
                neighbourdict[name]=arr
        print(neighbourdict)
        for row in range(m):
            for col in range(n):
                name=str([row,col])
                nlist=neighbourdict[name]
                livecount=nlist.count(1)
                deadcount=nlist.count(0)
                if board[row][col] and livecount<2:
                    board[row][col]=0
                elif board[row][col] and (livecount==2 or livecount==3):
                    pass
                elif board[row][col] and livecount>3:
                    board[row][col]=0
                elif board[row][col] == 0 and livecount==3:
                    board[row][col]=1
        return board


        
                    


                
        
        
    def neghbours(self,index):
        print(index,'index')
        i=index[0]
        j=index[1]
        neighbourlist=[]
        
        v1=[(i-1),j]
        v2=[(i+1),j]
        h1=[i,j+1]
        h2=[i,j-1]
        drl1=[(i-1),(j-1)]
        drl2=[(i+1),(j+1)]
        dlr1=[(i-1),(j+1)]
        dlr2=[(i+1),(j-1)]
        neighbourlist=[v1,v2,h1,h2,drl1,drl2,dlr1,dlr2]
        return neighbourlist

        