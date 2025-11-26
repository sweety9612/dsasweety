class Solution(object):
    def maxNumberOfBalloons(self, text):
        ballondict={
            'b':1,
            'a':1,
            'l':2,
            'o':2,
            'n':1
        }
        textdict={}
        for i in text:
            if i in ballondict:
                textdict[i]=textdict.get(i,0)+1
        print(textdict)
        print(len(textdict))
        if len(textdict)<5:
            print('kkk')
            return 0
        count=textdict['b']
        for i,val in ballondict.items():
            val=textdict[i]//ballondict[i]
            count=min(count,val)
            print(ballondict[i],'b ',textdict[i],'t ', i,' ',val)
            
        return count
        