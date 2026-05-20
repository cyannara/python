package work_java;

import java.util.List;

class Good {
    List<Integer> li = List.of(1,2);
}

public class ClassTest {
    public static void main(String[] args) {
        Good good = new Good();
        System.out.println(good.li.get(0));
    }
}


