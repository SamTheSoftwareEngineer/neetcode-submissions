class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Loop through each string in the input array
        // Sort the string
        // Insert sorted string into hashmap
        // If the sorted string is already in our hashmap, append the original string to the key list of the sorted string
        // Otherwise, add the sorted string and the list of matching anagrams to the hashmap
        // Iterate through hasmap and put each value in our results array
        // Return the results array

        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
    
        for (String str: strs) {
            char[] temp = str.toCharArray();
            Arrays.sort(temp);
            String sortedString = new String(temp);

            if (map.containsKey(sortedString)) {
                map.get(sortedString).add(str);
            } else {
                List<String> tempList = new ArrayList<>();
                tempList.add(str);

                map.put(sortedString, tempList);
            }
        }

        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            result.add(entry.getValue());
        }
        return result;
    }
}
