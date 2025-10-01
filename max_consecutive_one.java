import java.util.*;

public class Main
{
    static int max_consecutive_one(int []arr,int len){
        int max=0,temp=0;
        for(int i=0;i<len;i++){
            if (arr[i]==1){
                temp+=1;
            }
            else{
                if(temp>max){
                    max=temp;
                }
                temp=0;
            }
        }
        return max;
    }
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int len = input.nextInt();
        int[] arr = new int[len];
        
        for (int i = 0; i < len; i++) {
            arr[i] = input.nextInt();
        }
        
        System.out.printf("max_consecutive_one :%d", max_consecutive_one(arr,len));
	}
}