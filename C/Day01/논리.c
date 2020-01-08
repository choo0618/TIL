int AndOrNot (void) {
	int num1 = 10;
	int num2 = 12;
	int result1, result2, result3;
	result1 = (num1 == 10 && num2 == 12);
	result2 = (num1 == 9 || num2 == 10);
	result3 = (!num1);
	printf("%d\n", result1);
	printf("%d\n", result2);
	printf("%d\n", result3);
	return 0;
}