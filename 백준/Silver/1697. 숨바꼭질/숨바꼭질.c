//숨바꼭질
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int x, y;//x는 수빈 y는 동생
int visit[100010] = { 0, };
int qx[3] = { 1,-1,0 };
struct hide
{
	int time;
	int val;
	
};
struct hide q[100010] = { 0, };
void bfs(int a, int b)
{
	int xx;
	int front = -1;
	int rear = -1;
	int pop;
	rear++;
	q[rear].val = a;
	q[rear].time = 0;
	while (front < rear)
	{
		front++;
		pop = q[front].val;
		qx[2] = pop;
		if (pop == b)
		{
			printf("%d\n", q[front].time);
			return;
		}
		for (int i = 0; i < 3; i++)
		{
			xx = pop + qx[i];

			if (xx >= 0 && xx <= 100000)
			{
				if (visit[xx] == 0)
				{
					visit[xx] = 1;
					rear++;
					q[rear].val = xx;
					q[rear].time = q[front].time + 1;
				}
			}
		}
	}
	
}
int main()
{
	
	scanf("%d %d", &x, &y);
	bfs(x, y);
	return 0;

}