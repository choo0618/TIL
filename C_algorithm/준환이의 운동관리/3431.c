#include<stdio.h>

int main(void) {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		long L, U, X, R;
		scanf("%ld %ld %ld", &L, &U, &X);
		if (X < L)R = L - X;
		else if (X > U)R = -1;
		else R = 0;
		printf("#%d %ld\n", t, R);

	}

	return 0;
}