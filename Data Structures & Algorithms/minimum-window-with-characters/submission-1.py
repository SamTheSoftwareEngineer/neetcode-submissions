class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        t_counts = Counter(t)
        l = r = matches = 0
        required_matches = len(t_counts)
        
        # keeps track of all counts in the sliding window
        window_counts = defaultdict(int)

        
        ans = (float('inf'), 0, 0)

        while r < len(s):
            current_char = s[r]

            window_counts[current_char] += 1

            if current_char in t_counts and t_counts[current_char] == window_counts[current_char]:
                matches += 1
            
            while l <= r and matches == required_matches:
                to_remove = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[to_remove] -= 1

                if to_remove in t_counts and window_counts[to_remove] < t_counts[to_remove]:
                    matches -= 1 
                
                l += 1 
        
            r += 1 

        return s[ans[1]:ans[2] + 1] if ans[0] != float('inf') else ''





        
        
        
        
        

            

            