import java.util.Scanner;

public class Main
{
    static void reverse(int []arr,int start,int end){
        while(start < end){
            int temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
        return;
    }
    static void Left_rotate_array_D_places(int []arr,int len,int d){
        d=d%len;
        if(len<=1 || d==0){
            return;
        }
        reverse(arr,0,d-1);
        reverse(arr,d,len-1);
        reverse(arr,0,len-1);
        for(int i = 0; i < len; i++){
            System.out.print(arr[i]+" ");
        }
    }
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];
        
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        int d=input.nextInt();
        
        Left_rotate_array_D_places(arr,len,d);
	}
}