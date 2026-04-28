package work_java;

import java.util.Scanner;

public class InputTest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("숫자 2개 입력");
        String[] str = input.nextLine().split(" ");
        System.out.println(str[0]);

        System.out.println("숫자를 입력하세요.");
        int number = input.nextInt();
        System.out.println(number);
    }
}
