#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int sequence(int n)
{
	int num1;
	int result = 0;
	if (n >= 1 && n <= 99)
	{
		result = n;
	}
	if (n >= 100 && n <=1000)
	{
		int temp1, temp2, temp3;
		int a, b;
		int i = 0;//증가되는 수
		for (int num1 = 100; num1 <= n; num1++)
		{
			temp1 = num1 % 10;//첫째자리수
			temp2 = (num1/ 10) % 10; //둘째자리수
			temp3 = (num1 / 10) / 10; //셋째자리수
			a = (temp1 - temp2);
			b = (temp2 - temp3);
			if (a == b)
			{
				i++;
			}
			result = 99 + i;

		}	
		
	}
	

	return result;
}
int main()
{
	int result;
	int n;//N
	scanf("%d", &n);//1000보다 같거나 작음
	result=sequence(n);

	printf("%d", result);

	return 0;


}