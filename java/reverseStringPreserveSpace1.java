public class reverseStringPreserveSpace1 {
    
    static void reverse(String str){
        
        char[] inputarray = str.toCharArray();
        
        int len = inputarray.length;
        char[] res = new char[len];


        for(int i =0; i<len; i++){
            if(inputarray[i] == ' '){
                res[i] = ' ';
            }           
        }

        int j = len -1;

        for(int i = 0; i< len; i++){
            if(inputarray[i] != ' '){
                if(res[j] == ' '){
                    j--;
                }
                res[j] = inputarray[i];
                j--;
            }
        }

        System.out.println(res);

    }

    public static void main(String[] args) {

        reverse("pooven");
        
    }
}
