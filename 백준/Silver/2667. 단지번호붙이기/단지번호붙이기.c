//단지 번호 붙이기
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
//#include<stdlib.h>
int visit[26][26] = { 0, };
char arr[26][26];
int narr[1000] = { 0, };
int n;
int count = 0;
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
void dfs(int i, int j)
{
	int xx, yy;
	
	visit[i][j] = 1;
	for (int k = 0; k < 4; k++)
	{
		 xx = i + dx[k];
		 yy = j + dy[k];
		 if (xx >= 0 && xx < n && yy >= 0 && yy < n)
		 {
			 if (visit[xx][yy] == 0 && arr[xx][yy] == 1)
			 {
				 arr[xx][yy] = 2;
				 visit[xx][yy] = 0;
				 narr[count] += 1;
				 dfs(xx, yy);
			 }
		 }
	}
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			scanf("%1d", &arr[i][j]);
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (arr[i][j] == 1 && visit[i][j] == 0)
			{
			
				visit[i][j] = 1;
				arr[i][j] = 2;
				count++;
				narr[count]++;
				dfs(i, j);
				
			}
		}
	}
	printf("%d\n", count);
	for (int i = 1; i <= count; i++)
	{
		for (int j = 1; j <= count - 1; j++)
		{
			if (narr[j] >narr[j + 1])
			{
				int temp = narr[j];
				narr[j] = narr[j + 1];
				narr[j + 1] = temp;
			}
		}
	}
	for (int i = 1; i <= count; i++)
	{
		printf("%d\n", narr[i]);
	}
	return 0;

}