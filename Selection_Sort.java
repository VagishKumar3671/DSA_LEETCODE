import java.util.Scanner;
public class Main {
    public static int minval(int[] arr, int index) {
        int min = arr[index];
        for (int i = index; i < arr.length; i++) {
            if (arr[i] <= min) {
                min = arr[i];
            }
        }
        return min;
    }
    public static int id(int[] arr, int index) {
        int id =index;
        int min = arr[index];
        for (int i = index; i < arr.length; i++) {
            if (arr[i] <= min) {
                min = arr[i];
                id=i;
            }
        }
        return id;
    }
	public static void main(String[] args) {
	    Scanner scan=new Scanner(System.in);
	    int index_lengt=scan.nextInt();
	    int[] arr = new int[index_lengt];
	    for (int i=0;i<index_lengt;i++){
	        arr[i]=scan.nextInt();
	    }
	    int swap=0;
	    for (int i=0;i<index_lengt;i++){
	        int min=minval(arr,i);
	        int min_id=id(arr,i);
	        swap=arr[i];
	        arr[i]=min;
	        arr[min_id]=swap;
	    }
	    for (int i=0;i<index_lengt;i++){
	        System.out.println(arr[i]);
	    }
	}
}