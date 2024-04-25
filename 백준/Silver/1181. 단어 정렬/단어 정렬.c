#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char strarr[20001][51];

int lencompare(const void* a, const void* b)
{
	int num1 = strlen((char*)a);
	int num2= strlen((char*)b);

	if (num1 > num2)
	{
		return 1;
	}
	if (num1 < num2)
	{
		return -1;
	}
	
	return 0;
}
int abccompare(const void* a, const void* b)
{
	return strcmp((char*)a, (char*)b);
}
int compare(const void* a, const void* b)
{
	int check;
	check = lencompare(a, b);
	if (check != 0)
	{
		return check;
	}
	else
		return abccompare(a, b);
}
int main()
{
	int num;
	scanf("%d", &num);//1<=num<=20000
	char temp[51];

	
	for (int i = 0; i < num; i++)
	{
		scanf("%s", strarr[i]);
	}


	qsort((void**)strarr, num,sizeof(strarr[0]) , compare);
	for (int i = 0; i < num; i++)
	{
		if (strcmp(strarr[i], strarr[i + 1]) == 0)
		{
			continue;
		}
		printf("%s\n", strarr[i]);
	}

	return 0;
}