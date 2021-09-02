import java.util.Scanner;

public class swapnumbers {
    public static void main(String[] args) {
        int x,y;
        Scanner in = new Scanner(System.in);
        System.out.println("Enter first number");
        x = in.nextInt();
        System.out.println("Enter second number");
        y = in.nextInt();
        System.out.println("Before Swap");
        System.out.println(x+ " "+ y);
        System.out.println("After Swap");
        int temp = x;
        x = y;
        y = temp;
        System.out.println(x+ " "+ y);
    }
}
