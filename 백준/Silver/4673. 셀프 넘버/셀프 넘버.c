#include<stdio.h>
#include<string.h>

int array[10001];

 int self_num(int n)
{
	int result = n;
	int i = 0;
	if (n >=0 && n <= 9)
	{
		result = n + n;
	}
	else if (n >= 10 && n < 100)
	{
		int temp1,temp2;
		
		temp1 = n % 10; //12면 2
		temp2 = n / 10;//12면 1
		result = temp1 + temp2 + n;

	}
	else if (n >= 100 && n <= 999)
	{
		result = n % 10 + (n / 10) % 10 + (n / 10) / 10 + n;
		/*int temp1, temp2, temp3;
		temp1 = n % 10;
		temp2 = (n / 10) % 10;
		temp3 = (n / 10) / 10;
		result = temp1 + temp2 + temp3 + n;
		result = 1;
		array[i] = result;
		i++;*/

	}
	else if (n >= 1000 && n < 10000)
	{

		result = n % 10 + (n / 10) % 10 + (((n / 10) / 10) % 10) + (((n / 10) / 10) / 10) + n;
		/*int temp1, temp2, temp3, temp4;
		temp1 = n % 10;
		temp2 = (n / 10) % 10;
		temp3 = (((n / 10) / 10) % 10);
		temp4 = (((n / 10) / 10) / 10);
		result = temp1 + temp2 + temp3 + n;
		result = 1;
		array[i] = result;
		i++;*/
	}


	return result;

}

int main()
{
	int a;//self_num의 반환값
	memset(array, 0, sizeof(array));//배열 1로 초기화
	int i = 0;
	for (int i = 0; i < 10001; i++)
	{
		a = self_num(i);
		if (array[a] == 0)
		{
			array[a] = 1;
		}
;

	}
	for (int i = 0; i < 10001; i++)
	{
		if (array[i] != 1)
		{
			printf("%d\n", i);
		}
	}
	

	return 0;

}