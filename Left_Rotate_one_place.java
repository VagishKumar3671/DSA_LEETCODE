import java.util.Scanner;

public class Main
{
    static void Left_Rotate_one_place(int []arr,int len){
        int temp=arr[0];
        for(int i=1;i<len;i++){
            arr[i-1]=arr[i];
        }
        arr[len-1]=temp;
        for (int i=0;i<len;i++){
	        System.out.print(arr[i]+" ");
	    }
    }
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
	    int index_lengt=scan.nextInt();
	    int[] arr = new int[index_lengt];
	    for (int i=0;i<index_lengt;i++){
	        arr[i]=scan.nextInt();
	    }
	    Left_Rotate_one_place(arr,len);
	    scan.close()
	}
}