#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	int a, b, c;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	int multi;
	multi = a * b * c;
	int countarr[10] = { 0, };
	int temp = multi;
	int temp2;
	while (temp != 0)
	{
		temp2 = temp % 10;
		countarr[temp2]++;
		temp = temp / 10;
	}

	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", countarr[i]);
	}
	return 0;
}