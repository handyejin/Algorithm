//덱
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int deque[20010] = { 0, };
int main()
{
	int n;
	int rear = 10000;
	int front = 10000;
	scanf("%d", &n);
	char order[50];
	for (int i = 0; i < n; i++)
	{
		memset(order, 0, sizeof(order));
		scanf("%s", order);
		if (strcmp(order, "push_back") == 0)
		{
			int num1;
			scanf("%d", &num1);
			deque[rear] = num1;
			rear++;
		}
		else if (strcmp(order,"push_front") == 0)
		{
			int num2;
			scanf("%d", &num2);
			front--;
			deque[front] = num2;
		}
		else if (strcmp(order, "pop_front") == 0)
		{
			if (front == rear)
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", deque[front]);
				front++;
			}
			
		}
		else if (strcmp(order, "pop_back") == 0)
		{
			if (front == rear)
			{
				printf("-1\n");
			}
			else
			{
				rear--;
				printf("%d\n", deque[rear]);
			}
		}
		else if (strcmp(order, "size") == 0)
		{
			printf("%d\n", rear - front);
		}
		else if (strcmp(order, "empty") == 0)
		{
			if (front == rear)
			{
				printf("1\n");
			}
			else
				printf("0\n");

		}
		else if (strcmp(order, "front") == 0)
		{
			if (front == rear)
			{
				printf("-1\n");
			}
			else
				printf("%d\n",deque[front]);
		}
		else if (strcmp(order, "back") == 0)
		{
			if (front == rear)
				printf("-1\n");
			else
				printf("%d\n", deque[rear - 1]);
		}
	}
	return 0;
}