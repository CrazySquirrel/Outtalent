class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (map.find(complement) != map.end()) {
                return {map[complement], i};
            }

            map[nums[i]] = i;
        }

        throw invalid_argument("No two sum solution");
    }
};