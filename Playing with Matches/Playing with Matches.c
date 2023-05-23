#include <stdio.h>
#include <string.h>


int main(void) {
    int testcases;
    scanf("%d",&testcases);
    while (testcases>0)
    {
        testcases--;
        int a,b,s,sum;
        scanf("%d %d",&a,&b);
        sum = a+b;
        s = 0;
        char snum[10000001];
        sprintf(snum, "%d", sum);
        int len = strlen(snum);
        for (int i =0; i<len;i++)
        {
            switch(snum[i])
            {
                case '0':
                    s+=6;
                    break;
                    
                case '1':
                    s+=2;
                    break;
                    
                case '2':
                    s+=5;
                    break;
                    
                case '3':
                    s+=5;
                    break
                    ;
                case '4':
                    s+=4;
                    break;
                    
                case '5':
                    s+=5;
                    break;
                    
                case '6':
                    s+=6;
                    break;
                    
                case '7':
                    s+=3;
                    break;
                    
                case '8':
                    s+=7;
                    break;
                    
                case '9':
                    s+=6;
                    break;
                    
                default:
                    printf("");
            }
        }
        printf("%d\n",s);

    }
	return 0;
}

