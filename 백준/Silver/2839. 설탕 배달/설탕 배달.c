//설탕배달
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	int num;
	int count = 0;
	scanf("%d", &num);

	while (1)
	{
		if (num % 15 == 0 || num % 5 == 0)
		{
			count++;
			num = num - 5;
		}
		else
		{
			count++;
			num = num - 3;
		}
		if (num == 0)
		{
			printf("%d\n", count);
			break;
		}
		if (num < 0)
		{
			printf("-1\n");
			break;
		}
	}
	return 0;

}