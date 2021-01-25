#include <iostream>
using namespace std;
int visited[1001][1001];
string l[1001];
int  solve(int i,int j,int n,int m){
    //cout<<l[i][j]<<"H ";
    if (i<n && j<m && l[i][j]=='.')
    {
        visited[i][j]=true;
        solve(i+1,j,n,m);
        solve(i,j+1,n,m);
    }
}

int main() {
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
