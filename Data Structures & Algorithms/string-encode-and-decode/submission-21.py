class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for word in strs:
            print("length=", len(word))
            ans+=str(len(word))+word
        return ans

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i<len(s):
            length = int(s[i])+1
            print("length ", length, 'word ', s[i+1:i+length])
            res.append(s[i+1:i+length])
            i+=length
        return res

