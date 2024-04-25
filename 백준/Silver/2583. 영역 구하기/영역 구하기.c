//영역구하기
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int arr[102][102] = { 0, };
int visit[102][102] = { 0, };
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int m, n, k;
struct xy
{
	int x1;
	int y1;
};
struct xy q[10001] = { 0, };
struct xy pop;
int compare(const void* a, const void* b)
{
	int num1, num2;
	num1 = *(int*)a;
	num2 = *(int*)b;

	if (num1 > num2)
		return 1;
	else if (num1 < num2)
		return -1;
	else
		return 0;
}
int bfs(int y, int x)
{
	int cnt = 1;
	visit[y][x] = 1;
	int xx;
	int yy;
	int front = -1;
	int rear = -1;
	rear++;
	q[rear].x1 = x;
	q[rear].y1 = y;
	while (front < rear)
	{
		front++;
		pop.x1 = q[front].x1;
		pop.y1 = q[front].y1;

		for (int i = 0; i < 4; i++)
		{
			xx = pop.x1 + dx[i];
			yy = pop.y1 + dy[i];
			if (yy >= 0 && xx >= 0 && yy < m && xx < n)
			{
				if (arr[yy][xx] == 0 && visit[yy][xx] == 0)
				{
					cnt++;
					visit[yy][xx] = 1;
					rear++;
					q[rear].x1 = xx;
					q[rear].y1 = yy;

				}

			}
		}
	}
	
	
	return cnt;
}
int main()
{
	int count=0;
	int lx, ly ,rx, ry;
	scanf("%d %d %d", &m, &n, &k);
	int* farr = (int*)malloc(sizeof(int) * (k * k));
	


	while (k > 0)
	{
		scanf("%d %d %d %d", &lx, &ly, &rx, &ry);
		for (int i = ly; i < ry; i++)
		{
			for (int j = lx; j < rx; j++)
			{
				arr[i][j] = 1;

			}
		}
		k--;
	}

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (arr[i][j] == 0 && visit[i][j] == 0)
			{
				count++;
				farr[count-1]=bfs(i, j);
			}
		}
	}
	qsort(farr, count,sizeof(int), compare);
	printf("%d\n", count);
	for (int i = 0; i < count; i++)
	{
		printf("%d ", farr[i]);
	}
	
	return 0;
}