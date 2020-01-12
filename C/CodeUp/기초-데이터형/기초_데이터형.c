#include<stdio.h>

int main(void) {
	// 1028
	unsigned int n;
	scanf("%u", &n);
	printf("%u", n);
	
	// 1029
	double d;
	scanf("%lf", &d);	// double(long float)형식으로 입력
	printf("%.11lf", d);

	// 1030
	long long int n;
	scanf("%lld", &n);
	printf("%lld", n);

	return 0;
}