#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int a[] = {10,20,30,40,50,60,70,80,90,100};
    for(int i =0;i<10;i++){
        printf("%d ",a[i]);
    }

    int low = 0;
    int high = (sizeof(a)/sizeof(a[0]))-1;
    int mid;
    
    int ele = 0;
    printf("\nEnter ele to search: ");
    scanf("%d", &ele);

    bool valid = false;

    while (low<=high){
        mid = (low + high)/2;
        if (ele < a[mid]){
            high = mid-1;
        }
        else if (ele>a[mid]){
            low = mid+1;
        }
        else if(ele == a[mid]){
            valid = true;
            break;
        }
    }

    if (valid == true){
        printf("element found");
    }
    else{
        printf("Element not found");
    }

    return 0;
}