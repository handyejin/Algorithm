#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	int sta = 6;
	int count = 1;

	int i = 2;
	while (i <= n)
	{
		count++;
		for (int j = i; j < i+ sta; j++)
		{
			if (j == n)
			{
				printf("%d", count);
				return 0;
			}
	
		}
		i = i + sta;
		sta = sta + 6;
	}

	printf("%d", count);

	return 0;
}