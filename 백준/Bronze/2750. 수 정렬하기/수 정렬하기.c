#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int main()
{
	
	int N; //N은 1~1000
		   //N은 수의 개수
	int temp = 0;
	scanf("%d", &N);
	int* arr = malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N - 1; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}

	}
	for (int i = 0; i < N; i++)
	{
		printf("%d\n", arr[i]);
	}

	free(arr);
	return 0;


}