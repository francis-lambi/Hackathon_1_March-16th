void main() {
  int num1 = 10;
  int num2 = 5;
  
  int result1 = add(num1, num2);
  int result2 = multiply(num1, num2);
  
  print("The result of adding $num1 and $num2 is $result1");
  print("The result of multiplying $num1 and $num2 is $result2");
}

int add(int a, int b) {
  return a + b;
}

int multiply(int a, int b) {
  return a * b;
}
