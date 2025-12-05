static void prac01(void) {

	int year, month, day;
	int ticket;
	float discount;

	printf("오늘의 날짜를 입력하시오<YYYY.MM.DD 형식으로>: ");
	scanf_s("%d.%d.%d", &year, &month, &day);
	
	printf("\n요즘 영화 한편 보려면 얼마나 하나요? ");
	scanf_s("%d", &ticket);

	printf("\n멤버쉽 카드가 있으면 몇퍼센트나 할인되나요? ");
	scanf_s("%f", &discount);

	printf("\n");
	printf("%d년 %d월 %d일 저녁에\n", year, month, day);
	printf("%d원으로 영화 한편 보면 어때요?\n", ticket);
	printf("%.2f%%나 할인받을수있는데요!\n", discount);

}