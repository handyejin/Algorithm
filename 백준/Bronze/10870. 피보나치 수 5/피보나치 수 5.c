#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	int num;
	scanf("%d", &num);

	int pivarr[20];

	if (num == 0)
	{
		printf("0");
		return 0;
	}
	pivarr[0] = 0;
	pivarr[1] = 1;
	for (int i = 2; i <= num; i++)
	{
		pivarr[i] = pivarr[i - 1] + pivarr[i - 2];

	}

	printf("%d\n", pivarr[num]);

	return 0;
}