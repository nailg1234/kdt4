#include <stdio.h>

static void scanf1() {
	//double grade;
	//printf("학점을 입력하시오");
	//scanf_s("%lf", &grade);
	//printf("학점이 %lf학점 이시군요!", grade);

	//int a, b;
	//printf("첫번쨰 숫자를 입력하세요.");
	//scanf_s("%d", &a);
	//printf("두번쨰 숫자를 입력하세요.");
	//scanf_s("%d", &b);
	//printf("%d + %d = %d", a, b, a + b);


	/*int a, b, c;
	printf("정수를 입력하세요");
	scanf_s("%d", &a);
	printf("정수를 입력하세요");
	scanf_s("%d", &b);
	printf("정수를 입력하세요");
	scanf_s("%d", &c);

	printf("평균값은 %d 입니다.", (a + b + c) / 3);*/

	double r; // 원의 반지름
	double area; // 원의 면적
	double peri; // 원의 둘레

	printf("원의 반지름을 입력하시오.");
	scanf_s("%lf", &r);
	area = 3.14 * r * r;
	peri = 2.0 * 3.14 * r;

	printf("원의 면적 : %lf", area);
	printf("원의 둘레 : %lf", peri);
	printf("\n");
	int a, b;
	scanf_s("%d %d", &a, &b);
	printf("%d %d", a, b);

}