import java.util.ArrayList;
import java.util.Iterator;

public class Arraylist {
    public static void main(String[] args) {
        

        ArrayList list = new ArrayList<>();
        list.add("20");
        list.add("25");
        list.add("234");
        list.add("34");
    
       Iterator it = list.iterator();
       System.out.println("while loop");
       while(it.hasNext()){
           System.out.println(it.next());
       }
      System.out.println("advanced for loop");
      for(Object obj : list){
          System.out.println(obj);
      }
      System.out.println("for loop");
      for(int i=0; i < list.size(); i++){
          System.out.println(list.get(i));
      }  
    }   
}
