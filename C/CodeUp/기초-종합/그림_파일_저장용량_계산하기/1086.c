#include<stdio.h>

int main(void) {

	double r, g, b;
	double R;
	scanf("%lf %lf %lf", &r, &g, &b);
	R = ((r * g * b) / 8) / (1024 * 1024);
	printf("%.2lf MB", R);



	return 0;
}