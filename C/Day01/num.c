#include<stdio.h>

int num(void) {
	int num=0;
	int num1 = -4;
	//num = 0; // num ÃÊ±âÈ­
	num += -num1;
	printf("%d\n", ++num);
	printf("%d\n", num);
	return 0;
}