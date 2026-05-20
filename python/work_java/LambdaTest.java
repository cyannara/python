package javawork;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class LambdaTest {
  public static void main(String[] args) {
    
    List<Integer> squares = IntStream.range(0, 10)
    .map(x -> x * x)     //각 요소를 제곱으로 변환
    .boxed()             //기본형(int)을 객체(Integer)로 변환(박싱)
    .collect(Collectors.toList()); //스트림의 요소를 리스트로 수집
    System.out.println(squares);
  }
}
