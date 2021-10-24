//Same as subset sum but instead or returning true return no. of ways
//we can create that sum

#include <bits/stdc++.h>
using namespace std;

int static t[101][1001];

int CountSubSum(int *arr,int n,int sum){
	if(sum==0)
		return 1;
	if(n==0)
		return 0;

	if(arr[n-1]>sum)
		return CountSubSum(arr,n-1,sum);
	/*
	Not using OR because if any subset we found OR will make true and we would've stopped
	but we have to keep counting. so it will make a tree and keep adding 1(return value for true) 
	for each case of correct subset.

	*/

	return CountSubSum(arr,n-1,sum-arr[n-1]) + CountSubSum(arr,n-1,sum);
}

int tCountSubSum(int* arr,int n,int sum){
	for(int i=0;i<=n;i++){
		for(int j=0;j<=sum;j++){
			if(i==0)
				t[i][j]=0;
			if(j==0)
				t[i][j]=1;
		}
	}

	for(int i=1;i<=n;i++){
		for(int j=1;j<=sum;j++){

			if(t[i][j]!=-1)
				return t[i][j];

			if(arr[i-1]>j)
				t[i][j]=t[i-1][j];
			else
				t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j];

		}
	}

	return t[n][sum];

}


int main(){
	memset(t,-1,sizeof(t));
	int arr[]={2,3,5,10,8};
	int n=sizeof(arr)/sizeof(arr[0]);
	int sum=10;

	cout<<rCountSubSum(arr,n,sum);
}