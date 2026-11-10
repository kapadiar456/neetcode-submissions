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
            for word in cache[letter]:
                prev = i+len(word)
                print(s[i])
                if len(word) + i > len(s):
                    dp[i] == False
                elif dp[prev] == True and s[i:i+len(word)] == word:
                    dp[i] = True
        for val in dp:
            print(val)
        return dp[0]
