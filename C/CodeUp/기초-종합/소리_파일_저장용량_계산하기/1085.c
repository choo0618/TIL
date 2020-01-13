#include<stdio.h>

int main(void) {
	double h, b, c, s;
	double r;
	scanf("%lf %lf %lf %lf", &h, &b, &c, &s);
	r = ((h * b * c * s) / 8) / (1024*1024);
	printf("%.1f MB\n", r);


	return 0;
}