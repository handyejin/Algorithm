//스택
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int stack[10001] = { 0, };
int main()
{
	int n;//명령어의 수
	scanf("%d", &n);
	int top = -1;
	char order[8];
	for (int i = 0; i < n; i++)
	{
		scanf("%s", order);
		if (strcmp(order, "push") == 0)
		{
			int num;
			scanf("%d", &num);
			top++;
			stack[top] = num;
		}
		else if (strcmp(order, "pop") == 0)
		{
			if (top == -1)
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", stack[top]);
				top--;
			}

		}
		else if (strcmp(order, "size") == 0)
		{
			printf("%d\n", top + 1);
		}
		else if (strcmp(order, "empty") == 0)
		{
			if (top == -1)
			{
				printf("1\n");
			}
			else
				printf("0\n");
		}
		else if (strcmp(order, "top") == 0)
		{
			if (top == -1)
			{
				printf("-1\n");
			}
			else
				printf("%d\n", stack[top]);
		}
	}

}