//괄호
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int sol(char* arr)
{
	int count=0;
	int len = strlen(arr);
	for (int i = 0; i < len; i++)
	{
		if (count == 0)
		{
			if (arr[i] == ')')
			{
				return -1;
			}
		}
		if (arr[i] == '(')
		{
			count++;
		}
		else if (arr[i] == ')')
		{
			count--;
		}

	}

	if (count == 0)
	{
		return 0;
	}
	else if (count != 0)
	{
		return -1;
	}

}
int main()
{
	int num;
	scanf("%d", &num);
	char** arr = (char**)malloc(sizeof(char*) * num);
	for (int i = 0; i < num; i++)
	{
		arr[i] = (char*)malloc(sizeof(char) * 52);
		memset(arr[i], 0, sizeof(char));
	}

	for (int i = 0; i < num; i++)
	{
		scanf("%s", arr[i]);
	}
	for (int i = 0; i < num; i++)
	{
		if (sol(arr[i]) == 0)
		{
			printf("YES\n");
		}
		else
			printf("NO\n");
	}

	for (int i = 0; i < num; i++)
	{
		free(arr[i]);
	}
	free(arr);
	return 0;
}