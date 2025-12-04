#include <stdio.h>
#define PI 3.141592

static void vari() {

	// C언어 식별자 규칙
	// 1. 영문자, 숫자, 밑줄문자(_)로 이루어짐
	// 2. 첫글자는 영문 혹은 밑줄문자(_)
	// 3. 대소문자 구분
	// 
	// 불가
	// 1. 숫자로 시작 불가
	// 2. #과 같은 기호 불가
	// 3. double, int 등 키워드 불가


	int x = 325236;
	printf("%d\n", x);

	int number = 23;
	float grade = 3.99;

	printf("%5d%5.2f\n", number, grade);
	int a = 1;
	int b = 2;
	int tmp = 0;

	tmp = a;
	a = b;
	b = tmp;

	printf("%d %d\n", a, b);

	float radius = 10;
	printf("%f\n", radius);
	scanf_s("%f", &radius);

	float area = PI * radius * radius;
	printf("원의 면적 : %f\n", area);

	int c = 5;
	int d = 6;
	int e = 7;

	printf("%d * %d * %d = %d", c, d, e, c * d * e);
}
