//좌표 정렬하기2
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
struct xysort
{
	int x; //x좌표
	int y; //y좌표
};

int num;
void merge(struct xysort* p, int left, int mid, int rignt)
{
	struct xysort* temp = (struct xysort*)malloc(sizeof(struct xysort) * num);;
	int i = left;
	int j = mid + 1;
	int k = left;
	while (i <= mid && j <= rignt)
	{
		if (p[i].y < p[j].y)
		{
			temp[k++] = p[i++];

		}
		else if (p[i].y > p[j].y)
		{
			temp[k++] = p[j++];
		}

		else if (p[i].y == p[j].y)
		{
			if (p[i].x < p[j].x)
			{
				temp[k++] = p[i++];
			}
			else
			{
				temp[k++] = p[j++];
			}

		}

	}
	while (i <= mid)
	{
		temp[k++] = p[i++];

	}
	while (j <= rignt)
	{
		temp[k++] = p[j++];
	}
	for (int i = left; i <= rignt; i++)
	{
		p[i] = temp[i];
	}

	free(temp);
}

void mergesort(struct xysort* p, int left, int rignt)
{
	int mid;
	if (left < rignt)
	{
		mid = (left + rignt) / 2;
		mergesort(p, left, mid);
		mergesort(p, mid + 1, rignt);
		merge(p, left, mid, rignt);
	}
}

int main()
{
	scanf("%d", &num);
	struct xysort* p = (struct xysort*)malloc(sizeof(struct xysort) * num);
	if (p == NULL)
		return -1;

	for (int i = 0; i < num; i++)
	{
		scanf("%d %d", &p[i].x, &p[i].y);
	}
	mergesort(p, 0, num - 1);
	for (int i = 0; i < num; i++)
	{
		printf("%d %d\n", p[i].x, p[i].y);
	}
	free(p);
	return 0;



}