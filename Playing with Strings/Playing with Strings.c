#include <stdio.h>
#include <string.h>


int main(void) {
    int testcases;
    scanf("%d",&testcases);
    while (testcases>0)
    {
        testcases--;
        int length;
        scanf("%d",&length);
        char a[length+1];
        char b[length+1];
        
        int count01,count02,count11,count12;
        count01 = 0;
        count02 = 0;
        count11 = 0;
        count12 = 0;
        
        scanf("%s",a);
        scanf("%s",b);
        // printf("%s",a);
        // printf("%s",a);
        for (int i = 0; i<length; i++)
        {
            if (a[i]=='0')
            {
                count01++;
            }
            else
            {
                count11++;
            }
        }
        
        for (int i = 0; i<length; i++)
        {
            if (b[i]=='0')
            {
                count02++;
            }
            else
            {
                count12++;
            }
        }
        // printf("%d",count01);
        // printf("%d",count11);
        // printf("%d",count02);
        // printf("%d",count12);
        if (count12==count11 && count02==count01)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
                

    }
	return 0;
}

