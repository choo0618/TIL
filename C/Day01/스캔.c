#include<stdio.h>
int abc(void) {
	int num3;
	printf("숫자를 입력하세요:");
	scanf_s("%d", &num3);
	printf("%d\n", num3);
	return 0;
}