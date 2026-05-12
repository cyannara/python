package work_java;

import java.util.HashMap;
import java.util.Map;

public class MapTest {
    public static void main(String[] args) {
        Map<String, Integer> map =  new HashMap<>(Map.of( "apple", 3, "banana", 5));
        map.put("apple", 3);
        System.out.print(map.get("apple"));
        System.out.println(map.keySet() );
    }
}
