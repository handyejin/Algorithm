//수찾기
//시간초과-2진트리 탐색
//O(logn)으로 빠르게 탐색 가능
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int search(int*narr,int n, int key)
{
	int left = 0;
	int rignt = n - 1;
	int mid;
	while (rignt>=left)
	{
		mid = (left + rignt) / 2;
		if (narr[mid] == key)
		{
			return mid;
		}

		if (narr[mid] > key) //key값이 배열의 중앙보다 작을때 왼쪽으로
		{
			rignt = mid - 1;
		}
		else if (narr[mid] < key)
		{
			left = mid + 1; //key 값이 배열의 중앙보다 클때 오른쪽으로
		}
	}
	return -1;
}

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
	int n, m;
	scanf("%d", &n);
	int* narr = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &narr[i]);
	}
	qsort(narr, n, sizeof(int), compare);
	scanf("%d", &m);
	int k;

	for (int i = 0; i < m; i++)
	{
		scanf("%d", &k);
		int check = search(narr, n, k);
		if (check == -1)
		{
			printf("0\n");
		}
		else
			printf("1\n");
		check = 0;
			
	}
	
	free(narr);

	return 0;
}
