#include<stdio.h>

void RemoveBSN(char str[])
{
	int len = strlen(str);
	str[len - 1] = 0;
}

int main(void) {
	/*
	int ch1, ch2;
	ch1 = getchar();	// 문자 입력
	ch2 = fgetc(stdin);	// 엔터 키 입력

	putchar(ch1);		// 문자 출력
	fputc(ch2, stdout);	// 엔터 키 출력
	*/
	/*
	int ch;
	while (1) {
		ch = getchar();
		if (ch == EOF)
			break;
		putchar(ch);
	};
	*/
	/*
	char* str = "Simple String";
	printf("1. puts test \n");
	puts(str);
	puts("So Simple String");

	printf("1. fputs test \n");
	fputs(str, stdout); printf("\n");
	fputs("So Simple String",stdout);printf("\n");
	*/
	/*
	char str[7];
	int i;
	for (i = 0; i < 3; i++)
	{
		fgets(str, sizeof(str), stdin);
		printf("Read %d: %s \n", i + 1, str);
	};
	*/
	/*
	char str[100];

	printf("문자 입력: ");
	fgets(str, sizeof(str), stdin);
	printf("길이 : %d, 내용 : %s\n", strlen(str), str);
	RemoveBSN(str);
	printf("길이 : %d, 내용 : %s\n", strlen(str), str);
	*/
	/*
	char str1[20] = "First~";
	char str2[20] = "Second";
	char str3[20] = "Simple num: ";
	char str4[20] = "1234567890";

	strcat(str1, str2);
	printf(str1);

	strncat(str3, str4, 7);
	printf(str3);
	*/


	return 0;
}