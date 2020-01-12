#include<stdio.h>

int main(void) {
	// 1071
	int n;
reload:
	scanf("%d", &n);
	if (n == 0) goto end;
	printf("%d\n", n);
	goto reload;
end:
	return 0;
	
	// 1072
	int n, m;
	scanf("%d", &n);
reget:
	scanf("%d", &m);
	printf("%d\n", m);
	if (n-- != 1) goto reget;	// reget:으로 이동 n-1
	
	// 1073
	int n;
	while (1)
	{
		scanf("%d", &n);
		if (n == 0) break;
		printf("%d\n", n);
	}
	
	// 1074
	int n;
	scanf("%d", &n);
	while (n != 0)
	{
		printf("%d\n", n);
		n--;
	}
	
	// 1075
	int n;
	scanf("%d", &n);
	while (n != 0)
	{
		n--;
		printf("%d\n", n);
	}
	
	// 1076
	char x,t = 'a';
	scanf("%c", &x);
	do
	{
		printf("%c ", t);
		t++;
	} while (t <= x);

	// 1077
	int n;
	scanf("%d", &n);
	for (int i = 0; i <= n; i++)
	{
		printf("%d\n", i);
	}

	return 0;
}