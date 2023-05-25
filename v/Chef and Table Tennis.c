#include <stdio.h>

int main(void) {

    int testcases;
    scanf("%d",&testcases);
    while(testcases--)
    {
        char a[101];
        scanf("%s",a);

        int chef, opponent;
        chef = 0;
        opponent = 0;
        int i = 0;
        while (a[i]!='\0')
        {
            if (a[i]=='1')
            {
                chef++;
            }
            else
            {
                opponent++;
            }
            i++;
        }
        if (chef>opponent)
        {
            printf("WIN\n");
        }
        else
        {
            printf("LOSE\n");
        }
    }
	return 0;
}

