import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long h = sc.nextLong();
        int m = sc.nextInt();
        sc.close();
        long n = 60 * h + m;
        for (int i = 1; (long) i * i <= n; i++) {
            if (n % i > 0)
                continue;
            if ((i + 1) % 60 == 0 || (n / i + 1) % 60 == 0) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
}