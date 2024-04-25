//이친수
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
struct fin
{
	long long zero; //0으로 끝나는 수
	long long one;  //1로 끝나는 수
};
int main()
{
	int num;
	struct fin b[92] = { 0, };
	scanf("%d", &num);

	b[1].zero = 0;
	b[1].one = 1;

	
	b[2].zero = 1;
	b[2].one = 0;
	for (int i = 3; i <= num; i++)
	{
		b[i].zero = b[i - 1].one + b[i - 1].zero;
		b[i].one = b[i - 1].zero;
	}

	printf("%lld\n",b[num].zero+b[num].one);
	return 0;
	
}