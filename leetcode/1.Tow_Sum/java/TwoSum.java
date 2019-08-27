public class TwoSum {

    private static int[] towSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++) {
            for(int j = i +1; j < nums.length; ++j) {
                if(nums[i] + nums[j] == target)
                    return new int[] {i, j};
            }
        }
        return new int[0];
    }

    public static void main(String[] args) {
        int[] myList = {1, 3, 5, 7, 9};
        int target = 4;
        int[] result = towSum(myList, target);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }
}
