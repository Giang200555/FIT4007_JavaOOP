import java.util.Scanner;

public class Bai13 {
    public static void main(String[] agrs){
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap vao n: ");
        int n = sc.nextInt();
        int Total = 0;
        for (int i = 1; i <= n; i++){
            Total += i;
        }
        System.out.println(Total);
    }
}
