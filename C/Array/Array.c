#include<stdio.h>

int main(void) {
	/*
	int arr[5];
	int sum = 0, i;
	
	arr[0] = 10, arr[1] = 20, arr[2] = 30, arr[3] = 40, arr[4] = 50;

	for (i = 0; i < 5; i++) {
		sum += arr[i];
	};
	printf("%d\n", sum);
	*/

	/*
	int arr1[] = { 1,2,3,4,5 };
	printf("%d\n", sizeof(arr1));
	*/
	/*
	int arr[5] = { 1,2,3,4,5 };
	int sum = 0, i;
	int arrLen;
	arrLen = sizeof(arr) / sizeof(int);
	printf("arr�� ���� : %d\n", arrLen);

	for (i = 0; i < arrLen; i++) {
		sum += arr[i];
	};
	printf("�迭�� �� : %d\n", sum);
	*/
	/*
	char str[7] = "Simple";
	int strLen;
	strLen = sizeof(str) / sizeof(char);
	printf("%c\n", str[4]);
	printf("%d\n", strLen);
	*/
	/*
	char str[50];
	int idx = 0;

	printf("���ڿ� �Է� :");
	scanf_s("%s", str, sizeof(str));
	printf("���� ���� ��� : ");
	while (str[idx] != '\0') {
		printf("%c", str[idx]);
		idx++;
	};
	*/


	return 0;
}