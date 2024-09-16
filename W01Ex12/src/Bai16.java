import java.util.Scanner;

public class Bai16 {
    public static void main(String[] agrs){
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap vao a: ");
        int a = sc.nextInt();
        System.out.print("Nhap vao b: ");
        int b = sc.nextInt();
        if (a == 0) {
            if (b == 0) {
                System.out.println("Phuong trinh co vo so nghiem.");
            } else {
                System.out.println("Phuong trinh vo nghiem.");
            }
        } else {
            float x = -b / a;
            System.out.printf("Phuong tinh co nghiem %.2f\n", x);
        }
    }
}
