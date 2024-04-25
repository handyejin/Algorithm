//바이러스
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int arr[101][101];
int visit[101] = { 0, };
int q[101] = { 0, };
int n, m;//n 컴퓨터의 수
			 //m 연결되어있는 컴퓨터 쌍의수
int bfs(int v)
{
	int count = 0;
	int front = 0;
	int rear = 0;
	int pop;
	rear++;
	q[0] = v;
	visit[v] = 1;
	while (front < rear)
	{
		pop = q[front];
		front++;
		for (int i = 1; i <= n; i++)
		{
			if (visit[i] == 0 && arr[pop][i])
			{
				visit[i] = 1;
				q[rear] = i;
				rear++;
				count++;

			}
		}
	}
	return count;
}
int main()
{
	int x, y;
	scanf("%d", &n);
	scanf("%d", &m);
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &x,&y);
		arr[x][y] = 1;
		arr[y][x] = 1;
	}
	printf("%d\n", bfs(1));
	return 0;
}