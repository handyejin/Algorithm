//블랙잭
//sum1의 값들을 배열로 만들 필요 없음!
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int  black_jack(int array[], int count,int M)
{
	int sum1;
	int* sum;
	int MAx = 0;;
	int r= 0;
	for (int i = 0; i < count; i++)
	{
		for(int j = i + 1; j < count; j++)
		{
			for (int k = j + 1; k < count; k++)
			{
				sum1 = array[i] + array[j] + array[k];
				if (sum1 <= M&& MAx<sum1)
				{
					MAx = sum1;
				}
			}
		}
		
	}


	return MAx;
}


int main()
{
	int* array;

	int N, M; //N은 카드의 개수
			 //M은 합의 최대수
	int Max;
	
	int near = 0; //최대한 가까운수;
	scanf("%d %d", &N, &M);
	array =(int*) malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &array[i]);
	}
	Max = black_jack(array, N, M);
	printf("%d", Max);	
		
	
	

	free(array);

	return 0;
}


