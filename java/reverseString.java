
//reverse string with String builder and Reverse Function

public class reverseString {
    public static void main(String[] args) {
        String str = "hello world";
        StringBuilder str1 = new StringBuilder();
        str1.append(str);
        System.out.println(str1);
        str1 = str1.reverse();
        System.out.println(str1);
        
    }
}
