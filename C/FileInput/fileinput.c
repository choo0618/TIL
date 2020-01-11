#include<stdio.h>

typedef struct fren
{
	char name[10];
	char sex;
	int age;
} Friend;


int main(void) {
	/*
	FILE * fp = fopen("data.txt","wt");

	if (fp == NULL) {
		puts("파일 오픈 실패");
		return -1;
	};

	fputc('A', fp);
	fputc('B', fp);
	fputc('C', fp);

	fclose(fp);		// 스트림 형성시 할당된 모드 리소스가 소멸된다.
	*/
	/*
	int ch, i;
	FILE* fp = fopen("data.txt", "rt");
	if (fp == NULL) {
		puts("파일 오픈 실패");
		return -1;
	};
	for (i = 0; i < 3; i++)
	{
		ch = fgetc(fp);
		printf("%c\n", ch);
	};
	fclose(fp);
	*/
	/*
	FILE* fp = fopen("simple.txt", "wt");
	if (fp == NULL) {
		puts("오픈 실패");
		return -1;
	}

	fputc('A', fp);
	fputc('B', fp);
	fputs("My name is Jin\n", fp);
	fputs("My name is Hyeon\n", fp);
	fclose(fp);
	*/
	/*
	char str[30];
	int ch;
	FILE* fp = fopen("simple.txt", "rt");

	if (fp == NULL) {
		puts("오픈 실패");
		return -1;
	}

	ch = fgetc(fp);
	printf("%c\n", ch);
	ch = fgetc(fp);
	printf("%c\n", ch);
	
	fgets(str, sizeof(str), fp);
	printf("%s", str);
	fgets(str, sizeof(str), fp);
	printf("%s", str);

	fclose(fp);
	*/
	/*
	FILE* fp;
	Friend myfren1;
	Friend myfren2;

	fp=fopen("friend.bin","wb");
	printf("이름, 성별, 나이 순으로 입력: ");
	scanf("%s %c %d", myfren1.name, &(myfren1.sex), &(myfren1.age));
	fwrite((void*)&myfren1, sizeof(myfren1), 1, fp);

	fp = fopen("friend.bin", "rb");
	fread((void*)&myfren2, sizeof(myfren2), 1, fp);
	printf("%s %c %d \n", myfren2.name, myfren2.sex, myfren2.age);
	fclose(fp);
	*/


	return 0;
}