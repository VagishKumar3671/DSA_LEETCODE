import java.util.Scanner;

public class Main
{
    static void Remove_duplicates(int []arr,int len){
        int j=0;
        for(int i=1;i<len;i++){
            if(arr[j]!=arr[i]){
                arr[j+1]=arr[i];
                j++;
            }
            else{
                continue;
            }
        }
        for(int i=j+1;i<len;i++){
            arr[i]=0;
        }
        for(int i=0;i<len;i++){
            if (arr[i]==0){
                continue;
            }
            else{
                System.out.print(arr[i]+" ");
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
        Remove_duplicates(arr,len);
	}
}