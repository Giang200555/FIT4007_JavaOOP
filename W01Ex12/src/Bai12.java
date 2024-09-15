public class Bai12 {
    public static void main(String[] args) {
        int i = 1;
        int BoiSo;

        while (true) {
            BoiSo = i * 7;
            if (BoiSo >= 100) {
                break;
            }
            System.out.println(BoiSo);
            i++;
        }
    }
}