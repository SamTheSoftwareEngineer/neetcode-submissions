class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq_map = {}
        result = 0

        for char in text:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        l_count = freq_map.get('l' , 0)
        possible_l_sets = l_count // 2

        b_count = freq_map.get('b', 0)
        a_count = freq_map.get('a', 0)
        o_count = freq_map.get('o', 0)
        possible_o_pairs = o_count // 2
        n_count = freq_map.get('n', 0)

        return min(b_count, a_count, possible_l_sets, possible_o_pairs, n_count)