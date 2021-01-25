#include<stdio.h>
using namespace std;
long long M = 1000000007;
int dp[1000001]={0};
int solve(int n){
    if (n>0){
        if (dp[n]){
        return dp[n];
        }
        else{
            for (int i=1;i<7;i++){
                dp[n]=solve(n-i);
    }
    }
    
} 
int main(){
    int n;
    cin>>n;
    int a=1,b=2,c=4,d=8,e=16,g=32;
    if (n<7){
        if (n==1){printf()}
    }
}