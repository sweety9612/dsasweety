class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dictmag={}
        dictran={}
        for i in magazine:
            dictmag[i]=dictmag.get(i,0)+1
        for i in ransomNote:
            dictran[i]=dictran.get(i,0)+1
        print(dictmag,'dictmag')
        for i in ransomNote:
            if (dictmag.get(i,0)//dictran[i])<1:
                return False
        return True

        
        