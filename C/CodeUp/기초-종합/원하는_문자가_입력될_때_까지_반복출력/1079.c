#include<stdio.h>

int main(void) {
	char s;
	do
	{
		scanf("%c ", &s);
		printf("%c\n", s);
	} while (s != 'q');

	return 0;
}