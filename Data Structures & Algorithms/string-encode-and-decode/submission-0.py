class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        result = ''
        for string in strs:
            result+=str(len(string))+'#'
            result+=string
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            if s[i].isdigit():
                length = int(s[i])
                word = s[i+2: i+2+length]
                res.append(word)
        return res