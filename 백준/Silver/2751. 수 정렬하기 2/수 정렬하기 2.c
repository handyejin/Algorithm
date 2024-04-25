#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int compare(const void* a, const void* b)
{
	long long num1 = *(long long*)a;
	long long num2 = *(long long*)b;

	if (num1 < num2)
	{
		return -1;
	}
	if (num1 > num2)
		return 1;
	return 0;
	


}
int main()
{
	long long N;
	scanf("%lld", &N);
	long long *arr =malloc(sizeof(long long) * N);
	for (long long i = 0; i < N; i++)
	{
		scanf("%lld", &arr[i]);
	}

	qsort(arr, N, sizeof(long long), compare);

	for (int i = 0; i < N; i++)
	{
		printf("%lld\n", arr[i]);
	}
	
	free(arr);

	return 0;
	
	

}