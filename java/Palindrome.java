import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter number or string");
        String str = in.nextLine();
        StringBuilder str1 = new StringBuilder();
        str1.append(str);
        str1 = str1.reverse();
        String str2 = str1.toString();

        System.out.println(str1);

        if(str.equals(str2)){
          System.out.println(str + " is palindrome");
        }else{
          System.out.println(str + " is  not palindrome");
 
        }
        
    }
    
}
