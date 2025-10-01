import java.util.Scanner;

public class Main {
    public static void insertion_sort(int[] arr, int len) {
        for (int i = 1; i < len; i++) {
            if (check(arr)==0){
                return;
            }
            for (int j = i; j > 0; j--) {
                if (arr[j] < arr[j - 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = temp;
                } else {
                    break;
                }
            }
        }
    }
    
    public static int check(int arr[]){
        int index=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]<arr[i+1]){
                index=0;
                continue;
            }
            else{
                index=1;
                break;
            }
        }
        return index;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int index_length = scan.nextInt();
        int[] arr = new int[index_length];
        for (int i = 0; i < index_length; i++) {
            arr[i] = scan.nextInt();
        }
        insertion_sort(arr, index_length);
        for (int i = 0; i < index_length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
