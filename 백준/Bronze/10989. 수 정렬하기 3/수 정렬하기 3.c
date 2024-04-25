#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int numarr[10001] = { 0, };
int main()
{
	int num;
	int now=0;
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
	{
		scanf("%d", &now);
		numarr[now]++;

	}
	int i = 0;


	for (int i = 0; i < 10001; i++)
	{
		while (numarr[i] > 0)
		{
			printf("%d\n", i);
			numarr[i]--;
		}
	}
	return 0;


}