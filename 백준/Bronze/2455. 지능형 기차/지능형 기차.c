#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
struct train
{
	int out;
	int in;
};
int main()
{
	int maxarr[5];
	struct train st[4] = { 0, };
	for (int i = 0; i <4; i++)
	{
		scanf("%d %d", &st[i].out, &st[i].in);
	}
	
	maxarr[0] = 0;

	for (int i = 1; i <= 4; i++)
	{
		maxarr[i] = maxarr[i - 1] + st[i-1].in - st[i-1].out;

	}
	int max = maxarr[0];
	for (int i = 1; i <= 4; i++)
	{
		if (maxarr[i] >= max)
		{
			max = maxarr[i];
		}
	}
	printf("%d\n", max);

	return 0;

}