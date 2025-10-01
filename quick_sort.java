import java.util.Scanner;
public class Main
{
    public static void quick_sort(int []arr,int low,int high){
        if (low>=high){
            return;
        }
        else{
            int main_piviot=piviot_function(arr,low,high);
            quick_sort(arr,low,main_piviot-1);
            quick_sort(arr,main_piviot+1,high);
        }
    }
    public static int piviot_function(int []arr,int low,int high){
        int piviot = arr[low];
        int i = low + 1;
        int j = high;
        while (i <= j) {
            while (i <= high && arr[i] <= piviot) { 
                i++;
            }   
            while (j >= low && arr[j] > piviot) { 
                j--;
            }
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        arr[low] = arr[j];
        arr[j] = piviot;
        return j;
    }
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];

        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }

        quick_sort(arr, 0, len - 1);

        for (int num : arr) {
            System.out.print(num + " ");
        }
	}
}