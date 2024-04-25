#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n;//동전의 개수
	int k;//만들어야되는 값
	int count = 0;
	int sum = 0;

	scanf("%d %d", &n, &k);
	int* coinarr = malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &coinarr[i]);
	}
	for (int i = n-1; i >=0 ; i--)
	{
		while (sum + coinarr[i] <= k)
		{
			sum = sum + coinarr[i];
			count++;
	
		}
		if (sum == k)
		{
			break;
		}
	}

	printf("%d\n", count);

	free(coinarr);
	return 0;


}