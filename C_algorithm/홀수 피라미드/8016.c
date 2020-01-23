#include<stdio.h>

int main(void) {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		long N, f, l;
		scanf("%ld", &N);
		f = 2 * (N-1) * (N-1) + 1;
		l = 2 * N * N - 1;
		printf("#%d %ld %ld\n", t, f, l);
		
	}
	return 0;
}