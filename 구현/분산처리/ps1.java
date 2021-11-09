import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        String trim = scanner.nextLine();
        for (int i = 0; i < T; i++){
            String[] s = scanner.nextLine().split(" ");
            int a = Integer.parseInt(s[0]);
            int b = Integer.parseInt(s[1]);
            int res = getNumber(a, b);
            if (res == 0) System.out.println(10);
            else System.out.println(getNumber(a, b));
        }
    }

    public static int getNumber(int a, int b){
        ArrayList arr = new ArrayList();
        int t2 = a % 10;
        arr.add(a % 10);
        while (true){
            int num = (t2 * (a % 10)) % 10;
            if ((a%10) == num) break;
            else t2 = num; arr.add(t2);
        }
        return (int) arr.get((b - 1) % arr.size());
    }
}