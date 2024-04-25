//소수구하기
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
int sol(int num)
{

	int temp;
	temp = sqrt(num);
	for (int i = 2; i <= temp; i++)
	{
		if (num % i == 0) //약수가 아님
		{
			return 0;
		}
	}
	return num;
}
int main()
{
	int num1, num2;
	scanf("%d %d", &num1, &num2);
	for (int i = num1; i <= num2; i++)
	{
		if (i!=1 && i % 2 != 0)
		{
			if (sol(i) == i)
			{
				printf("%d\n",i);
			}
		}
		if (i == 2)
		{
			printf("%d\n", i);
		}
	}


}