//큐
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int q[100002] = { 0, };
int main()
{

	int n;//명령의 수
	scanf("%d", &n);
	char order[10];
	int front = 0;
	int rear = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%s", order);
		if (strcmp(order, "push") == 0)
		{
			int num;
			scanf("%d", &num);
		
			q[rear] = num;
			rear++;
		}
		else if (strcmp(order, "pop" )== 0)
		{
			if (front==rear)
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", q[front]);
				front++;
			
			}

		}
		else if (strcmp(order, "size") == 0)
		{
			printf("%d\n", rear-front);
		}
		else if (strcmp(order, "empty") == 0)
		{
			if (front==rear)
			{
				printf("1\n");
			}
			else
				printf("0\n");
		}
		else if (strcmp(order, "front") == 0)
		{
			if(front==rear)
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", q[front]);
			}
		}
		else if (strcmp(order, "back") == 0)
		{
			if (front==rear)
			{
				printf("-1\n");
			}
			else
				printf("%d\n", q[rear-1]);
			
		}
	}

}