#include<stdio.h>

int main(void) {
	// 1089
	int a, d, n, r;
	scanf("%d %d %d", &a, &d, &n);
	r = a + d * (n - 1);
	printf("%d", r);
	
	// 1090
	long long int a, r, n;
	scanf("%lld %lld %lld", &a, &r, &n);
	for (int i = 0; i < n - 1; i++)
	{
		a *= r;
	}
	printf("%lld", a);

	// 1091
	long long int a, m, d, n, r;
	scanf("%lld %lld %lld %lld", &a, &m, &d, &n);
	for (int i = 0; i < n - 1; i++)
	{
		a = a * m + d;
	}
	printf("%lld", a);

	return 0;
}