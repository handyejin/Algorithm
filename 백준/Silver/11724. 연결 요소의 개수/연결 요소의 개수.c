#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int visit[1001] = { 0, };
int n, m;
int arr[1001][1001] = { 0, };
void dfs(int v)
{
	visit[v] = 1;
	for (int i = 1; i <= n; i++)
	{
		if (visit[i] == 0 && arr[v][i] == 1)
		{
			dfs(i);
		}
	}
	
}

int main()
{
	int count = 0;
	int x, y;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &x, &y);
		arr[x][y] = 1;
		arr[y][x] = 1;
	}

	for (int i = 1; i <= n; i++)
	{
		if (visit[i] == 0)
		{
			count++;
			dfs(i);
		}
		
		
	}

	printf("%d\n", count);
}