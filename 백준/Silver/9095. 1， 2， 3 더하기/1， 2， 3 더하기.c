#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int solve(int n);
int dp[12] = { 1, }; //갯수

int main()
{
	int num;
	scanf("%d", &num);
	int* numarr = (int*)malloc(sizeof(int) * num);
	for (int i= 0; i < num; i++)
	{
		scanf("%d", &numarr[i]);
	}
	
	for (int i = 0; i < num; i++)
	{
		printf("%d\n",solve(numarr[i]));
	}
	free(numarr);
	return 0;

}

int solve(int n)
{

	dp[0] = 1;
	dp[1] = 1;
	dp[2] = dp[0] + dp[1];
	for (int i = 3; i <= n; i++)
	{
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
	}

	return dp[n];

}