//회의실 배정
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

struct time {
	int x;//시작시간
	int y;//끝나는 시간
};
int num;//회의의 수



void merge(struct time* timearr, int first, int mid, int last)
{
	int i, j, k;

	i = first;
	j = mid + 1;
	k = first;

	struct time* countarr = (struct time*)malloc(sizeof(struct time) * num);
	while (i <= mid && j <= last)
	{
		if (timearr[i].y < timearr[j].y)
		{
			countarr[k++] = timearr[i++];
		}
		else if (timearr[i].y > timearr[j].y)
		{
			countarr[k++] = timearr[j++];
		}
		else if (timearr[i].y == timearr[j].y)
		{
			if (timearr[i].x < timearr[j].x)
			{
				countarr[k++] = timearr[i++];
			}
			else
			{
				countarr[k++] = timearr[j++];
			}

		}
	}

	while (i <= mid)
		countarr[k++] = timearr[i++];
	while (j <= last)
	{
		countarr[k++] = timearr[j++];
	}
	for (int i = first; i <= last; i++)
	{
		timearr[i] = countarr[i];
	}

	free(countarr);

}
void mergesort(struct time* timearr, int first, int last)
{
	int mid;
	if (first < last)
	{
		mid = (first + last) / 2;
		mergesort(timearr, first, mid);
		mergesort(timearr, mid + 1, last);
		merge(timearr, first, mid, last);
	}
}


int main()
{

	int now = 0;
	int temp=0;
	int count = 1;
	scanf("%d", &num);
	struct time* timearr= (struct time*)malloc(sizeof(struct time) * num);
	for (int i = 0; i < num; i++)
	{
		scanf("%d %d", &timearr[i].x, &timearr[i].y);
	}
	mergesort(timearr, 0, num - 1);
	now = timearr[0].y;
	for (int i =temp +1; i < num; i++)
	{
		if (timearr[i].x >= now)
		{
			now = timearr[i].y;
			temp += i;
			count++;

		}
	}


	printf("%d\n", count);

	free(timearr);

	return 0;


}
