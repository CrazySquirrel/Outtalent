class Solution {
    public int[] twoSum(int[] nums, int target) {
        Integer[] map = new Integer[2048];

        for (int i = 0; i < nums.length; i++) {
            int complement = (target - nums[i]) & 2047;

            if (map[complement] != null) {
                return new int[]{map[complement], i};
            }

            map[nums[i] & 2047] = i;
        }

        throw new IllegalArgumentException("No two sum solution");
    }
}