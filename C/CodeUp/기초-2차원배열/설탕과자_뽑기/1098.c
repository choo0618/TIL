#include<stdio.h>

int main(void) {
	int i, j, h, w, n, l, d, x, y, arr[100][100] = { 0 };
	int dir[2][2] = { {1,0},{0,1} };
	scanf("%d %d", &h, &w);
	scanf("%d", &n);
	for (int t = 0; t < n; t++)
	{
		scanf("%d %d %d %d", &l, &d, &x, &y);
		x--;
		y--;
		arr[x][y] = 1;
		for (int ll = 1; ll < l; ll++)
		{
			arr[x + ll * dir[d][1]][y + ll * dir[d][0]] = 1;
		}

	}
	for (i = 0; i < h; i++)
	{
		for (j = 0; j < w; j++)
		{
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}


	return 0;
}