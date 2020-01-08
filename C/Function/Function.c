#include<stdio.h>
void ADD(int val);
// 전역변수는 기본으로 0으로 초기화됨, main 함수 return 0 일떄 소멸
int num;	

int Add(int num1, int num2) {
	return num1 + num2;
}

void SimpleFunc(void) {
	//static qustn
	static int num1 = 0;
	int num2 = 0;
	num1++, num2++;
	printf("static: %d, local: %d\n", num1, num2);
}
void Recursive(int num) {
	if (num == 10) {
		printf("%d, num", num);
		return;
	};
	printf("Recurcive call! \n");
	Recursive(num + 1);
	printf("back\n");
}

int Factorial(int n) {
	if (n == 0)
		return 1;
	else
		return n * Factorial(n - 1);
}
int main(void) {
	/*
	int num1, num2;
	num1 = printf("12345\n");
	num2 = printf("I love my home\n");
	printf("%d %d \n", num1, num2);
	*/
	
	/*
	int result1;
	result1 = Add(1, 2);
	printf("%d\n", result1);
	*/

	/*
	printf("num: %d\n", num);
	ADD(3);
	printf("num: %d\n", num);
	num++;
	printf("num: %d\n", num);
	*/

	/*
	int i;
	for (i = 0; i < 3; i++) {
		SimpleFunc();
	};
	*/


	Recursive(0);
	printf("1! = %d\n", Factorial(1));
	printf("2! = %d\n", Factorial(2));
	printf("3! = %d\n", Factorial(3));
	printf("4! = %d\n", Factorial(4));
	printf("5! = %d\n", Factorial(5));

	return 0;
}

void ADD(int val)
{
	num += val;
}