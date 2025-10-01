import java.util.*;

public class Main
{
    static void max_profit(int[] arr, int n) {
        int mini = arr[0], max_pro = 0;
        for (int i = 1; i < n; i++) {
            max_pro = Math.max(max_pro, arr[i] - mini);
            mini = Math.min(mini, arr[i]);
        }
        System.out.println(max_pro); 
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];
        
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        max_profit(arr, len);

    }
}
