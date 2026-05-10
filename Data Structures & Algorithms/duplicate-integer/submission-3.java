class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for (int value : nums) {
            if (set.contains(value)) {
                return true;
            } else {
                set.add(value);
            }
        }
        return false;
    }

}