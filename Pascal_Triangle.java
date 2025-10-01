import java.util.*;

public class Main
{
    static void Pascal_Triangle(int n){
        for (int i=0;i<=n;i++){
            int ans=1;
            for(int j=1;j<=i;j++){
                System.out.print(ans + " ");
                ans = ans * (i - j) / j;}
            System.out.println();
        }
    }
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of rows:");
        int len = input.nextInt();
        
        Pascal_Triangle(len);
    }
}
