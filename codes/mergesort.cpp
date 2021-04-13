#include <iostream>
using namespace std;
void merge(int start,int mid,int end,int *l){
    int a=mid+1;
    while (start<mid && a<=end){
        if (l[start]>l[a]){
            swap(l[start],l[a]);
            
        }
        start++;
    }
    while (start<=mid && a<=end){
        if (l[start]>l[a]){swap(l[start],l[a]);}
        a+=1;
    }
}
void mergesort(int start,int end,int *l){
    int mid = (start+end)/2;
    if (start<end){
        mergesort(start,mid,l);
        mergesort(mid+1,end,l);
        merge(start,mid,end,l);
    }
    
}

int main() {
	// your code goes here
	int n;cin>>n;
	int l[n];
	for (int i=0;i<n;i++){cin>>l[i];}
	mergesort(0,n-1,l);
	for (int i=0;i<n;i++){cout<<l[i]<<" ";}
	return 0;
}
