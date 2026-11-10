class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for word in strs:
            ans+=str(len(word))+'#'+word
        return ans

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i<len(s):
            length=0
            numberAndHash = 1
            for j in range(i, len(s)):
                if s[j]=='#':
                    break
                length = s[i:j+1]
                numberAndHash+=1
            length = int(length)
            print("word: ", s[i+numberAndHash:i+numberAndHash+length], "length: ", length)
            #print("length ", length, 'word ', s[i+2:i+2+length])
            res.append(s[i+numberAndHash:i+numberAndHash+length])
            i+=length + numberAndHash
        return res

