//We're given an array and we've to tell if it's possible to equally divide it or not

#include <bits/stdc++.h>
using namespace std;

int static t[101][1001];

//Subsetsum memoized code
int subsetSum(int*arr,int n,int sum){
	if(sum==0)
		return 1;
	if(n==0)
		return 0;

	if(t[n][sum]!=-1)
		return t[n][sum];

	if(arr[n-1]>sum)
		return t[n][sum]=subsetSum(arr,n-1,sum);
	else
		return t[n][sum]=subsetSum(arr,n-1,sum-arr[n-1]) || subsetSum(arr,n-1,sum);
}

int EqualSumPart(int *arr,int n){
	//sum of all elements
	int sum=0;
	for(int i=0;i<n;i++)
		sum+=arr[i];

	//we can make two equal halves iff it's even
	if(sum%2!=0)
		return 0;
	//if it's even then do subsetsum for sum/2
	return subsetSum(arr,n,sum/2);
}

int main(){
	memset(t,-1,sizeof(t));

	int arr[]={1,5,11,5};
	int n=sizeof(arr)/sizeof(arr[0]);

	cout<<EqualSumPart(arr,n);

}