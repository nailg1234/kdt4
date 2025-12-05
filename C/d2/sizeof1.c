#include <stdio.h>

static void sizeof1() {
	printf("sizeof short : %d \n", sizeof(short));
	printf("sizeof int : %d \n", sizeof(int));
	printf("sizeof long : %d \n", sizeof(long));
	printf("sizeof long long : %d \n", sizeof(long long));

	/*
		바이트 단위로 출력 1바이트 = 8비트
		sizeof short : 2 // 16비트
		sizeof int : 4 //32비트
		sizeof long : 4 // 32비트
		sizeof long long : 8 // 64비트
	*/
}