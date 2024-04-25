//AC
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
char order[100002];
int q[100002];
int main()
{
	int t;
	
	scanf("%d", &t);
	while(t>0)
	{
		int error_ch = 0;

		int j= 0;
		int n;//배역에 들어있는 수의 개수
		char c;
		int front = 0;
		int rear = -1;
		char* result;
		memset(q, 0, sizeof(q));
		scanf("%s", order);
		scanf("%d", &n);
		getchar();
		scanf("%c", &c);
		
		if (n != 0)
		{
			for (int a = 0; a < n; a++)
			{
				rear++;
				scanf("%d%c", &q[a], &c);

			}
		}
		else if (n == 0)
		{
			scanf("%c", &c);
		}
		result = strchr(order, 'D');
		if (rear == -1&&result!=NULL) //명령어에 D가 있으면
		{
			//getchar();
			error_ch = 1;

		}
		while (order[j] != '\0')
		{
			if (order[j] == 'R')
			{
				int temp = front;
				front = rear;
				rear = temp;
			}

			else if (order[j] == 'D')
			{
				if (q[front + 1] == 0)
				{
					if (q[front] == 0||front<0)
					{
						getchar();
						error_ch = 1;
						break;
					}
					q[front] = 0;
					front--;

					
				}
				else
				{
					if (q[front] == 0||front < 0)
					{
						getchar();
						error_ch = 1;
						break;
					}
					q[front] = 0;
					front++;
				
				}
			}

			j++;
		}
		if (error_ch != 1)
		{
			printf("[");
			if (q[front+1] == '\0'&& q[front]!=0 &&front>=rear)
			{
				for (int k = front; k >= rear; k--)
				{
					if (k == rear)
						printf("%d", q[k]);
					else
						printf("%d,", q[k]);
				}
			
			}
			else if(q[front+1]!='\0'&&q[front]!=0 && front<=rear)
			{
				for (int k = front; k <= rear; k++)
				{
					if (k == rear)
					{
						printf("%d", q[k]);
					}
					else
						printf("%d,", q[k]);
				}
			}
			printf("]\n");
		}
		else if (error_ch == 1)
		{
			printf("error\n");

		}
		t--;
		
	}
	return 0;

}