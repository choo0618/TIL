#include<stdio.h>
typedef struct sbox
{
	int mem1;
	int mem2;
	double mem3;
} SBox;
typedef union ubox
{
	int mem1;
	int mem2;
	double mem3;
} UBox; 
typedef struct dbshort
{
	unsigned short upper;
	unsigned short lower;
}DBShort;
typedef union rdbuf
{
	int iBuf;
	char bBuf[4];
	DBShort sBuf;
}RDBuf;
typedef enum syllable
{
	Do = 1, Re = 2, Mi = 3, Fa = 4, So = 5, La = 6, Ti = 7
} Syllable;

void Sound(Syllable sy)
{
	switch (sy)
	{
	case Do:
		puts("��������"); return;
	case Re:
		puts("��������"); return;
	case Mi:
		puts("�̹̹̹�"); return;
	case Fa:
		puts("��������"); return;
	case So:
		puts("�ּּּ�"); return;
	case La:
		puts("�����"); return;
	case Ti:
		puts("�ýýý�"); return;
	}
	puts("���"); return;
};


int main(void) {
	/*
	SBox sbx;
	UBox ubx;
	printf("%p %p %p \n", &sbx.mem1, &sbx.mem2, &sbx.mem3);
	printf("%p %p %p \n", &ubx.mem1, &ubx.mem2, &ubx.mem3);

	printf("%d %d \n", sizeof(SBox), sizeof(UBox));
	*/
	/*
	RDBuf buf;
	printf("���� �Է�: ");
	scanf("%d", &(buf.iBuf));
	printf("���� 2����Ʈ: %u \n", buf.sBuf.upper);
	printf("���� 2����Ʈ: %u \n", buf.sBuf.lower);
	printf("���� 1����Ʈ �ƽ�Ű�ڵ�: %c \n", buf.bBuf[0]);
	printf("���� 1����Ʈ �ƽ�Ű�ڵ�: %c \n", buf.bBuf[3]);
	*/
	/*
	Syllable tone;
	
	for (tone = Do; tone <= Ti; tone)
		Sound(tone);
	*/

	return 0;
}