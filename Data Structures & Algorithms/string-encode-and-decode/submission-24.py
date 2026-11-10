class Solution:
    # sand, dog
    # 10#sand#3dog
    def encode(self, strs: List[str]) -> str:
        finalString = ''
        for word in strs:
            finalString+=str(len(word))
            finalString+='#'
            finalString+=word
        return finalString

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            length = 0
            for j in range(i+1, len(s)):
                #print(s[i:j+1])
                if s[j]=='#':
                    length=int(s[i:j])
                    res.append(s[j+1:j+1+length])
                    i = j+1+length
                    break
        return res
