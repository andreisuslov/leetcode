class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        range_min_length = len(word1) if len(word1) <= len(word2) else len(word2)
        merged = []
        for i in range(range_min_length):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.append(word1[i + 1 :])
        merged.append(word2[i + 1 :])
        return "".join(merged)

if __name__ == "__main__":
    s = Solution()
    w1 = "abc"
    w2 = "def"
    print(s.merge_alternately(w1, w2))
    w1 = "abc"
    w2 = "12"
    print(s.merge_alternately(w1, w2))