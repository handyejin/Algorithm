//다이얼
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int main()
{
	char dir[16];
	scanf("%s", dir);

	int size = strlen(dir);
	char alph[26];
	int timearr[26] = { 0, };
	int check = 0;
	int timesum = 0;
	char a = 'A';
	int time = 3;
	for (int i = 0; i < 26; i++)
	{
		alph[i] = a; //알파벳 저장
		a++;

	}
	for (int i = 0; i < 26; i++)
	{
		
		timearr[i] = time;
		check++;
		if (time == 10||time==8)
		{
			if (check == 4)
			{
				time++;
				check = 0;
			}
		}
		else if (check == 3)
		{
			time++;
			check = 0;
		}
		
		

	}

	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < 26; j++)
		{
			if (dir[i] == alph[j])
			{
				timesum = timesum + timearr[j];
				break;
			}

		}
		
	}
	printf("%d\n", timesum);

	return 0;

	

}
