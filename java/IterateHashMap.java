import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * Iterate HashMap using while an for
 */
public class IterateHashMap {

    public static void main(String[] args) {
        
        HashMap<String , Integer> map = new HashMap<>();
        map.put("name", 1);
        map.put("n", 2);
        map.put("na", 3);
        map.put("nam", 4);

        Iterator it = map.entrySet().iterator();

        while(it.hasNext()){
            Map.Entry me = (Map.Entry) it.next();
            System.out.println("key is "+me.getKey()+" "+"vlaue is "+me.getValue());
        }
        
        for(Map.Entry me1 : map.entrySet()){
            System.out.println("key is "+me1.getKey()+" value is "+me1.getValue());
        }
    }
}