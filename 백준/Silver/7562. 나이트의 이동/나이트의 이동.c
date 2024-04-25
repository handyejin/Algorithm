//나이트의 이동
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int sx, sy;
int ex, ey;
int len;
int dx[8] = { 1,2,2,1,-1,-2,-2,-1 };
int dy[8] = { -2,-1,1,2,2,1,-1,-2 };
int visit[310][310] = { 0, };

struct pair
{
	int x;
	int y;
	int cnt;
};
struct pair deque; 
struct pair q[90002] = { 0, };
int bfs(int i, int j)
{
	visit[i][j] = 1;
	memset(visit, 0, sizeof(visit));
	memset(q, 0, sizeof(q));
	
	int xx, yy;
	int front = 0;
	int rear = 0;
	q[front].x = j;
	q[front].y = i;
	q[front].cnt = 0;
	rear++;

	while (front<rear)
	{

		deque.x = q[front].x;
		deque.y = q[front].y;
		if (deque.x == ex && deque.y == ey)
		{
			return q[front].cnt;
		}
		
		for (int k = 0; k < 8; k++)
		{

			xx = deque.x + dx[k];
			yy = deque.y + dy[k];
			if (xx >= 0 && xx < len && yy >= 0 && yy < len)
			{
				if (visit[yy][xx] == 0)
				{
					visit[yy][xx] = 1;
					q[rear].x = xx;
					q[rear].y = yy;
					q[rear].cnt = q[front].cnt + 1;
					rear++;
				}
			}
		}
		front++;
	}

}
int main()
{
	int t;
	scanf("%d", &t);
	int* final = (int*)malloc(sizeof(int) * t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &len);
		scanf("%d %d", &sy, &sx);
		scanf("%d %d", &ey, &ex);
		final[i]=bfs(sy,sx);
	}

	for (int i = 0; i < t; i++)
	{
		printf("%d\n", final[i]);
	}
	return 0;
}
