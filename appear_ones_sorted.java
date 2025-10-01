import java.util.*;

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
    static int appear_ones_sorted(int []arr){
        int len=arr.length,
        temp=arr[0],
        xor_array=0;
        if (len==1){
            return arr[0];
        }
        if (check(arr)!=0){
            divide(arr,0,len-1);
        }
        for (int i=0;i<len;i++){
            if (temp==arr[i]){
                xor_array^=arr[i];
            }
            else{
                temp=arr[i];
                xor_array^=arr[i];
            }
        }
        if (xor_array==0){
            return -1;
        }
        return xor_array;
    }
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];
        
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        System.out.printf("appear_ones_sorted : %d", appear_ones_sorted(arr));
	}
}