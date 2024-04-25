//촌수계산
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int n;
int a, b; //구해야 하는 촌수
int arr[101][101];
int visit[101] = { 0, };
int count = 0;
int q[101] = { 0, };
int check[101] = { 0, };

void bfs(int v)
{
	visit[v] = 1;
	int front = 0;
	int rear = 0;
	int pop;
	rear++;
	q[0] = v;
	while (front < rear)
	{
		pop = q[front];
		front++;
		for (int i = 1; i<= n; i++)
		{
			if (arr[pop][i] == 1 && visit[i] == 0)
			{
				count++;
				visit[i] = 1;
				check[i] = check[pop] + 1;
				q[rear] = i;
				rear++;
				if (i == b)
				{
					return 0;
				}
			}

		}
		
	}
}
//int dfs(int v)
//{
//	visit[v] = 1;
//	int i;
//	int check = 0;
//	for ( i = 1; i <= n; i++)
//	{
//		if (visit[i] == 0 && arr[v][i] == 1)
//		{
//			count++;
//			if (i == b)
//			{
//				break;
//			}
//			else
//			{
//
//				dfs(i);
//			}
//		}
//	}
//	return count;
//}
int main()
{
	
	scanf("%d", &n);
	scanf("%d %d", &a, &b);
	int m;//부모 자식간의 관계의 수
	scanf("%d", &m);
	int x, y;
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &x, &y);
		arr[x][y] = 1;
		arr[y][x] = 1;
	}
	bfs(a);
	if (check[b]==0)
	{
		printf("-1");
	}
	else
		printf("%d\n", check[b]);
	return 0;
}