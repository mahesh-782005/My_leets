class Solution {
    public long rob(int[] nums, int[] colors) {
        int n = nums.length;
        if (n == 0) return 0;

        long rob = 0;
        long skip = 0;
        for (int i = 0; i < n; i++) {
            long prevMax = Math.max(rob, skip);
            long currentRob;

            if (i > 0 && colors[i] == colors[i - 1]) {
                currentRob = skip + nums[i];
            }
            else {
                currentRob = prevMax + nums[i];
            }

            skip = prevMax;
            rob = currentRob;
        }

        return Math.max(rob, skip);
    }
}