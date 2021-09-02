import java.util.Scanner;

/**
 * reverse string  Without  Reverse
 */
public class reversestringWithoutReverse {

   public static void main(String[] args) {
       System.out.println("enter your string");
       String str;
       Scanner inn = new Scanner(System.in);
       str = inn.nextLine();
       System.out.println(str);
       String[] arr = str.split("");
       
       for(int i= arr.length - 1; i >= 0; i--){
           System.out.print(arr[i] + "");
       }
   }    

    
}

