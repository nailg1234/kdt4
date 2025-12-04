#include <stdio.h>

static void escape() {
	printf("\a"); // 경고(컴퓨터 벨소리)
	printf("\n"); // 줄바꿈
	printf("1234\b5678\n");  //백 스페이스
	printf("1\t2"); // 탭
	printf("\\") / // 백슬래시
	printf("\'"); // 작은 따옴표
	printf("\""); // 큰 따옴표
	printf("**\tPROGRAMMING\t**");
}