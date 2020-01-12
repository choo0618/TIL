#include<stdio.h>

int main(void) {
	// 1053
	int a;
	scanf("%d", &a);
	printf("%d", !a);
	
	// 1054
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a && b);
	
	// 1055
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a || b);

	// 1056
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a ^ b);
	
	// 1057
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", (!a & !b) || (a & b));

	// 1058
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", !a & !b);

	return 0;
}