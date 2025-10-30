class Solution:
    def gcd_memory_optimized(self, str1: str, str2: str) -> str:
        range_min_length = min(len(str1), len(str2)) # <-- Corrected to use min()
        common_prefix = []
        for i in range(range_min_length):
            if str1[i] == str2[i]:
                common_prefix.append(str2[i])
            else:
                break
        
        prefix = "".join(common_prefix)
        prefix_len = len(prefix)

        for L in range(prefix_len, 0, -1):
            candidate = prefix[:L]
            len_cand = L

            if len(str1) % len_cand != 0:
                continue 
            times1 = len(str1) // len_cand
            if str1 != candidate * times1:
                continue
            if len(str2) % len_cand != 0:
                continue
            times2 = len(str2) // len_cand
            if str2 != candidate * times2:
                continue
            return candidate
        return ""
    
    def gcd_fast(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for k in range(min(len1, len2), 0, -1):
            if len1 % k or len2 % k:
                continue
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            if str1 == n1 * base and str2 == n2 * base:
                return str1[:k]
        return ""

if __name__ == "__main__":
    s = Solution()

    s1 = "abababab"
    s2 = "ababab"

    print(s.gcd_fast(s1, s2))
    print(s.gcd_memory_optimized(s1, s2))
