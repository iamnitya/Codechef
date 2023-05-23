#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d",&t);
    while (t>0)
    {
        t--;
        int a,b;
        scanf("%d %d",&a,&b);
        int count = 0;
        int listofpeople[a];
        
        for (int i = 0; i<a; i++)
        {
            scanf("%d",&listofpeople[i]);
            if (listofpeople[i]>b)
            {
              count++;
            }
            
        }
        printf("%d\n",count);
    }
    
    
    
	return 0;
}
