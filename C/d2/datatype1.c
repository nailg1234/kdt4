static void datatype1() {
	short year = 0; // 8비트 정수형 -32768~32767
	int sale = 0; // 32비트 정수형 -21억 ~ 21억
	long long total_sale = 0;

	year = 10; // 32000 넘지 않도록
	sale = 20000000; // 21억 넘지 않도록
	total_sale = year * sale; 

	printf("%lld \n", total_sale);
}