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
		puts("도도도도"); return;
	case Re:
		puts("레레레레"); return;
	case Mi:
		puts("미미미미"); return;
	case Fa:
		puts("파파파파"); return;
	case So:
		puts("솔솔솔솔"); return;
	case La:
		puts("라라라라"); return;
	case Ti:
		puts("시시시시"); return;
	}
	puts("노띵"); return;
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
	printf("정수 입력: ");
	scanf("%d", &(buf.iBuf));
	printf("상위 2바이트: %u \n", buf.sBuf.upper);
	printf("하위 2바이트: %u \n", buf.sBuf.lower);
	printf("상위 1바이트 아스키코드: %c \n", buf.bBuf[0]);
	printf("하위 1바이트 아스키코드: %c \n", buf.bBuf[3]);
	*/
	/*
	Syllable tone;
	
	for (tone = Do; tone <= Ti; tone)
		Sound(tone);
	*/

	return 0;
}