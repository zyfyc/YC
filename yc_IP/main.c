/*待解决
IP规则：
25(i):0<=i<=4
末IP大于首ip

*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

char *F_ip[20];//起始IP
char *E_ip[20];
int F_i[20];//int型IP
int E_i[20];
int len;

Layout(){
    system("mode con cols=33 lines=18");
    system("title IP生成器");
    system("color 06");
    system("cls");
}
judge(){
    int i;
    //printf("%c\n",46);//小数点
    printf("请输入始IP:");
    gets(F_ip);
    len = strlen(*F_ip);
    //F_i=atoi(F_ip);//会被小数点截断
    for(i=0;i<len;i++){
        //printf("%d",F_ip[i]);
        if(*F_ip[i]>57||(*F_ip[i]!=46&&*F_ip[i]<48))printf("无效IP");//大过9或小于0；
        if(*F_ip[i]==46){
            F_i[i] = *F_ip[i];
            //printf("%d",F_i[i]);
        }
        else{
            F_i[i]=*F_ip[i]-48;
            //printf("%d",F_i[i]);
        }
    }
    for(i=0;i<len;i++)
    printf("%d %d\n",F_i[i],len);
    if(F_i[0]==0)printf("无效IP");
    else if(F_i[0]==1&&F_i[1]==7&&F_i[2]==2)printf("无效IP");
    else if(len>15)printf("无效IP");//超过最大位数
    else if(F_i[len-3]==2&&F_i[len-2]==5&&F_i[len-1]==5)printf("无效IP");//末尾为255
    else if(F_i[len-4]==46){
        if(F_i[len-3]>3||F_i[len-3]<0)printf("无效IP");
        else{
            //if(F_i[len-2]>)
        }
    }//最大不超过255
    else{
        if(strlen(*F_ip))
        printf("请输入末IP:");
        gets(E_ip);
    }

}

IP(){
    int i;
    //for()

}

int main()
{

    Layout();
    judge();

    IP();

}
