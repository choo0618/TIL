#include<stdio.h>

int main(void) {
	/*
	int opt;
	double num1, num2;
	double result;
	
	printf("1 ����, 2 ����, 3 ����, 4 ������ \n");
	printf("���� ? ");
	scanf_s("%d", &opt);
	printf("�� �Ǽ� �Է�: ");
	scanf_s("%lf %lf", &num1, &num2);

	if (opt==1)
		result = num1 + num2;
	if (opt == 2)
		result = num1 - num2;
	if (opt == 3)
		result = num1 * num2;
	if (opt == 4)
		result = num1 / num2;

	printf("��� : %f \n", result);
	*/
	
	/*
	int num;
	printf("���� �Է� : ");
	scanf_s("%d", &num);
	if (num > 0)
		printf("���");
	else
		printf("����");
	*/

	/*
	int num;
	printf("���� �Է� : ");
	scanf_s("%d", &num);
	if (num > 0)
		printf("���");
	else if (num < 0)
		printf("����");
	else
		printf("0");
	*/

	/*
	int opt;
	double num1, num2;
	double result;

	printf("1 ����, 2 ����, 3 ����, 4 ������ \n");
	printf("���� ? ");
	scanf_s("%d", &opt);
	printf("�� �Ǽ� �Է�: ");
	scanf_s("%lf %lf", &num1, &num2);

	if (opt == 1)
		result = num1 + num2;
	else if (opt == 2)
		result = num1 - num2;
	else if (opt == 3)
		result = num1 * num2;
	else
		result = num1 / num2;

	printf("��� : %f \n", result);
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
	printf("���� �Է� : ");
	scanf_s("%d", &num);
	switch (num) {
	case 1:
		printf("���� 1");
		break;
	case 2:
		printf("���� 2");
		break;
	case 3:
		printf("���� 3");
		break;
	default:
		printf("default");
	}
	*/
	
	/*
	int num;
	printf("���� �Է� : ");
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
	printf("�ٸ� ����");
	goto END;
END:
	return 0;
	*/

	return 0;
}