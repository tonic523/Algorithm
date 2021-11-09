import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        while (count-- != 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int r = a;

            for (int i = 2; i <= b; i++) r = (r * a) % 10;
            if (r == 0) r = 10;

            System.out.println(r);
        }
        sc.close();
    }
}