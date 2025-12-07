#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int a[] = {10,20,30,40,50,60,70,80,90,100};
    for(int i =0;i<10;i++){
        printf("%d ",a[i]);
    }

    int ele = 0;
    printf("\nEnter element to find:");
    scanf("%d", &ele);

    bool valid = false;
    for (int i = 0; i<10; i++){
        if(a[i]==ele){
            valid = true;
            break;
        }
    }
    if(valid == true){
        printf("Ele found");
    }
    else{
        printf("Ele not found in list");
    }
    return 0;
}