class Solution(object):
    def letterCombinations(self, digits):
        codes={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if len(digits)==0:
            return [""]
        ch=digits[0]
        rres=self.letterCombinations(digits[1:])
        arr=[]
        codech=codes[int(ch)]
        for let in range(len(codech)):
            w=codech[let]
            for i in rres:
                arr.append(w+i)
        return arr



        