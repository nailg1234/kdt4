#include <SoftwareSerial.h>
SoftwareSerial esp8266(2, 3);  // RX=D2, TX=D3

const char *ssid = "spreatics_eungam_cctv";
const char *password = "spreatics*";
const char *server = "192.168.1.248";
const int port = 5000;

// sendCommand(): ESP 모듈에 AT 명령을 보내, 응답 중 특정 단어가 나올 때까지 기다리는 함수
// 예를 들어 명령 처리를 완료했으면 OK를 보내라고 지정 시 OK가 올 때까지 실행됨
// bool: 반환값으로 응답을 잘 했는지 확인
// cmd: 보낼 명령
// expect: 응답에서 원하는 문자열
// timeout: 기다릴 시간
bool sendCommand(String cmd, String expect, int timeout) {
  esp8266.print(cmd);

  unsigned long t = millis(); // 시작 시간을 저장해 종료 시간 계산하기 위한 변수
  String buf; // esp가 보낸 문자열을 합칠 변수

  while (millis() - t < timeout) { // timeout 동안만 동작하겠다
    while (esp8266.available()) { // esp-01이 보낸 데이터가 있는지 확인
      char c = esp8266.read(); // 한 글자씩 읽어오기
      buf += c; // 읽은 글자를 buf에 이어붙이기
      Serial.write(c); // 시리얼 모니터에 출력

      if (buf.indexOf(expect) != -1) { // 전달받은 문자열 중 내가 원하는 단어가 있으면 true 리턴
        return true;
      }
    }
  }
  return false; // 아니라면 false로 실패 처리
}

void setup() {
  Serial.begin(9600);     // PC ↔ 아두이노
  esp8266.begin(9600);      // ESP ↔ 아두이노 통신 속도 (안정)

  Serial.println("ESP Setup Start...");

  sendCommand("AT", "OK", 2000); // esp 살아있는지 확인
  sendCommand("AT+CWMODE=1", "OK", 2000); // esp를 일반 wifi 기기 모드로 설정
  sendCommand(String("AT+CWJAP=\"") + ssid + "\",\"" + password + "\"",
              "GOT IP", 15000); // 위에 작성한 공유기로 접속해라
  sendCommand("AT+CIPMUX=0", "OK", 2000); // 연결 시 1개의 TCP만 쓰겠다 (한 번의 연결에 데이터는 한 번만 주고받겠다)
}

void loop() { // 5초마다 sendDataToServer() 함수 실행 -> 서버로 데이터 전송
  sendDataToServer(25, 60);
  delay(5000);
}

void sendDataToServer(int temp, int hum) {
  String url = "/data?temperature=" + String(temp) +
               "&humidity=" + String(hum); // 쿼리스트링으로 HTTP GET 요청 경로 작성

  if (!sendCommand("AT+CIPSTART=\"TCP\",\"" + String(server) + "\"," + port,
                   "CONNECT", 5000)) // AT+CIPSTART: 서버와 TCP 연결
    return;

  String req =
      "GET " + url + " HTTP/1.1\r\n" // \r\n은 시작이나 종료를 알리는 빈 줄
      "Host: " + String(server) + ":" + String(port) + "\r\n"
      "Connection: close\r\n\r\n";

  // String(req.length()): HTTP 요청 문자열 바이트 수 계산
  if (sendCommand("AT+CIPSEND=" + String(req.length()), ">", 3000)) { // ">" 나올 때 까지 3초 기다림
    esp8266.print(req); // HTTP 전송
    sendCommand("", "SEND OK", 4000); // ESP가 OK라고 할 떄까지 4초 기다림 -> 데이터 전송 완료 기다림
  }

  sendCommand("AT+CIPCLOSE", "OK", 2000);  // AT+CIPCLOSE: TCP 연결 종료
  Serial.println("\n[전송 완료]");
}

// =====

// 흐름 정리

/*
  1. setup()
    - AT: ESP 살아있는지 확인
    - AT+CWMODE=1: Wifi 동작 모드 설정
    - AT+CWJAP="ssid","password": 와이파이 공유기 접속
    - AT+CIPMUX=0: 안정적인 통신을 위해 한 번에 하나의 연결만 하도록 제한
*/

/*
  2. loop()
    - 5초마다 sendDataToServer(25, 60) 실행
    - sendDataToServer()
      - AT+CIPSTART="TCP","서버IP",포트: TCP 열기
      - 온도와 습도에 해단 HTTP 요청 문자열 생성
      - AT+CIPSEND=길이: 해당 길이만큼 HTTP 요청
      - > 나올 때까지 기다리면서 HTTP GET 요청 전송
      - AT+CIPCLOSE로 연결 종료
*/

/*
  3. senCommand()
    - 공통 유틸 함수
    - 명령 문자열과 \r\n(종료용 빈 문자열) 전송
    - ESP 응답을 읽어 시리얼 모니터에 출력
    - 응답 안에 원하는 문자열 나오면 성공
    - timeout 까지 안나오면 실패
*/