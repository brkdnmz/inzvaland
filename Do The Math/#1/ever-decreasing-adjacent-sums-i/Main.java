import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int r = sc.nextInt();
        sc.close();
        int[] ans = new int[20];
        for (; l <= r; l++) {
            for (int div = 1; div <= 16 && (l - 1) % div == 0; div++)
                ans[div - 1]++;
        }
        for (int i = 0; i < 16; i++) {
            System.out.print(ans[i] + " ");
        }
    }
}