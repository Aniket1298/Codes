#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n,k;
	cin>>n>>k;
	int l[n]={0};
	for (int i=0;i<n;i++){cin>>l[i];}
	long long dp[k+1];
	for (int i=0;i<=k;i++){dp[i]=0;}
	long M=1e9 +7;
	dp[0]=1;
	//for (int i=0;i<n;i++){if (l[i]<k+1){dp[l[i]]+=1;}}
	    for (int money=0;money<=k;money++){
	        for(int i=0;i<n;i++){
	            
	            if (money>=l[i]){
	                dp[money]+=dp[money-l[i]];
	                
	            }
	        }
	        dp[money]%=M;
	    }
	//for(int i=0;i<=k;i++){cout<<dp[i]<<" ";}
	cout<<dp[k]%M;
	
	return 0;
}

