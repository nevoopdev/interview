import java.util.Scanner;

public class SwapNumberWithoutThirdVariable {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x,y;
        x = in.nextInt();
        y = in.nextInt();
        System.out.println("before swapping");
        System.out.println(x+" "+y);
        System.out.println("after swapping");
        x = x + y;
        y = x - y;
        x = x - y;
        System.out.println(x+" "+y);

    }
}
