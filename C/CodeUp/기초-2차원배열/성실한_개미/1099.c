#include<stdio.h>

int main(void) {
	int i, j, n = 10;
	int arr[10][10] = { 0 }, in, ant[2] = { 1,1 }, Map[10][10] = { 0 };
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			scanf("%d", &in);
			arr[i][j] = in;
			Map[i][j] = in;
		}
	}
	
	while (1)
	{
		Map[ant[0]][ant[1]] = 9;
		if (arr[ant[0]][ant[1]] == 2) break;
		if (arr[ant[0]][ant[1] + 1] == 0 || arr[ant[0]][ant[1] + 1] == 2) ant[1]++;
		else
		{
			ant[0]++;
			if (arr[ant[0]][ant[1]] == 1) break;
		}
	}


	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			printf("%d ", Map[i][j]);
		}
		printf("\n");
	}

	return 0;
}