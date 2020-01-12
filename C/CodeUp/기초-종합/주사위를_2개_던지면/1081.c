#include<stdio.h>

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			printf("%d %d\n", i + 1, j + 1);
		}
	}


	return 0;
}