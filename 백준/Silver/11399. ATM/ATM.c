//ATM순서 정하기
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int coumpare(const void* a, const void* b)
{
	int num1, num2;
	num1 = *(int*)a;
	num2 = *(int*)b;
	if (num1 > num2)
	{
		return 1;
	}
	if (num1 < num2)
	{
		return -1;
	}
	else
		return 0;
}

int main()
{
	int num;
	int sum1 = 0;
	int sum = 0;
	scanf("%d", &num);
	int* atmarr = (int*)malloc(sizeof(int) * num);
	int* sumarr = (int*)malloc(sizeof(int) * num);
	memset(sumarr, 0, sizeof(sumarr));
	for (int i = 0; i < num;i++)
	{
		scanf("%d", &atmarr[i]);
	}
	qsort(atmarr, num, sizeof(int), coumpare);

	for (int i = 0; i < num; i++)
	{
		sum += atmarr[i];
		sumarr[i] = sum;
		sum1 += sumarr[i];

	}

	printf("%d", sum1);
	free(atmarr);

	return 0;

}