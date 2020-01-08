#include<stdio.h>

int main(void) {
	/*
	char ch = 9;
	int inum = 1052;
	double dnum = 3.1415;
	
	printf("ch의 크기: %d\n", sizeof(ch));
	printf("inum의 크기: %d\n", sizeof(inum));
	printf("dnum의 크기: %d\n", sizeof(dnum));
	*/

	/*
	char num1 = 1, num2 = 2, result1 = 0;
	short num3 = 300, num4 = 400, result2 = 0;

	printf("num1,num2 : %d, %d \n", sizeof(num1), sizeof(num2));
	printf("num3,num4 : %d, %d \n", sizeof(num3), sizeof(num4));
	printf("char add num1+num2 : %d \n", sizeof(num1+num2));
	printf("short add num3+num4 : %d \n", sizeof(num3 + num4));

	result1 = num1 + num2;
	result2 = num3 + num4;
	printf("sizeof result1,result2: %d, %d \n", sizeof(result1), sizeof(result2));

	*/

	/*
	double rad;
	double area;
	printf("원의 반지름 입력: ");
	scanf_s("%lf", &rad);

	area = rad * rad * 3.1415;
	printf("원의 넓이 : %f \n", area);
	*/

	/*
	char ch = 'A';
	printf("%c\n", ch);
	printf("%d\n", ch);
	*/

	/*
	const int Max = 100;
	printf("%d", Max);
	Max++;
	printf("%d", Max);
	*/

	/*
	int num1 = 3.1234;
	double num2 = 245;

	printf("%d\n", num1);
	printf("%f", num2);
	*/
	
	int num1 = 3, num2 = 4;
	double divResult;
	divResult = (double)num1 / num2;
	printf("결과 : %f\n", divResult);

	return 0;
}