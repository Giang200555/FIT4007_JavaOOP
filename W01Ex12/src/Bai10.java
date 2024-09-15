public class Bai10 {
    public static void main(String[] agrs) {
        int i = 1;
        int Total = 0;
        for (; i <= 10; i++) {
            if (i % 2 == 0){
                Total += i;
            }
        }
        System.out.print(Total);
    }
}
