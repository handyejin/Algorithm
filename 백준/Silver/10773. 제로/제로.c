//제로
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int stack[1000010] = { 0, };
int main()
{
	
	int k;
	int num;
	int sum = 0;
	int top = -1;
	scanf("%d", &k);
	while ((k--) > 0)
	{
		scanf("%d", &num);
		
		if (num == 0)
		{
			stack[top] = 0;
			top--;
			
		}
		else
		{
			top++;
			stack[top] = num;
		}


	}
	for (int i = 0; i <= top; i++)
	{
		sum = sum + stack[i];
	}
	printf("%d\n", sum);
	return 0;
}