/**
 * primenumber
 */
public class primenumber {

    public static void main(String[] args) {
        int n = 100;

        for (int i=2; i<=n;i++){
            boolean isprime = true;
            for(int j=2;j<i;j++){
                if(i%j==0){
                    isprime= false;
                    break;
                }
                
            }
            if(isprime){
                System.out.println(i);
            }
        }
    }
}