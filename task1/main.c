#include <stdio.h>
#include<math.h>
int main()
{
    double temp,buChang = 0.0001;
    double yStart = 1,y = 1;
    // scanf("%lf %lf",&yStart,&buChang);
    temp = buChang;
    printf("x          y\n");
    while(y > 0.0001||y < -0.0001)
    {
        y = yStart*exp(-buChang);
        printf("%lf     %lf\n",buChang,y);
        buChang += temp;
    }
return 0;

}