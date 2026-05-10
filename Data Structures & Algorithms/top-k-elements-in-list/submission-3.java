class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Count frequencies
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int value : nums) {
            frequencyMap.put(value, frequencyMap.getOrDefault(value, 0) + 1);
        }

        // Step 2: Convert to a list of [element, frequency]
        List<List<Integer>> temp = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            temp.add(List.of(entry.getKey(), entry.getValue()));
        }

        // Step 3: Sort by frequency descending
        temp.sort((a, b) -> Integer.compare(b.get(1), a.get(1)));

        // Step 4: Build result array from top k
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = temp.get(i).get(0); // get the element
        }

        return result;
    }
}
