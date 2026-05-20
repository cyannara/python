package work_java;

import java.util.ArrayList;
import java.util.List;

public class ListTest {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(List.of(1, 3, 7, 9));
        list.add(11);
        list.addAll(new ArrayList<>(List.of(11,13)));
        list.remove(0);
        list.set(0,2);
        System.out.print(list.get(0));
        System.out.print(list.size());
    }
}
