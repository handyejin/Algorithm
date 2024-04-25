//상수
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int table[3] = { 100,10,1 };
int Max(int a, int b)
{
	if (a >= b)
	{
		return a;
	}
	else if (a < b)
	{
		return b;
	}
}
int change(int num)
{
	int arr[3] = { 0, };
	int i = 0;
	int sum = 0;

	while (num > 0)
	{
		int temp;
		temp = num % 10;
		sum =sum+ temp * table[i];
		i++;
		num = num / 10;
	}
	return sum;

}
int main()
{
	int num1,num2;
	int n1, n2;
	scanf("%d %d", &num1, &num2);
	n1 = change(num1);
	n2 = change(num2);
	printf("%d\n", Max(n1, n2));

	return 0;
}