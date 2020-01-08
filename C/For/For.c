#include<stdio.h>

int main(void) {
	/*
	for (int num = 0; num < 5; num++) {
		printf("hello world, %d\n", num);
	};
	*/
	
	int total = 0;
	int i, num;

	printf("0ºÎÅÍ num±îÁöÀÇ µ¡¼À, num°ªÀº?");
	scanf_s("%d", &num);
	for (i = 0; i <= num; i++) {
		total += i;
	};
	printf("total = %d\n",total);

	return 0;
}