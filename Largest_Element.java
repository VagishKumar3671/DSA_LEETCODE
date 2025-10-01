import java.util.Scanner;
public class Main
{
    static void Largest_Element(int []arr,int len){
        int max=arr[0];
        int count=0;
        for(int i=0;i<len;i++){
            if (max<=arr[i]){
                max=arr[i];
                count=i;
            }
            else{
                continue;
            }
        }
        System.out.printf("Largest Element: %d\nIndex: %d\n", max, count);
    }
    
    static int largest_number(int []arr,int len){
        int max=arr[0];
        for(int i=0;i<len;i++){
            if (max<=arr[i]){
                max=arr[i];
            }
            else{
                continue;
            }
        }
        return max;
    }
    
    static int Largest_Element_Index(int []arr,int len){
        int max=arr[0];
        int index=0;
        for(int i=0;i<len;i++){
            if (max<=arr[i]){
                max=arr[i];
                index=i;
            }
            else{
                continue;
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
        Largest_Element(arr,len);
        System.out.printf("\nLargest Element: %d",largest_number(arr,len));
        System.out.printf("\nIndex: %d",Largest_Element_Index(arr,len));
	}
}