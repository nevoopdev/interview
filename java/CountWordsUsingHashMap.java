import java.util.HashMap;

public class CountWordsUsingHashMap {

    public static void main(String[] args) {
        String str = "this this is is key key word";
        String[] arr = str.split(" ");
        int count;

        HashMap<String , Integer> map = new HashMap<>();

        for(int i=0; i<arr.length; i++){
            if(map.containsKey(arr[i])){
               count = map.get(arr[i]);
               map.put(arr[i], count+1);
            }else{
                map.put(arr[i], 1);
            }
        }

        System.out.println(map);
    }
    
}
