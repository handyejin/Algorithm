#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int dp[305] = { 0, };

int maxsum(int a, int b)
{
	if (a >= b)
	{
		return a;
	}
	if (a < b)
	{
		return b;
	}
}
int main()
{
	int stair;
	int count = 0;
	scanf("%d", &stair);

	int *sarr = (int*)malloc(sizeof(int) * stair);
	for (int i = 0; i < stair; i++)
	{
		scanf("%d", &sarr[i]);
	}
	dp[0] = sarr[0];
	dp[1] = sarr[0] + sarr[1];
	dp[2] = maxsum(sarr[0] + sarr[2], sarr[1] + sarr[2]);

	for (int i = 3; i <= stair - 1; i++)
	{
		dp[i] = maxsum(dp[i - 3] + sarr[i - 1] + sarr[i], dp[i - 2] + sarr[i]);
	}

	printf("%d\n", dp[stair - 1]);
	free(sarr);
	return 0;
}


