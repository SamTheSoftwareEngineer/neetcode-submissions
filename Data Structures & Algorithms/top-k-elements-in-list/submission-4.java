class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count the number of occurrences for each element 
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        List<List<Integer>> temp = new ArrayList<>();

        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            temp.add(List.of(entry.getKey(), entry.getValue()));
        }

        temp.sort((a, b) -> Integer.compare(b.get(1), a.get(1)));

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = temp.get(i).get(0);
        }
        
        return result;
        }
    }
