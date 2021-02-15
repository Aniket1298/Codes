#include <bits/stdc++.h>
using namespace std;
void solve(){
    long long int M=1000000000+7;
    long long int  i,n,m,j;
    cin>>n>>m;
    int l[n];
    long long int dp[n+1][m+1]={0};
    for (int x=0;x<n;x++){cin>>l[x];}
    for (i=0;i<n;i++){
        for (j=1;j<=m;j++){dp[i][j]=0;}
    }
    i=0;
    for (i=0;i<n;i++){
        if (i==0)
            if (l[i]==0){
                for(j=1;j<=m;j++){dp[i][j]=1;}}
            else{dp[i][l[i]]=1;}
        else{
            if (l[i]==0)
                {
                    j=1;
                    while (j<=m)
                    {
                        dp[i][j]=0;
                        dp[i][j]+=dp[i-1][j];
                        if (j-1>0){dp[i][j]+=dp[i-1][j-1];}
                        if (j+1<=m){dp[i][j]+=dp[i-1][j+1];}
                        dp[i][j]%=M;
                        j+=1;
                    }
                }
            else{
                    j=l[i];
                    dp[i][j]=0;
                    dp[i][j]+=dp[i-1][j];
                    if (j-1>=1){dp[i][j]+=dp[i-1][j-1];}
                    if (j+1<=m){dp[i][j]+=dp[i-1][j+1];}
                    dp[i][j]%=M;
                }
            }
        
    }
    long long int ans=0;
    for (i=1;i<=m;i++){ans+=dp[n-1][i];}
    cout<<ans%M;
}
int main()
{
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}