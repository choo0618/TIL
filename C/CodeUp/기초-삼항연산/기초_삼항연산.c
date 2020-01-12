#include<stdio.h>

int main(void) {
	// 1063
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a > b ? a : b);

	//1064
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	printf("%d", (a > b ? b : a) > c ? c : (a > b ? b : a) );

	return 0;
}