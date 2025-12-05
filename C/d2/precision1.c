static void precision1(void) {
	float x = 1.234567890123456789;
	double y = 1.234567890123456789;
	long double z = 1.234567890123456789;

	printf("float의 크기 = %d\n", sizeof(float));
	printf("double의 크기 = %d\n", sizeof(double));
	printf("long double의 크기 = %d\n", sizeof(long double));

	printf("x = %.25f\n", x);
	printf("y = %.25lf\n", y);
	printf("z = %.25f\n", z);
}