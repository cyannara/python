package work_java;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SetTest {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>(List.of("apple", "banana", "apple"));
        set.add("banana");
        set.addAll(Set.of("kiwi","berry"));
        System.out.println(set.contains("apple"));
        System.out.print(set.size());
    }
}
