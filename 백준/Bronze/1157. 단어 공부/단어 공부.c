#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
char carr[1000001];
int main() 
{
	scanf("%s", carr);
	int size = strlen(carr);
	int countarr[26] = { 0, };
	char c = 'A';
	char alpharr[26];
	for (int i = 0; i < 26; i++)
	{
		alpharr[i] = c;
		c++;
	}
	for (int i = 0; i <= size-1; i++)
	{
		if (carr[i] >= 'a' && carr[i] <= 'z')
		{
			carr[i] = carr[i] - 32;
		}
		for (int j = 0; j < 26; j++)
		{
			if (carr[i] == alpharr[j])
			{
				countarr[j]++;
				break;
			}
		}
		
	}
	int max = countarr[0];
	int t=0;
	for (int i = 1; i < 26; i++)
	{
		if (countarr[i] >= max)
		{
			if (countarr[i] == max)
			{
				alpharr[i] = '?';
			}
			max = countarr[i];
			t = i;
		}
		
	}
	printf("%c\n", alpharr[t]);
	return 0;
}