#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

struct Body{
	int x; //몸무게  10 ≤ x,y ≤ 200 
	int y; //키
};
int main()
{
	int N;//전체 사람의 수, 2 ≤ N ≤ 50
	scanf("%d", &N);
	int Maxweight ,Maxlength = 0;
	int* grade = malloc(sizeof(int) * N);
	int count = 0;

	struct Body *bodyarr = (struct Body*)malloc(sizeof(struct Body)*N); //구조체 배열

	for (int i = 0; i < N; i++)
	{
		scanf("%d %d", &bodyarr[i].x, &bodyarr[i].y);
	}

	for (int i = 0; i < N; i++)
	{
		Maxweight = bodyarr[i].x;
		Maxlength = bodyarr[i].y;
		for (int j = 0; j < N; j++)
		{
			
			if (bodyarr[j].x > Maxweight && bodyarr[j].y > Maxlength)
			{
				count++;
			}

		}
		grade[i] = count + 1;
		count = 0;
		
	}
	for (int i = 0; i < N; i++)
	{
		printf("%d ", grade[i]);
    }
	free(grade);
	free(bodyarr);
	return 0;
}
