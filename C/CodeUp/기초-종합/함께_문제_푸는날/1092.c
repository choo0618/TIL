#include<stdio.h>

int main(void) {
	int a, b, c, day = 1;
	scanf("%d %d %d", &a, &b, &c);
	while (day % a || day % b || day % c)
	{
		day += 1;
	}
	printf("%d", day);

	return 0;
}