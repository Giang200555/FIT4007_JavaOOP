import java.util.Scanner;

public class Bai14 {
    public static void main(String[] agrs){
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap vao n: ");
        int n = sc.nextInt();
        int Total = 0;
        if (n % 2 == 0) {
            for (int i = 1; i <= n; i++){
                if (i % 2 != 0){
                    Total += i;
                }
            }
        }
        if (n % 2 != 0) {
            for (int i = 1; i <= n; i++){
                if (i % 2 == 0){
                    Total += i;
                }
            }
        }
        System.out.println(Total);
    }
}
