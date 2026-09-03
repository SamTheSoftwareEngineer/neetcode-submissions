class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> valueIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            
            if (valueIndex.containsKey(diff)) {
                return new int[] {valueIndex.get(diff), i};
            }
            
            valueIndex.put(nums[i], i);
        }
        return new int[] {};
    }
}
