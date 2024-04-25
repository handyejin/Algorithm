//프린트큐
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int q[10000] = { 0, };
int main()
{
	int t;
	scanf("%d", &t);
	int n, m;
	for (int i = 0; i < t; i++)
	{
		int front = 0;
		int rear = 0;
		int check = 0;
		int count = 1;
		memset(q, 0, sizeof(q));
		scanf("%d %d", &n, &m);

		for (int i = 0; i < n; i++)
		{
			scanf("%d", &q[i]); //우선순위 입력
			rear++;
		}
		while (front < rear)
		{
			check = 0;
			for (int i = front + 1; i < rear; i++)
			{
				if (q[i] >q[front])
				{
					q[rear] = q[front];
					if (front == m)
					{
						m = rear;
					}
					rear++;
					front++;
					check = 1; 
					
					break;
				}
			}

			if (check == 0)
			{
				if (front == m)
				{
					printf("%d\n", count);
					break;
				}
				else
				{
					front++;
					count++;
				}
				

			}
		}
	
	}

	return 0;
	
}