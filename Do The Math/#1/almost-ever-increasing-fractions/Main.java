import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            long sum = a + b;
            int cnt = 0;
            for (long i = 1; i * i <= sum; i++) {
                if (sum % i > 0)
                    continue;
                cnt++;
                cnt += i <= b ? 1 : 0;
                if (i * i != sum) {
                    cnt++;
                    cnt += sum / i <= b ? 1 : 0;
                }
            }
            System.out.println(cnt);
        }
        sc.close();
    }
}