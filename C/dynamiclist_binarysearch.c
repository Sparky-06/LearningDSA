#include <stdio.h>

void arrayip(int lst[],int n);
void printlist(int lst[], int num1);
void sorting(int lst[], int num1);
void binary_search(int lst[], int num1);

int main(void)
{   
    int num1;
    printf("Enter elements you want in list:");
    scanf("%d",&num1);
    
    int lst[num1];
    arrayip(lst,num1);  // For taking input in array

    printf("Orignal list: ");
    printlist(lst,num1);  // For output list

    // __SORTING__
    sorting(lst,num1);


    printf("Final list:\n");
    printlist(lst,num1);

    binary_search(lst,num1);

    return 0;

}

void arrayip(int lst[],int n){

    for(int i = 0; i<n;i++){
        printf("Enter ele in list: ");
        scanf("%d", &lst[i]);
    }
}


void printlist(int lst[], int num1){
    for(int i =0; i < num1 ; i++){
        printf("%d ",lst[i]);
    }
    printf("\n");
}



void sorting(int lst[], int num1){
    for(int j = 0; j < num1-1;j++){
        for(int i = 0 ; i<num1-j-1; i++){
            if (lst[i] > lst[i+1]){
                
                int temp = lst[i];
                lst[i] = lst[i+1];
                lst[i+1] = temp;
            }
        }
    }
}

void binary_search(int lst[], int num1){
    int low = 0;
    int high = (num1);
    int mid;
    int to_find;
    int found = 0;
    printf("Enter element to find:");
    scanf("%d",&to_find);

    while(low<=high){
        mid = (low+high)/2;
        if (to_find<lst[mid])high = mid-1;
        else if (to_find>lst[mid])low = mid+1;
        else if(to_find = lst[mid])found = 1;break;
        
    }

    if (found == 1)printf("Found element!");
    else printf("Element not in list!");
}