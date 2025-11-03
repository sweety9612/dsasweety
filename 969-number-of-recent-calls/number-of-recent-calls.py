class RecentCounter(object):

    def __init__(self):
        self.counter=[]
        self.start=-1
        self.end=-1
        

    def ping(self, t):
        if self.end==-1:
            self.counter.append(t)
            self.end+=1
            self.start+=1
            return 1
        else:
            self.counter.append(t)
            self.end+=1
            if t>3000:
                diff=t-3000
                if self.counter[self.start]>=diff:
                    return (self.end - self.start)+1
                else:
                    while self.counter[self.start]<diff:
                        self.start+=1
                    return (self.end - self.start)+1
            else:
                return (self.end - self.start)+1

                

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)