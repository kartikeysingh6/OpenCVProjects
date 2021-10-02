#include<bits/stdc++.h>
using namespace std;

int ncube(int *A, int n){
	int best=0;
	for(int i=0;i<n;i++){
		for(int j=i;j<n;j++){
			int sum=0;
			for(int k=i;k<=j;k++)
				sum+=A[k];
			best=max(best,sum);
		}
	}
	return best;
}

int nsq(int *A,int n){
	int best=0;
	for(int i=0;i<n;i++){
		int sum=0;
		for(int j=i;j<n;j++){
			sum+=A[j];
			best=max(sum,best);
		}
	}
	return best;
}

int n_aka_KadaneAlgo(int *A,int n){
	int best=0,sum=0;
	for(int i=0;i<n;i++){
		sum=max(A[i],sum+A[i]);
		best=max(sum,best);
	}
	return best;
}

int main(){
	int A[]={-1,-2,-3,-4};
	int n=sizeof(A)/sizeof(A[0]);
	cout<<n_aka_KadaneAlgo(A,n);
}