#include<stdio.h>

int main(void) {
	int n, i;
	scanf("%d", &n);
	for (i = 1; i < n + 1; i++)
	{
		if (i % 3)printf("%d ", i);
	}

	return 0;
}