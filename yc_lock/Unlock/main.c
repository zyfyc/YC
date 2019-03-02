#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>
int main()
{
    FILE *fp;
    char s[]={"ftype exefile=\"%%1\" %%*"};
    fp=fopen("note.bat","w");
    fprintf(fp,"cd c:\\windows\\system32\n");
    fprintf(fp,"assoc .exe=exefile\n");
    fwrite(&s,strlen(s),1,fp);
    fclose(fp);
    system("start /wait /b note.bat");
    Sleep(2000);
    system("erase /f /q note.bat");
    system("exit");


}
