#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void piv(long long arr[],int n);
int main()
{

	int n;
	scanf("%d", &n);
	long long* arr = (long long*)malloc(sizeof(long long) * (n + 1));
	for (int i = 0; i <= n; i++)
	{
		piv(arr,i);
	}
	printf("%lld",arr[n]);

	free(arr);


	 return 0;
}
void piv(long long arr[],int n)
{

	if (n == 0)
	{
		arr[n] = 0;
	}
	else if (n == 1)
	{
		arr[n] = 1;
	}
	else
	{
		arr[n] = arr[n - 1] + arr[n - 2];
	}

	return 0;


}