import java.util.Scanner;

/**
 * FindPrimeNumber
 */
public class FindPrimeNumber {

    public static void main(String[] args) {
        
        System.out.println("Enter a positive Number");
        Scanner in = new Scanner(System.in);
        int x = in.nextInt();
        int m=x/2;
        boolean b = false;
        
        if(x==0 || x==1){
            System.out.println(x+" is not prie number");
        }else{
            for(int i=2; i<=m; i++){
                if(x%i == 0){
                  b = true;
                  break;
                }
            }
        }
        if(b){
            System.out.println(x+" is not prime number");
        }else{
            System.out.println(x+" is  prime number");

        }

    }
}