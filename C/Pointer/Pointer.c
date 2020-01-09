#include<stdio.h>

void fct(int* ptr) {
	*ptr += 1;
}
void SimpleFunc(int* param)
{
	printf("%d %d %d\n", param[0], param[1], param[2]);
}
void ArrFunc(int* param, int len)
{
	for (int i = 0; i < len; i++) {
		printf("%d \n", param[i]);
	}
}
void Swap(int x, int y)
{
	int tmp = x;
	x = y;
	y = tmp;
	printf("x y : %d %d\n", x, y);
}
void Swap1(int* ptr1, int* ptr2)
{
	int tmp = *ptr1;
	*ptr1 = *ptr2;
	*ptr2 = tmp;
}

int main(void) {
	/*
	int num = 10;
	int *ptr;
	ptr = &num;

	double num1 = 3.15;
	double *ptr1;
	ptr1 = &num1;
	
	printf("int형 :%d\n", ptr);
	printf("double형 : %d\n", ptr1);
	*/
	/*
	int num = 10;
	int *ptr = &num;
	printf("%d\n", *ptr);
	*ptr = 20;
	printf("%d\n", *ptr);
	printf("%d\n", num);
	*/
	/*
	int num = 10;
	int* ptr = &num;

	double num1 = 3.15;
	double* ptr1 = &num1;

	*ptr = 30;
	*ptr1 = 1.2;
	*/
	/*
	int arr[3] = {10, 20, 30};
	int* ptr = &arr[0];

	printf("%d %d\n", ptr[0], arr[0]);
	printf("%d %d\n", ptr[1], arr[1]);
	printf("%d %d\n", ptr[2], arr[2]);
	printf("%d %d\n", *ptr, *arr);
	*/
	/*
	int arr[3];
	int* ptr = arr;
	*ptr = 10;
	ptr++;
	*ptr = 20;
	ptr++;
	*ptr = 30;
	ptr -= 2;

	printf("%d %d\n", *ptr, arr[0]);
	printf("%d %d\n", *ptr, arr[1]);
	printf("%d %d\n", *ptr, arr[2]);
	*/
	/*
	int arr[3] = { 11,12,13 };
	int* ptr = arr;

	printf("%d %d %d \n", *ptr, *(ptr + 1), *(ptr + 2));
	*/
	/*
	char str1[] = "My String";
	char* str2 = "Your String";

	str1 = "불가능";
	str2 = "가능";
	*/
	/*
	int num1 = 10, num2 = 20, num3 = 30;
	int* arr[3] = { &num1,&num2,&num3 };

	printf("%d\n", *arr[0]);
	printf("%d\n", *arr[1]);
	printf("%d\n", *arr[2]);
	*/
	/*
	char* strArr[3] = { "Simple","string","Array" };

	printf("%s\n", strArr[0]);
	printf("%s\n", strArr[1]);
	printf("%s\n", strArr[2]);
	*/
	/*
	int age = 20;
	fct(&age);
	printf("%d\n", age);
	*/
	/*
	int arr[3] = { 1,2,3 };
	SimpleFunc(arr);
	*/
	/*
	int arr[3] = { 1,2,3 };
	ArrFunc(arr, sizeof(arr) / sizeof(int));
	*/
	/*
	int num1 = 10;
	int num2 = 20;
	printf("num1 num2 : %d %d\n", num1, num2);
	Swap(num1, num2);
	printf("num1 num2 : %d %d\n", num1, num2);
	*/
	/*
	int num1 = 10;
	int num2 = 20;
	printf("num1 num2 : %d %d\n", num1, num2);
	Swap1(&num1, &num2);
	printf("num1 num2 : %d %d\n", num1, num2);
	*/
	/*
	int num = 20;
	const int* ptr = &num;
	// *ptr = 30;
	num = 40;
	printf("%d\n", num);
	*/

	return 0;
}