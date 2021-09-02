/**
 * numberSeries
 */
public class numberSeries {

    static int by2(int n){
        int sum = 0;
        for(int i =1,j=2; i<=n; i++ ,j*=2){
            System.out.println(j);
            sum += j;

        }

        return sum;
    }

    
    static int by3(int n){
        int sum = 0;
        
        for(int i=1, j= 2; i<=n; i++, j*=3){
            System.out.println(j);
            sum += j;
        }
        return sum;
    }
   
    //(x + 5^2)/1+2 + (x + 25^2)/2+3 + (x + 125^2)/3+4 .....n
    static double geometric(int x,int n){
        double sum = 0;

        for(int i=1,k=5;i<=n;i++, k*= 5){
            sum = sum +(x+Math.pow(k, 2))/(i+i+1);
        }

        return sum;
    }
    public static void main(String[] args) {
        
         System.out.println( geometric(20,3));
        
    }
}