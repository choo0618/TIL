#include<stdio.h>

int main(void) {
	// 1038
	long long a, b;
	scanf("%lld %lld", &a, &b);
	printf("%lld", a + b);
	
	// 1039
	long long int a, b;
	scanf("%lld %lld", &a, &b);
	printf("%lld", a + b);
	
	// 1040
	int a;
	scanf("%d", &a);
	printf("%d", -a);
	
	// 1041
	char s;
	scanf("%c", &s);
	printf("%c", s + 1);
	
	// 1042
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a /b);
	
	// 1043
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a % b);
	
	// 1044
	long long a;
	scanf("%lld", &a);
	a++;
	printf("%lld", a);
	
	//1045
	long long int a, b;
	scanf("%lld %lld", &a, &b);

	printf("%lld\n", a + b);
	printf("%lld\n", a - b);
	printf("%lld\n", a * b);
	printf("%d\n", a / b);
	printf("%lld\n", a % b);
	printf("%.2f\n", ((float)a / (float)b));
	
	// 1046
	long long int a, b, c;
	scanf("%lld %lld %lld", &a, &b, &c);
	printf("%lld\n", a + b + c);
	printf("%.1f", (float)(a + b + c) / 3);

	return 0;
}