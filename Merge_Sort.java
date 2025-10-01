import java.util.Scanner;

public class Main
{
    public static void divide(int []arr,int low,int hight){
        if (low>=hight){
            return;
        }
        
        int mid=(low+hight)/2;
        
        divide(arr,low,mid);
        divide(arr,mid+1,hight);
        merge(arr,low,mid,hight);
        
    }
    public static void merge(int []arr,int low,int mid,int hight){
        int []leftarr=new int[mid-low+1];
        int []rightarr=new int[hight-mid];
        
        for (int i = 0; i < leftarr.length; i++) {
            leftarr[i] = arr[low + i];
        }
        for (int i = 0; i < rightarr.length; i++) {
            rightarr[i] = arr[mid + 1 + i];
        }
        
        int i=0,j=0,k=low;
        while(i < leftarr.length && j < rightarr.length){
            if(leftarr[i]<=rightarr[j]){
                arr[k]=leftarr[i];
                i++;
            }
            else{
                arr[k]=rightarr[j];
                j++;
            }
            k++;
        }
        
        while (i < leftarr.length) {
            arr[k] = leftarr[i];
            i++;
            k++;
        }

        while (j < rightarr.length) {
            arr[k] = rightarr[j];
            j++;
            k++;
        }
        
    }
    
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];

        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }

        divide(arr, 0, len - 1);

        for (int num : arr) {
            System.out.print(num + " ");
        }
	}
}
