import java.util.Scanner;

public class Main {
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void sortedarr(int[] arr, int num) {
        int low = 0, mid = 0, high = num - 1;
        
        while (mid <= high) {
            if (arr[mid] == 0) {
                swap(arr, low, mid);
                low++;
                mid++;
            } else if (arr[mid] == 2) {
                swap(arr, mid, high);
                high--;
            } else {
                mid++;
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("number of elements:");
        int len = input.nextInt();
        int[] arr = new int[len];
        
        System.out.println("elements (0, 1, or 2):");
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        sortedarr(arr, len);
        
        System.out.println("\nsorted arr");
        for (int i = 0; i < len; i++) {
            System.out.print(arr[i] + " ");
        }
        
    }
}
