import java.util.Scanner;
public class Main {
    public static void bubble(int[] arr, int len) {
        for (int j = 0; j < len - 1; j++) {
            for (int i = 0; i < len - 1 - j; i++) {
                if (arr[i] > arr[i + 1]) {
                    int swap = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = swap;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];
        
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        bubble(arr, len);
        
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}


// modified bubble sort with less time complexity

import java.util.Scanner;

public class Main {
    public static void bubble(int[] arr, int len) {
        if (check(arr)==0){
            return;
        }
        else{
            for (int j = 0; j < len - 1; j++) {
                for (int i = 0; i < len - 1 - j; i++) {
                    if (arr[i] > arr[i + 1]) {
                        int swap = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = swap;
                }
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
        Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];
        
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        bubble(arr, len);
        
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
