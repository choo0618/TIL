#include<stdio.h>

int main(void) {
	// 1047
	int a;
	scanf("%d", &a);
	printf("%d", a << 1);

	// 1048
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a * (1 << b));

	return 0;
}