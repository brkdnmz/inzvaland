import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            a -= b;
            int cnt = 0;
            for (int i = b; i <= Math.abs(a); i++) {
                cnt += a % i == 0 ? 1 : 0;
            }
            if (a == 0)
                cnt = -1;
            System.out.println(cnt);
        }
        sc.close();
    }
}