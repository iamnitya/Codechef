#include <stdio.h>

int main(void) {
    int testcases;
	scanf("%d",&testcases);
	while(testcases--)
    {
    	int a,b,c,d;
    	scanf("%d %d %d %d",&a,&b,&c,&d);
    	
        if (a+b>=d|| a+c>=d|| b+c>=d)
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

