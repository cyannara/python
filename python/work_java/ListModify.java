package work_java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ListModify {
    public static void main(String[] args) {
       // immutableList();
       // fixedSixeList();
        variableSizeList();

    }

    public static void immutableList() {
        List<Integer> list = List.of(1, 3, 5, 7, 9); // ImmutableCollections
        list.set(0, 11); // 변경불가능한 자료구조라서 값 변경 안됨
    }

    public static void fixedSixeList() {
        List<Integer> list = Arrays.asList(1, 3, 5, 7, 9);
        list.remove(0); // 고정길이 배열이라서 get(), set()은 가능하지만 추가 삭제는 안됨.
        System.out.print(list.get(0));
        System.out.print(list.size());
    }

    public static void variableSizeList() {
        List<Integer> list = new ArrayList<>(List.of(1, 3, 5, 7, 9));
        list.set(0, 11);
        list.remove(0);
        System.out.print(list.get(0));
    }

}
