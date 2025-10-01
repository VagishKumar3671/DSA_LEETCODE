import java.util.*;

public class Main
{
    static int missing_number(int []nums){
        int n = nums.length,
        sum_n = n * (n + 1) / 2,
        actual_sum = 0;

        for (int num : nums) {
            actual_sum += num;
        }

        return sum_n - actual_sum;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of elements (including the missing one):");
        int len = input.nextInt();
        
        int []arr = new int[len - 1];
        
        System.out.println("Enter the elements:");
        for (int i = 0; i < len - 1; i++) {
            arr[i] = input.nextInt();
        }
        
        System.out.println("The missing number is: " + missing_number(arr));
    }
}
