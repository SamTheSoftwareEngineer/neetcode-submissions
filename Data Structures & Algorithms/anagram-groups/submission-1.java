class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (String s: strs) {
            char[] temp = s.toCharArray();
            Arrays.sort(temp);
            String sortedString = new String(temp);

            if (map.containsKey(sortedString)) {
                map.get(sortedString).add(s);
            } else {
                List<String> tempList = new ArrayList<>();
                tempList.add(s);
                map.put(sortedString, tempList);
            }
        }

        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            result.add(entry.getValue());
        }

        // Loop through each string in the input array
        // Sort the string
        // Insert into hashmap
        // Iterate through hasmap and put each value in our results array
        // Return the results array 
        return result;
    }
}
