#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){
	double x, y, pi;
	long i, n, m;
	
	pi=x=y=0.0;
	m=0;

	printf("*****************\n");
	printf("Monte Carlo Simul\n");
	printf("*****************\n");
	printf("\n");
	printf("Please define number of paths:\n");
	scanf("%ld", &n);
	for(i==0;i<=n;i++){
		x=rand()/(RAND_MAX+1.0);
		y=rand()/(RAND_MAX+1.0);
		if(x*x+y*y<=1.0){
			m++;
		}
	}
	pi=m*4.0/n;
	printf("Pi=%l1.6f\n", pi);

	return 0;
}
