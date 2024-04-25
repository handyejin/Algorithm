//토마토
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define Max 101
int arr[Max][Max][Max];
int visit[Max][Max][Max] = { 0, };
int n, m, h;//세로 가로 높이
int rear = -1;
int front = -1;
int dh[6] = { 1,-1,0,0,0,0 };
int dy[6] = { 0,0,-1,1,0,0 };
int dx[6] = { 0,0,0,0,1,-1 };

struct tomato
{
	int x;
	int y;
	int height;
	int day;
};
struct tomato q[Max * Max * Max] = { 0, };
struct tomato deque;
int bfs()
{
	int xx;
	int yy;
	int hh;
	while (front < rear)
	{
		front++;
		deque.x = q[front].x;
		deque.y = q[front].y;
		deque.height = q[front].height;

		for (int i = 0; i < 6; i++)
		{
			hh = deque.height + dh[i];
			xx = deque.x + dx[i];
			yy = deque.y + dy[i];
			if (hh >= 0 && hh < h && xx >= 0 && xx < m && yy >= 0 && yy < n)
			{
				if (arr[hh][yy][xx] == 0 && visit[hh][yy][xx] == 0)
				{
					arr[hh][yy][xx] = 1;
					visit[hh][yy][xx] = 1;
					rear++;
					q[rear].x = xx;
					q[rear].y = yy;
					q[rear].height = hh;
					q[rear].day = q[front].day + 1;

				}

			}
		}
	}
	return q[rear].day;
}
int main()
{
	int k = 0;
	int date = 0;
	scanf("%d %d %d", &m, &n, &h);

	for (int k = 0; k < h; k++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%d", & arr[k][i][j]);
				if (arr[k][i][j] == 1)
				{
					rear++;
					visit[k][i][j] = 1;
					q[rear].height = k;
					q[rear].y = i;
					q[rear].x = j;
					q[rear].day = 0;

				}
			}
		}
	}
	date = bfs();
	for (int k = 0; k < h; k++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (arr[k][i][j] == 0)
				{
					date = -1;
					break;
				}
			}
		}
	}
	printf("%d\n", date);
	return 0;
}