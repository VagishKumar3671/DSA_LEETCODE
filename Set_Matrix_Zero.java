import java.util.*;

public class Main {
    static void martix(int[][] arr, int row, int col) {
        boolean firstRowZero = false;
        boolean firstColZero = false;

        for (int j = 0; j < col; j++) {
            if (arr[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }

        for (int i = 0; i < row; i++) {
            if (arr[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }

        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (arr[i][j] == 0) {
                    arr[i][0] = 0;
                    arr[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < row; i++) {
            if (arr[i][0] == 0) {
                for (int j = 1; j < col; j++) {
                    arr[i][j] = 0;
                }
            }
        }


        for (int j = 1; j < col; j++) {
            if (arr[0][j] == 0) {
                for (int i = 1; i < row; i++) {
                    arr[i][j] = 0;
                }
            }
        }

        
        if (firstRowZero) {
            for (int j = 0; j < col; j++) {
                arr[0][j] = 0;
            }
        }

        
        if (firstColZero) {
            for (int i = 0; i < row; i++) {
                arr[i][0] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter number of rows: ");
        int row = input.nextInt();
        System.out.println("Enter number of columns: ");
        int col = input.nextInt();
        
        int[][] arr = new int[row][col];
        
        System.out.println("Enter the matrix elements: ");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                arr[i][j] = input.nextInt();
            }
        }
        
        martix(arr, row, col);
        
        
        System.out.println("Modified matrix:");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}


////////another kindy


import java.util.*;

public class Main
{
    static void check(int [][]arr, int row, int isRow){
        if(isRow == 1){
            for (int i = 0; i < row; i++){
                for (int j = 0; j < row; j++){
                    if(arr[i][j] == 0){
                        arr[i][0] = -1;
                        break;
                    }
                }
            }
        }
        else{
            for (int j = 0; j < row; j++){
                for (int i = 0; i < row; i++){
                    if(arr[i][j] == 0){
                        arr[0][j] = -1;
                        break;
                    }
                }
            }
        }
    }

    static void zeroRows(int[][] arr, int row) {
        for (int i = 1; i < row; i++){
            if (arr[i][0] == -1){
                for (int j = 0; j < row; j++){
                    arr[i][j] = 0;
                }
            }
        }
    }

    static void zeroColumns(int[][] arr, int row) {
        for (int j = 1; j < row; j++){
            if (arr[0][j] == -1){
                for (int i = 0; i < row; i++){
                    arr[i][j] = 0;
                }
            }
        }
    }

    static void Set_Matrix_Zero(int [][]arr, int row){
        check(arr, row, 1);
        check(arr, row, 0);
        zeroRows(arr, row);
        zeroColumns(arr, row);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter number of rows & columns: ");
        int row = input.nextInt();
        
        int[][] arr = new int[row][row];
        
        System.out.println("Enter the matrix elements: ");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < row; j++) {
                arr[i][j] = input.nextInt();
            }
        }
        
        Set_Matrix_Zero(arr, row);
        
        System.out.println("\n");
        
        System.out.println("Modified matrix:");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < row; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
