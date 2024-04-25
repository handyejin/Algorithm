//카드2
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int q[1000010] = { 0, };
int main()
{
	int n;
	int front = 0;
	int rear = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		q[rear] = i;
		rear++;
	}
	while (front < rear)
	{
		if (front == (rear-1))
		{
			printf("%d\n", q[front]);
			return 0;
		}
		else
		{
			front++;
			q[rear] = q[front];
			front++;
			rear++;
		}
	}


}