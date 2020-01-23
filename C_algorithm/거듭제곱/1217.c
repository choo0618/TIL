#include<stdio.h>

int DFS(int r,int x, int y)
{
	if (y == 0)return r;
	if (y)DFS(r * x, x, y - 1);
};
int main(void) {
	for (int i = 0; i < 10; i++)
	{
		int T;
		scanf("%d", &T);
		int N, M;
		scanf("%d %d", &N, &M);
		printf("#%d %d\n", T, DFS(1, N, M));
	}

	return 0;
}