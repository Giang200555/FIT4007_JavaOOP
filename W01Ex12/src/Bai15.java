import java.util.Scanner;
import java.util.Arrays;

public class Bai15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhập vào số lượng phần tử của mảng: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Số lượng phần tử phải lớn hơn 0.");
            return;
        }

        int[] myArray = new int[n];
        System.out.println("Nhập các phần tử cho mảng: ");
        for (int i = 0; i < n; i++) {
            System.out.print("Nhập phần tử thứ " + i + ": ");
            myArray[i] = sc.nextInt();
        }

        Arrays.sort(myArray);

        System.out.println("Phần tử nhỏ nhất: " + myArray[0]);

        System.out.println("Phần tử lớn nhất: " + myArray[n-1]);
    }
}
