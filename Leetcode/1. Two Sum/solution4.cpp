class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> map(2048, -1);

        for (int i = 0; i < nums.size(); i++) {
            if (map[(target - nums[i]) & 2047] != -1) {
                return {map[(target - nums[i]) & 2047], i};
            }

            map[nums[i] & 2047] = i;
        }

        throw invalid_argument("No two sum solution");
    }
};