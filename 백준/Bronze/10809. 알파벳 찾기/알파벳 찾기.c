#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int main() 
{
	int numarr[26];
	memset(numarr, -1, sizeof(numarr));
	int count = 0;
	char word[101];
	scanf("%s", word);
	int size = strlen(word);
	for (int i = 0; i < size; i++)
	{
		for (int j = 'a'; j <= 'z'; j++)
		{
			if (j == word[i])
			{
				if (numarr[j - 97] == -1)
				{
					numarr[j - 97] = i;
				}
			}
			
		}
	}
	for (int i = 0; i < 26; i++)
	{
		printf("%d ", numarr[i]);
	}
	return 0;

}