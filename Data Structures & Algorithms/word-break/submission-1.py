class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = defaultdict(list)
        for word in wordDict:
            cache[word[0]].append(word)

        dp = [False for _ in range(len(s)+1)]
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            letter = s[i]
            if not cache[letter]:
                dp[i] == False
                continue
            elif letter == s[-1]:
                continue
            for word in cache[letter]:
                prev = i+len(word)
                if dp[prev] == True:
                    dp[i] = True
        for val in dp:
            print(val)
        return dp[0]
