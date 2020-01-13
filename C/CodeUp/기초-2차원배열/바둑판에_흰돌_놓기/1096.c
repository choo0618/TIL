#include<stdio.h>

int main(void) {
	int i, j, n, arr[19][19] = { 0 }, y, x;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d %d", &y, &x);
		arr[y - 1][x - 1] = 1;
	}
	for (i = 0; i < 19; i++)
	{
		for (j = 0; j < 19; j++)
		{
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}

	return 0;
}