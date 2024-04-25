#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n; //테스트 케이스의 갯수
	int sum = 0;
	float aver = 0;
	int count = 0;
	scanf("%d", &n);

	int* student = (int*)malloc(sizeof(int) * n);
	int** starr = (int**)malloc(sizeof(int*) * n);
	float* per = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &student[i]);
		starr[i] = (int*)malloc(sizeof(int) * student[i]);
		for (int j = 0; j < student[i]; j++)
		{
			scanf("%d", &starr[i][j]);
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < student[i]; j++)
		{
			sum = sum + starr[i][j];
		}
		aver = (float)sum / student[i];
		for (int j = 0; j < student[i]; j++)
		{
			if (aver < starr[i][j])
			{
				count++;
			}
		}
		per[i] = ((float)count / (float)student[i]) * 100;
		sum = 0;
		aver = 0;
		count = 0;

	}
	for (int i = 0; i < n; i++)
	{
		printf("%.3f%\n", per[i]);
	}


	return 0;

}