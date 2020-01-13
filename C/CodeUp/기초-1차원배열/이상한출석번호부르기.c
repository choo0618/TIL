#include<stdio.h>

int main(void) {
	// 1093
	int n, i, t, arr[23] = {0};

	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d", &t);
		arr[t-1]++;
	}
	for (i = 0; i < 23; i++)
	{
		printf("%d ", arr[i]);
	}
	
	// 1094
	int i, n, t, arr[10000] = {0};
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d", &t);
		arr[i] = t;
	}
	for (i = n - 1; i >= 0; i--)
	{
		printf("%d ", arr[i]);
	}

	// 1095
	int i, n, t, arr[10001] = { 0 };
	scanf("%d", &n);
	for (i = 1; i < n; i++)
	{
		scanf("%d", &t);
		arr[t] = 1;
	}
	for (i = 1;; i++)
	{
		if (arr[i])
		{
			printf("%d", i);
			break;
		}
	}

	return 0;
}