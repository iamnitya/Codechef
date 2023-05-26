#include <stdio.h>

int main(void) {
	int testcases;
	scanf("%d",&testcases);
	while(testcases--)
    {
    	int a,b,c,d;
    	scanf("%d %d",&a,&b);
    	scanf("%d %d",&c,&d);
    
        if (a<=c && b<=d)
        {
            printf("POSSIBLE\n");
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
	return 0;
}

