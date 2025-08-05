class Solution(object):
    def productExceptSelf(self, nums):
        prodval=1
        arr=[]
        flag=1
        nonzero=False
        countzero=0
        for i in nums:
            if i!=0:
                prodval*=i
                nonzero=True
            else:
                flag=0
                countzero+=1
        if not nonzero:
            prodval=0
        if countzero>1:
            prodval=0
        for i in nums:
            if i !=0 and flag:
                arr.append(prodval/i)
            elif i==0:
                arr.append(prodval)
                flag=0
            elif flag==0:
                 arr.append(0)

        return arr
        