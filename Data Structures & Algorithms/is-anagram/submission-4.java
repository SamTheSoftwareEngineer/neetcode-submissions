class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (char c : s.toCharArray()) {
            sMap.put(c, sMap.getOrDefault(c, 0) + 1);
        }

        for (char character : t.toCharArray()) {
            tMap.put(character, tMap.getOrDefault(character, 0) + 1);
        }

        return sMap.toString().equals(tMap.toString());
    }
}
