/*�����
IP����
25(i):0<=i<=4
ĩIP������ip

*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

char *F_ip[20];//��ʼIP
char *E_ip[20];
int F_i[20];//int��IP
int E_i[20];
int len;

Layout(){
    system("mode con cols=33 lines=18");
    system("title IP������");
    system("color 06");
    system("cls");
}
judge(){
    int i;
    //printf("%c\n",46);//С����
    printf("������ʼIP:");
    gets(F_ip);
    len = strlen(*F_ip);
    //F_i=atoi(F_ip);//�ᱻС����ض�
    for(i=0;i<len;i++){
        //printf("%d",F_ip[i]);
        if(*F_ip[i]>57||(*F_ip[i]!=46&&*F_ip[i]<48))printf("��ЧIP");//���9��С��0��
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
    if(F_i[0]==0)printf("��ЧIP");
    else if(F_i[0]==1&&F_i[1]==7&&F_i[2]==2)printf("��ЧIP");
    else if(len>15)printf("��ЧIP");//�������λ��
    else if(F_i[len-3]==2&&F_i[len-2]==5&&F_i[len-1]==5)printf("��ЧIP");//ĩβΪ255
    else if(F_i[len-4]==46){
        if(F_i[len-3]>3||F_i[len-3]<0)printf("��ЧIP");
        else{
            //if(F_i[len-2]>)
        }
    }//��󲻳���255
    else{
        if(strlen(*F_ip))
        printf("������ĩIP:");
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
