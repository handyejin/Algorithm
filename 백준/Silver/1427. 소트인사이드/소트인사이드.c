#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int compare(const void* a, const void* b)
{
	long long num1, num2;
	num1 = *(long long*)a;
	num2 = *(long long*)b;
	if (num1 > num2)
		return -1;
	if (num1 < num2)
		return 1;
	else
		return 0;


}
int main()
{

	long long num;
	scanf("%lld", &num);
	long long i = 0;
	long long* arr;
	int dev=0;
	long long count = 0; //자리수 계산
	long long temp = num;;

	while (temp != 0)
	{
		temp = temp / 10;
		count++;
		
	}
	arr = malloc(sizeof(long long) * count);

	for (long long i = 0; i < count; i++)
	{
		dev = num % 10;
		num /= 10;
		arr[i] = dev;
	}
	qsort(arr, count, sizeof(long long), compare);

	for (int i = 0; i < count; i++)
	{
		printf("%lld", arr[i]);
	}

	free(arr);
	return 0;
	
}