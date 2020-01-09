#include<stdio.h>

void Swap1(int* p1, int* p2)
{
	int* temp = *p1;
	p1 = p2;
	p2 = temp;
}
void Swap2(int** p1, int** p2)
{
	int* temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}


int main(void) {
	/*
	int arrOneDim[10];
	int arrTwoDim[5][5];
	int arrThreeDim[3][3][3];

	printf("%d\n", sizeof(arrOneDim));
	*/
	/*
	int villa[4][2];
	int popu, i, j;

	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d층 %d호 인구수 입력 : ", i + 1, j + 1);
			scanf_s("%d", &villa[i][j]);
		}
	};

	for (i = 0; i < 4; i++)
	{
		popu = 0;
		popu += villa[i][0];
		popu += villa[i][1];
		printf("%d층 인구수: %d\n", i + 1, popu);
	};
	*/
	/*
	double num = 3.14;
	double* ptr = &num;
	double** dptr = &ptr;
	double* ptr2 = 0;

	printf("%9p %9p \n", ptr, *dptr);
	printf("%9g %9g \n", num, **dptr);
	ptr2 = *dptr;	// ptr2 = ptr과 같은 문장
	*ptr2 = 10.99;
	printf("%9g %9g \n", num, **dptr);
	*/
	/*
	int num1 = 10, num2 = 20;
	int* ptr1 = &num1, * ptr2 = &num2;
	printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);

	Swap1(ptr1, ptr2);

	printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);
	*/
	/*
	int num1 = 10, num2 = 20;
	int* ptr1 = &num1, * ptr2 = &num2;
	printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);

	Swap2(&ptr1, &ptr2);

	printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);
	*/
	/*
	int num1 = 10, num2 = 20, num3 = 30;
	int* ptr1 = &num1;
	int* ptr2 = &num2;
	int* ptr3 = &num3;

	int* ptrArr[3] = { ptr1, ptr2, ptr3 };
	int** dptr = ptrArr;

	printf("%d %d %d \n", *(ptrArr[0]), *(ptrArr[1]), *(ptrArr[2]));
	printf("%d %d %d \n", *(dptr[0]), *(dptr[1]), *(dptr[2]));
	*/
	/*
	int arr2d[3][3];

	printf("%d \n", arr2d);
	printf("%d \n", arr2d[0]);
	printf("%d \n", &arr2d[0][0]);

	printf("sizeof(arr2d) : %d \n", sizeof(arr2d));
	printf("sizeof(arr2d[0]) : %d \n", sizeof(arr2d[0]));
	printf("sizeof(arr2d[1]) : %d \n", sizeof(arr2d[1]));
	printf("sizeof(arr2d[2]) : %d \n", sizeof(arr2d[2]));
	*/
	/*
	int arr1[2][2] = { {1,2},{3,4} };
	int arr2[3][2] = { {1,2},{3,4},{5,6} };
	int arr3[4][2] = { {1,2},{3,4},{5,6},{7,8} };

	int(*ptr)[2];
	int i;
	ptr = arr1;
	printf("arr1\n");
	for (i = 0; i < 2; i++) {
		printf("%d %d \n", ptr[i][0], ptr[i][1]);
	};
	ptr = arr2;
	printf("arr2\n");
	for (i = 0; i < 3; i++) {
		printf("%d %d \n", ptr[i][0], ptr[i][1]);
	};
	ptr = arr3;
	printf("arr3\n");
	for (i = 0; i < 4; i++) {
		printf("%d %d \n", ptr[i][0], ptr[i][1]);
	};
	*/

	return 0;
}
