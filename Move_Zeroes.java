import java.util.*;

public class Main
{
    static void swap(int []arr,int i,int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    static void Move_all_Zeros(int []arr,int len){
        int i=0;
        int j=-1;
        while (i < len){
            if (arr[i] == 0){
                j = i;
                break;
            }
            i++;
        }
        if (j == -1) {
            return;
        }
        for (i = j; i < len; i++){
            if (arr[i] != 0){
                swap(arr, i, j);
                j++;
            }
        }
    }

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of elements:");
        int len = input.nextInt();
        int []arr = new int[len];
        
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        Move_all_Zeros(arr, len);
        
        for(int i = 0; i < len; i++){
            System.out.print(arr[i] + " ");
        }
	}
}

