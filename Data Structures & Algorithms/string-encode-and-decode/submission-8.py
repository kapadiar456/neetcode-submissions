class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        result = ''
        for string in strs:
            result+=str(len(string))+'#'
            result+=string
        return result

    def decode(self, s: str) -> List[str]:
        print("String: ", s)
        res = []
        for i in range(len(s)):
            if s[i].isdigit():
                print('digit: ',s[i])
                numberLength = 0
                for j in range(i, len(s)):
                    if s[j] == '#':
                        break
                    elif s[j].isdigit():
                        numberLength+=1
                #print("snippet", s[i: i+numberLength])
                length = int(s[i: i+numberLength])
                #print("length", length)
                word = s[i+2: i+2+length]
                res.append(word)
        return res