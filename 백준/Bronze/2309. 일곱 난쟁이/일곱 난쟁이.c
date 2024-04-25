//일곱난쟁이
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int compare(const void* a, const void* b)
{
	int num1, num2;
	num1 = *(int*)a;
	num2 = *(int*)b;

	if (num1 > num2)
	{
		return 1;
	}
	else if (num1 < num2)
	{
		return -1;
	}
	else
		return 0;

}
int main()
{
	int arr[11] = { 0, };
	int sum = 0;
	int sub;
	int a, b;
	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &arr[i]);
		sum = sum + arr[i];
	}
	sub = sum - 100;
	int i, j;
	
	for ( i = 0; i < 9; i++)
	{
		for ( j = 1; j < 9; j++)
		{
			if (i!=j&&sub==(arr[i]+arr[j]))
			{
				arr[i] = 0;
				arr[j] = 0;
				break;
			}
		}
		if (arr[i] == 0 && arr[j] == 0)
		{
			break;
		}
	}
	qsort(arr, 9, sizeof(int), compare);
	for (int i = 2; i < 9; i++)
	{
		printf("%d\n", arr[i]);
	}

	return 0;




}