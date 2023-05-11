import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            sc.nextLine();
            long ans = 0;
            int lmost = m, rmost = 0, umost = n, dmost = 0;
            for (int i = 0; i < n; i++) {
                String row = sc.nextLine();
                for (int j = 0; j < m; j++) {
                    char c = row.charAt(j);
                    if (c == '.')
                        continue;
                    lmost = Math.min(lmost, j);
                    rmost = Math.max(rmost, j);
                    umost = Math.min(umost, i);
                    dmost = Math.max(dmost, i);
                }
            }
            if (lmost < m) {
                ans = (long) (lmost + 1) * (m - rmost) * (umost + 1) * (n - dmost);
            }
            System.out.println(ans);
        }
        sc.close();
    }
}