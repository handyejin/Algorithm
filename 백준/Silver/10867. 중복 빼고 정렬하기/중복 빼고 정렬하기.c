//중복 빼고 정렬하기
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int compare(const void* a, const void* b)
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
int main()
{
	int n;
	int check = 0;
	int count=0;
	scanf("%d", &n);
	int* arr = (int*)malloc(sizeof(int) * n);
	int* farr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
		for (int j = 0; j < i; j++)
		{
			if (arr[i] == arr[j])
			{
				check = 1;
				break;
			}
		}
		if (check == 0||i==0)
		{
			
			farr[count] = arr[i];
			count++;
		}
		check = 0;

	}
	qsort(farr, count, sizeof(int), compare);
	for (int i = 0; i < count; i++)
	{
		printf("%d ", farr[i]);
	}
	return 0;
}