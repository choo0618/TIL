#include<stdio.h>

int main(void) {
	// 1010
	int n;
	scanf("%d", &n);
	printf("%d", n);

	// 1011
	char x;
	scanf("%c", &x);
	printf("%c", x);
	
	// 1012
	float x;
	scanf("%f", &x);
	printf("%f", x);
	
	// 1013
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d %d", a, b);
	
	// 1014
	char x, y;
	scanf("%c %c", &x, &y);
	printf("%c %c", x, y);
	
	// 1015
	float x;
	scanf("%f", &x);
	printf("%.2f", x);	// 소수 셋째자리 반올림
	
	// 1017
	int x;
	scanf("%d", &x);
	printf("%d %d %d", x, x, x);
	
	// 1018
	int h, m;
	scanf("%d:%d", &h, &m);
	printf("%d:%d", h, m);
	
	// 1019
	int y, m, d;
	scanf("%d %d %d", &y, &m, &d);
	printf("%04d.%02d.%02d", y, m, d);
	
	// 1020
	int a, b;
	scanf("%d-%d", &a, &b);
	printf("%06d%07d", a, b);
	
	// 1021
	char data[51] = "";
	scanf("%s", data);
	printf("%s", data);
	
	// 1022
	char data[2001];
	fgets(data, 2000, stdin);
	printf("%s", data);
	
	// 1023
	int a, b;
	scanf("%d.%d", &a, &b);
	printf("%d\n%d", a, b);
	
	// 1024
	char data[30];
	scanf("%s", data);
	for (int i = 0; data[i] != '\0'; i++)
	{
		printf("\'%c\'\n", data[i]);
	};
	
	// 1025
	int a, b, c, d, e;
	scanf("%1d%1d%1d%1d%1d", &a, &b, &c, &d, &e);
	printf("[%d]\n", a * 10000);
	printf("[%d]\n", b * 1000);
	printf("[%d]\n", c * 100);
	printf("[%d]\n", d * 10);
	printf("[%d]", e * 1);
	
	// 1026
	int h, m, s;
	scanf("%d:%d:%d", &h, &m, &s);
	printf("%d", m);
	
	// 1027
	int y, m, d;
	scanf("%d.%d.%d", &y, &m, &d);
	printf("%02d.%02d.%04d", d, m, y);

	return 0;
}