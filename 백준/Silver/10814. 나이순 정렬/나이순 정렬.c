//나이순 정렬
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
struct club {
	int age;
	char name[101];
	int seq;

};
int agecompare(const void* a, const void* b)
{
	struct club* num1;
	struct club* num2;
	num1 = (struct club*)a;
	num2 = (struct club*)b;
	if (num1->age < num2->age)
	{
		return -1;
	}
	if (num1->age > num2->age)
	{
		return 1;
	}
	else
		return 0;

}
int seqcompare(const void* a, const void* b)
{
	struct club* num1 = (struct club*)a;
	struct club* num2 = (struct club*)b;
	if (num1->seq > num2->seq)
	{
		return 1;
	}
	if (num2->seq < num2->seq)
	{
		return -1;
	}
	else
		return 0;


}
int compare(const void* a, const void* b)
{
	int check;
	check = agecompare(a, b);
	if (check != 0)
	{
		return check;
	}
	else
		return seqcompare(a, b);

}



int main()
{
	int num;
	scanf("%d", &num);
	struct club* c = (struct club*)malloc(sizeof(struct club) * num);

	for (int i = 0; i < num; i++)
	{
		scanf("%d %s", &c[i].age,&c[i].name);
		c[i].seq = i;
	}
	
	qsort(c, num, sizeof(struct club), compare);
	for (int i = 0; i < num; i++)
	{
		printf("%d %s\n", c[i].age, c[i].name);
	}


	return 0;
}