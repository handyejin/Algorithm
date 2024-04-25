#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int main()
{
	long long num; //num은 10000보다 작거나 같은수
	long long shomnum = 666;
	char buffer[10];
	char* ptr;
	long long count = 0;
	scanf("%lld", &num); //num번째 영화 입력
	for (shomnum = 666;; shomnum++)
	{
		sprintf(buffer, "%d", shomnum);
		ptr = strstr(buffer, "666");
		if (ptr != NULL)
		{
			count++;
			if (count == num)
			{
				printf("%d", shomnum);
				return 0;
			}
		}

	}
}