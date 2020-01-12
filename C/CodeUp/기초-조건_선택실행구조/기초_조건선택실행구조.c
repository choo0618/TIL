#include<stdio.h>

int main(void) {
	// 1065
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	if (a % 2 == 0)
		printf("%d\n", a);
	if (b % 2 == 0)
		printf("%d\n", b);
	if (c % 2 == 0)
		printf("%d", c);

	// 1066
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	if (a % 2 == 0)
		printf("even\n");
	else
		printf("odd\n");
	if (b % 2 == 0)
		printf("even\n");
	else
		printf("odd\n");
	if (c % 2 == 0)
		printf("even\n");
	else
		printf("odd\n");
	
	// 1067
	int a;
	scanf("%d", &a);
	if (a > 0)
	{
		printf("plus\n");
		if (a % 2 == 0)
			printf("even\n");
		else
			printf("odd\n");
	}
	else
	{
		printf("minus\n");
		if (a % 2 == 0)
			printf("even\n");
		else
			printf("odd\n");
	}
	
	// 1068
	int a;
	scanf("%d", &a);
	if (a >= 90)
		printf("A");
	else if (a >= 70)
		printf("B");
	else if (a >= 40)
		printf("C");
	else
		printf("D");
	
	// 1069
	char a;
	scanf("%c", &a);
	switch(a)
	{
	case 'A':
		printf("best!!!");
		break;
	case 'B':
		printf("good!!");
		break;
	case 'C':
		printf("run!");
		break;
	case 'D':
		printf("slowly~");
		break;
	default:
		printf("what?");
	}

	// 1070
	int a;
	scanf("%d", &a);
	switch (a)
	{
	case 3:
	case 4:
	case 5:
		printf("spring");
		break;
	case 6:
	case 7:
	case 8:
		printf("summer");
		break;
	case 9:
	case 10:
	case 11:
		printf("fall");
		break;
	case 12:
	case 1:
	case 2:
		printf("winter");
		break;
	}


	return 0;
}