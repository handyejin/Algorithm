//쉬운 계단 수
#define _CRT_SECURE_NO_WARNINGS
#define m 1000000000;
#include<stdio.h>
//int snum(int len)
//{
//	if (len == 1)
//	{
//		return 9;
//	}
//	int num = 1;
//	//num = pow(10, (len - 1));
//	for (int i = 0; i < (len-1); i++)
//	{
//		num *= 10;
//	}
//	int temp;
//	int temp2;
//	int count = 0;
//	for (int i = num; i <num*10; i++)
//	{
//		temp = i;
//		temp2 = temp % 10;
//		temp = temp / 10;
//		while (temp != 0)
//		{
//			if (temp % 10 == temp2 + 1 || temp % 10 == temp2 - 1)
//			{
//				temp2 = temp % 10;
//				temp = temp / 10;
//
//			}
//			else break;
//		}
//		if (temp == 0)
//		{
//			count++;
//		}
//	}
//	return count;
//}
int main()
{
	int dp[101][10] = { 0, };
	int len;
	scanf("%d", &len);
	//c = snum(len);
	for (int i = 1; i <= 9; i++)
	{
		dp[1][i] = 1;
	}
	for (int i = 2; i <=len; i++)
	{
		for (int j = 0; j <= 9; j++)
		{
			if (j == 0)
			{
				dp[i][0] = dp[i - 1][1]%m;
			}
			else if (j == 9)
			{
				dp[i][9] = dp[i - 1][8]%m;
			}
			else
				dp[i][j] =( dp[i - 1][j - 1] + dp[i - 1][j + 1])%m;
		}
	}

	int sum = 0;
	for (int i = 0; i <= 9; i++)
	{
		sum = (sum + dp[len][i])%m;
	}
	
	printf("%d\n",sum);
	return 0;
}