#include <iostream>
using namespace std;
int visited[1001][1001];
string l[1001];
void  solve(int i,int j,int n,int m){
    
        visited[i][j]=true;
        if (i+1<n  && visited[i+1][j]==false && l[i+1][j]=='.'){solve(i+1,j,n,m);}
        if (j+1<m && visited[i][j+1]==false && l[i][j+1]=='.'){solve(i,j+1,n,m);}
        if (i-1>=0 && visited[i-1][j]==false && l[i-1][j]=='.'){solve(i-1,j,n,m);}
        if (j-1>=0 && visited[i][j-1]==false && l[i][j-1]=='.'){solve(i,j-1,n,m);}
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,m;
    cin>>n>>m;
    for (int i=0;i<n;i++){
        cin>>l[i];
        for (int j=0;j<m;j++)
        {visited[i][j]=false;}
    }
    int rooms=0;
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            
            //cout<<" "<<l[i][j]<<" ";
            if (visited[i][j]==false && l[i][j]=='.'){
                rooms++;
                solve(i,j,n,m);
            }
        }
    }
    cout<<rooms;
    
	return 0;
}