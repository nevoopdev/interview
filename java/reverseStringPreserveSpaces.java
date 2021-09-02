import java.util.ArrayList;

public class reverseStringPreserveSpaces {
    static void reverse(String str){
        
        String[] str1 = str.split(" ");
        System.out.println(str1[1]);

        ArrayList res = new ArrayList<>();

        for(int i=0;i<str1.length; i++){
           String x = "";

           String[] y = str1[i].split("");
        
           for(int j=y.length - 1; j>=0; j-- ){
             
            x = x +  y[j];
           
           }
           res.add(x);
        }

        System.out.println(res.toString());

    }

    public static void main(String[] args) {
        reverse("hello world");
        reverse("hello world to javaa and javascript");
        
    }
}
