#include<stdio.h>

int main(void) {
	// 1059
	int a;
	scanf("%d", &a);
	printf("%d", ~a);
	
	// 1060
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a & b);
	
	//1061
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a | b);

	// 1062
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a ^ b);

	return 0;
}