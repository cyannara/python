package work_java;
import java.util.List;

public class Listslice {
    public static void main(String[] args) {
        List<Integer> a = List.of(1, 2, 3, 4, 5);
        List<Integer> b = a.subList(2, 4);
        System.out.print(b);
    }
}