#include <stdio.h>

int main(void) {

	int a,b,c,d;
	scanf("%d %d %d %d",&a,&b,&c,&d);
	
    if (a==d|| c==d|| b==d)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

	return 0;
}

