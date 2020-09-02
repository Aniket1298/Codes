
#include <iostream>
using namespace std;
#define INT_MAX 9999999
struct TreeNode{
    int data;
    struct TreeNode* left ;
    struct TreeNode* right; 
};
 
int getMin(int x, int y) 
{ 
    return (x < y)? x :y; 
} 
int findClosestUtil(struct TreeNode *root, int k, struct TreeNode *ancestors[], 
                                               int index) 
{ 
    if (root == NULL) 
        return INT_MAX; 
  
    if (root->data == k) 
    { 
        int res = closestDown(root); 
  
        for (int i = index-1; i>=0; i--) 
            res = getMin(res, index - i + closestDown(ancestors[i])); 
        return res; 
    } 
  
    ancestors[index] = root; 
    return getMin(findClosestUtil(root->left, k, ancestors, index+1), 
                  findClosestUtil(root->right, k, ancestors, index+1)); 
  
} 



void findLeafDown(TreeNode *root, int lev, int *minDist) 
{
    if (root == NULL) 
        return ; 
  
    if (root->left == NULL && root->right == NULL) 
    { 
        if (lev < (*minDist)) 
            *minDist = lev; 
        return; 
    } 
   
    findLeafDown(root->left, lev+1, minDist); 
    findLeafDown(root->right, lev+1, minDist); 
}
int closestDown(struct TreeNode *root) 
{ 
    if (root == NULL) 
        return 999999999; 
    if (root->left == NULL && root->right == NULL) 
        return 0; 

    return 1 + getMin(closestDown(root->left), closestDown(root->right)); 
} 

int ClosestLeaf(struct TreeNode* tree,int k){
    struct TreeNode *ancestors[100]; 
  
    return findClosestUtil(root, k, ancestors, 0); 
    
}
int main(){
    cout<<"Hello";
    return 0;
}




#include <bits/stdc++.h> 
using namespace std;
int main(){
    int n=10;
    int arr[] ={3,4,5,-3,100,3,90,55,23,20};
    sort(arr,n);
    int a=0,b=0,i;
    i=0;
    while (i<n-1){
        a+=arr[i];
        if (i+1<n){b+=arr[i+1];}
        i+=1;
    }
    if (a<b){cout<<b-a;}
    else{cout<<a-b;}
    return 0;
}