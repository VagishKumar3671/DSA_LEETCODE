import java.util.*;

public class Main {
    public int maxSubArray(int[] nums) {
        int maxi=Integer.MIN_VALUE,n=nums.length,sum=0;
        if (n==1){
            if(nums[0]<0){
                return -1;
            }
            else{
                return nums[0];
            }
        }
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            if (sum > maxi) {
                maxi = sum;
            }
            if (sum < 0) {
                sum = 0;
            }
        }
        return maxi;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("No.s of elements:");
        int len = input.nextInt();
        int[] arr = new int[len];

        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }

        System.out.printf("Maximum Subarray Sum: %d%n", new Main().maxSubArray(arr));
    }
}
