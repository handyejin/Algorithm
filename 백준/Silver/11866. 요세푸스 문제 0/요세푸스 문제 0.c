//요세푸스 문제0
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int q[1000000] = { 0, };
int main()
{
	int n, k;
	int count = 0;
	scanf("%d %d", &n, &k);
	int rear = 0;
	int front = 0;
	for (int i = 1; i <= n; i++)
	{
		q[rear++] = i;
	}
	printf("<");
	while (front < rear)
	{
		count++;
	
		if(count!=k)
		{
			q[rear] = q[front];
			front++;
			rear++;
		}
		else if (count == k)
		{
			if (front == rear - 1)
			{
				printf("%d>", q[front]);
			}
			else
				printf("%d, ", q[front]);

			front++;
			count = 0;
		}
	}
	return 0;

}