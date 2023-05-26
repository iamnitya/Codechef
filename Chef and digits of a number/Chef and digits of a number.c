#include<stdio.h>
#include<string.h>
int main()
{
    int testcase;
    scanf("%d",&testcase);
    while(testcase--)
    {

        char str[100000];
        int x,i;
        scanf("%s",str);
        x=strlen(str);
        int count1=0,count2=0;
        for(i=0;i<x;i++)
        {
            if(str[i]=='1')
                count1++;
            if(str[i]=='0')
                count2++;
        }
        if(count1==1||count2==1)
            printf("Yes\n");
        else
            printf("No\n");

    }
return 0;
}
