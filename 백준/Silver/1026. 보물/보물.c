//보물
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int compare1(const void* a, const void* b)
{
	int num1, num2;
	num1 = *(int*)a;
	num2 = *(int*)b;
	if (num1 > num2)
		return 1;

	if (num1 < num2)
		return -1;
	return 0;
}
int compare2(const void* a, const void* b)
{
	int num1, num2;
	num1 = *(int*)a;
	num2 = *(int*)b;
	if (num1 < num2)
		return 1;

	if (num1 >num2)
		return -1;
	return 0;
}

int main()
{
	int n;
	int sum = 0;
	scanf("%d", &n); 
	int* aarr = (int*)malloc(sizeof(int) * n);
	int* barr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d",&aarr[i]);
	}
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &barr[i]);
	}
	qsort(aarr, n, sizeof(int), compare1);
	qsort(barr, n, sizeof(int), compare2);

	for (int i = 0; i < n; i++)
	{
		sum = sum + (aarr[i] * barr[i]);
	}
	printf("%d\n", sum);
	return 0;
}