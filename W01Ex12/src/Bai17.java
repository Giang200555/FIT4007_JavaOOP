import java.util.Scanner;

public class Bai17 {
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap vao n: ");
        int n = sc.nextInt();

        if (n == 0) {
            System.out.println("n la zero.");
        } else if (n % 2 == 0) {
            System.out.println("n la so chan.");
        } else {
            System.out.println("n la so le");
        }
    }
}
