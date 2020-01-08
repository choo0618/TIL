#include<stdio.h>

int main(void) {
	/*
	int opt;
	double num1, num2;
	double result;
	
	printf("1 µ¡¼À, 2 »¬¼À, 3 °ö¼À, 4 ³ª´°¼À \n");
	printf("¼±ÅÃ ? ");
	scanf_s("%d", &opt);
	printf("µÎ ½Ç¼ö ÀÔ·Â: ");
	scanf_s("%lf %lf", &num1, &num2);

	if (opt==1)
		result = num1 + num2;
	if (opt == 2)
		result = num1 - num2;
	if (opt == 3)
		result = num1 * num2;
	if (opt == 4)
		result = num1 / num2;

	printf("°á°ú : %f \n", result);
	*/
	
	/*
	int num;
	printf("Á¤¼ö ÀÔ·Â : ");
	scanf_s("%d", &num);
	if (num > 0)
		printf("¾ç¼ö");
	else
		printf("À½¼ö");
	*/

	/*
	int num;
	printf("Á¤¼ö ÀÔ·Â : ");
	scanf_s("%d", &num);
	if (num > 0)
		printf("¾ç¼ö");
	else if (num < 0)
		printf("À½¼ö");
	else
		printf("0");
	*/

	/*
	int opt;
	double num1, num2;
	double result;

	printf("1 µ¡¼À, 2 »¬¼À, 3 °ö¼À, 4 ³ª´°¼À \n");
	printf("¼±ÅÃ ? ");
	scanf_s("%d", &opt);
	printf("µÎ ½Ç¼ö ÀÔ·Â: ");
	scanf_s("%lf %lf", &num1, &num2);

	if (opt == 1)
		result = num1 + num2;
	else if (opt == 2)
		result = num1 - num2;
	else if (opt == 3)
		result = num1 * num2;
	else
		result = num1 / num2;

	printf("°á°ú : %f \n", result);
	*/

	/*
	int total = 0, num = 0;
	while (1) {
		if (total > 10)
			break;
		total += num;
		printf("%d, %d\n",total,num);
		num++;

	};
	*/

	/*
	int total = 0;
	for (int num = 0; num < 10; num++) {
		if (num % 2 == 0)
			continue;
		total += num;
	};
	printf("%d", total);
	*/

	/*
	int num;
	printf("¼ýÀÚ ÀÔ·Â : ");
	scanf_s("%d", &num);
	switch (num) {
	case 1:
		printf("¼ýÀÚ 1");
		break;
	case 2:
		printf("¼ýÀÚ 2");
		break;
	case 3:
		printf("¼ýÀÚ 3");
		break;
	default:
		printf("default");
	}
	*/
	
	/*
	int num;
	printf("¼ýÀÚ ÀÔ·Â : ");
	scanf_s("%d", &num);

	if (num == 1)
		goto ONE;
	else if (num == 2)
		goto TWO;
	else
		goto THREE;

ONE:
	printf("1");
	goto END;
TWO:
	printf("2");
	goto END;
THREE:
	printf("´Ù¸¥ ¼ýÀÚ");
	goto END;
END:
	return 0;
	*/

	return 0;
}