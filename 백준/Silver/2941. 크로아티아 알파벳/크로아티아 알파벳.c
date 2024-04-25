#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int main()
{
	char cro[8][4] = { "c=","c-","dz=","d-","lj","nj","s=","z=" };
	int count = 0;
	char arr[101] = { 0, };
	scanf("%s", arr);
	char* ptr;
	int size = strlen(arr);
	for (int i = 0; i < 8; i++)
	{
		ptr = strstr(arr, cro[i]);

		while (ptr != NULL)
		{
			count++;
			ptr = strstr(ptr + 1, cro[i]);
		}
	}

	printf("%d\n", size - count);
	return 0;


}