 public class Pyramid {

    static void pyramid(int num){
     
      int count = 1;

      for(int i=1;i<=num;i++){
        //   for(int j=num; j>=i; j--){
        //     System.out.print(" ");
        //   }
        //   for(int k =1; k <= i; k++){
        //       System.out.print(i +" ");
        //   }

        for(int j=num; j>=i ; j--){
            System.out.print(" ");
        }
        for(int k = 1; k<=i; k++,count++){
            System.out.print(count+" ");
        }

          System.out.println();
      }
    }
    public static void main(String[] args) {
        System.out.println("yiktyikgytk");
        pyramid(6);
       
    }
}
