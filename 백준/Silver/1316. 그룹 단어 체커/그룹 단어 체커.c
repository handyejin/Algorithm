//그룹 단어 체커
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int group_word(char* str)
{
	int size;
	size = strlen(str);
	for (int i = 0; i < size; i++)
	{
		for (int j = i + 1; j < size; j++)
		{
			if (str[i] != str[j])
			{
				for (int k = j + 1; k < size; k++)
				{
					if (str[i] == str[k])
					{
						return -1;
					}
				}

			}
		}
	}

	return 0;

}
int main()
{
	char garr[101][101];
	int n;
	int counts = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", garr[i]);
		if (group_word(garr[i]) == 0)
		{
			counts++;
		}
	}
	printf("%d\n", counts);
	return 0;

}