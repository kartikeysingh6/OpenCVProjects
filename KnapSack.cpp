#include <bits/stdc++.h>
using namespace std;

int static dp[1001][1001];
int static t[1001][1001];

int KS(int* wt, int *val, int n,int W){
	//if no items or no capacity we will have no profit
	if(n==0 || W==0)
		return 0;

	//if item has weight more than capacity we 
	//have only once choice i.e NOT to pick it up
	if(wt[n-1]>W)
		return KS(wt,val,n-1,W);
	//if it's less than capacity then we've 2 choices
	//i.e pick it or NOT pick it (select max from them)
	else
		return max(val[n-1] + KS(wt,val,n-1,W-wt[n-1]) , KS(wt,val,n-1,W));
}

int memoizeKS(int* wt, int *val, int n,int W){
	if(n==0 || W==0)
		return 0;

	//checking if there exists any value in table
	//if it does then return it
	if(dp[n][W]!=-1)
		return dp[n][W];

	//ofc this means value in table is -1 so
	//calculate it and save it and return it
	if(wt[n-1]>W)
		return dp[n][W]=KS(wt,val,n-1,W);
	else
		return dp[n][W]=max(val[n-1] + KS(wt,val,n-1,W-wt[n-1]) , KS(wt,val,n-1,W));

}

int topdownKS(int* wt, int *val, int n,int W){
	
	//Initializing the row 0 and column 0
	for(int i=0;i<=n;i++){
		for(int j=0;j<=W;j++){
			if(i==0||j==0)
				t[i][j]=0;
		}
	}

	//Looping through entire table untouching initial zeros
	for(int i=1;i<=n;i++){
		for(int j=1;j<=W;j++){
			if(wt[i-1]>j)
				t[i][j] = t[i-1][j];
			else
				t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]] , t[i-1][j]);
		}
	}

	//bottom right element of the table is the answer
	return t[n][W];
}

int main(){
	memset(dp,-1,sizeof(dp));
	int wt[]={2,1,7,3};
	int val[]={5,3,11,2};
	int W=7;
	int n=sizeof(wt)/sizeof(wt[0]);

	cout<<topdownKS(wt,val,n,W);

}