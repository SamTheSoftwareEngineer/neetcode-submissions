class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_substring = 0
        curr_chars = set()
        
        while r < len(s):
            if s[r] not in curr_chars:
                curr_chars.add(s[r])
                max_substring = max(max_substring, r - l + 1)
                r += 1
            else:
                curr_chars.remove(s[l])
                l += 1

        
        return max_substring
