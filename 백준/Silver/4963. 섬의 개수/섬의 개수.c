//섬의 갯수
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int arr[52][52];
int visit[52][52] = { 0, };
int w, h;
void dfs(int yy, int xx)
{
	visit[yy][xx] = 1;
	for (int i = yy - 1; i <= yy + 1; i++)
	{
		for (int j = xx - 1; j <= xx + 1; j++)
			{
				if (i >= 0 && j >= 0 && i < h && j < w)
					{
						if (arr[i][j] == 1 && visit[i][j] == 0)
						{
							dfs(i, j);
						}
					}
				}
			}

}
int main()
{
	
	while (1)
	{
		memset(visit, 0, sizeof(visit));
		int count = 0;
		scanf("%d %d", &w, &h); //너비, 높이
		if (w == 0 && h == 0)
		{
			break;
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &arr[i][j]);
			}
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (arr[i][j] == 1&& visit[i][j]==0)
				{
					count++;
					dfs(i, j);//높이, 너비
				}
			}
		}
		printf("%d\n", count);

	}
}