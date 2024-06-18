class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seent = new HashMap<>();

        for(int i=0; i < nums.length; i++){
            int diff = target - nums[i];

            if (seent.containsKey(diff)) {
                return new int[] {seent.get(diff), i};
            }

            seent.put(nums[i], i);
        }

        return new int[]{};
        
    }
}
