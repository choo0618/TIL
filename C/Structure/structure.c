#include <stdio.h>
#include <math.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;
struct person
{
	char name[20];
	char phoneNum[20];
	int age;
};
/*
struct circle
{
	double radius;
	struct point* center;
};
*/
typedef struct circle
{
	Point cen;
	double rad;
} Circle;
void OrgSymTrans(Point* ptr)
{
	ptr->xpos = (ptr->xpos) * -1;
	ptr->ypos = (ptr->ypos) * -1;
}
void ShowPostion(Point pos)
{
	printf("%d %d\n", pos.xpos, pos.ypos);
}
void ShowCircleInfo(Circle* ptr)
{
	printf("[%d, %d] \n", (ptr->cen).xpos, (ptr->cen).ypos);
	printf("radius: %g\n", ptr->rad);
}

Point GetCurrentPostion(void)
{
	Point cen;
	printf("Input current pos : ");
	scanf("%d %d", &cen.xpos, &cen.ypos);
	return cen;
}




int main(void) {
	/*
	struct point pos1, pos2;
	double distance;
	fputs("point1.pos : ", stdout);
	scanf_s("%d %d", &pos1.xpos, &pos1.ypos);
	fputs("point2.pos : ", stdout);
	scanf_s("%d %d", &pos2.xpos, &pos2.ypos);

	distance = sqrt((double)((pos1.xpos - pos2.xpos) * (pos1.xpos - pos2.xpos) + (pos1.ypos - pos2.ypos) * (pos1.ypos - pos2.ypos)));
	printf("두점 사이의 거리는 %g 입니다. \n", distance);
	*/
	/*
	struct person man1, man2;
	strcpy(man1.name, "안성준");
	strcpy(man1.phoneNum, "010-1234-5678");
	man1.age = 20;

	printf("이름 입력: "); scanf("%s", man2.name);
	printf("번호 입력: "); scanf("%s", man2.phoneNum);
	printf("나이 입력: "); scanf("%d", &(man2.age));

	printf("이름 : %s\n", man1.name);
	printf("번호 : %s\n", man1.phoneNum);
	printf("나이 : %d\n", man1.age);

	printf("이름 : %s\n", man2.name);
	printf("번호 : %s\n", man2.phoneNum);
	printf("나이 : %d\n", man2.age);
	*/
	/*
	struct point arr[3];
	int i;
	for (i = 0; i < 3; i++)
	{
		printf("점의 좌표 입력: ");
		scanf("%d %d", &arr[i].xpos, &arr[i].ypos);
	};
	for (i = 0; i < 3; i++)
	{
		printf("[%d %d]\n", arr[i].xpos, arr[i].ypos);
	};
	*/
	/*
	struct point arr[3] = { {1,2},{1,3},{1,4} };
	int i;

	for (i = 0; i < 3; i++)
	{
		printf("[%d %d]\n", arr[i].xpos, arr[i].ypos);
	};
	*/
	/*
	struct point pos = { 11,22 };
	struct point* pptr = &pos;

	(*pptr).xpos = 10;
	(*pptr).ypos = 20;

	printf("%d %d \n", (*pptr).xpos, (*pptr).ypos);
	*/
	/*
	struct point cen = { 2,7 };
	double rad = 5.5;
	struct circle ring = { rad,&cen };

	printf("원의 반지름 : %g \n", ring.radius);
	printf("원의 중심 : [%d, %d]\n", (ring.center)->xpos, (ring.center)->ypos);
	*/
	/*
	struct point pos = { 10,20 };
	struct person man = { "조현진","010-1234-5678",28 };

	printf("%p %p\n", &pos, &pos.xpos);
	printf("%p %p\n", &man, man.name);
	*/
	/*
	Point curPos = GetCurrentPostion();
	ShowPostion(curPos);
	*/
	/*
	Point pos = { 7,-5 };
	OrgSymTrans(&pos);
	ShowPostion(pos);
	OrgSymTrans(&pos);
	ShowPostion(pos);
	*/
	/*
	Circle c1 = { {1,2}, 3.5 };
	Circle c2 = { 2,4,3.9 };
	ShowCircleInfo(&c1);
	ShowCircleInfo(&c2);
	*/

	return 0;
}