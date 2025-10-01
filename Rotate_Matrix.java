import java.util.Scanner;

public class Main {
    void swap(int[][] arr, int x1, int y1, int x2, int y2) {
        int temp = arr[x1][y1];
        arr[x1][y1] = arr[x2][y2];
        arr[x2][y2] = temp;
    }

    void Rotate_Matrix(int[][] arr, int len) {
        if(len==1){
            return;
        }
        
        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                swap(arr, i, j, j, i);
            }
        }

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len / 2; j++) {
                swap(arr, i, j, i, len - j - 1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("size of the matrix: ");
        int len = input.nextInt();
        int[][] arr = new int[len][len];

        System.out.println("matrix elements:");
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                arr[i][j] = input.nextInt();
            }
        }

        Main main = new Main();
        main.Rotate_Matrix(arr, len);

        System.out.println("Rotated Matrix:");
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
