import serial # pyserial 라이브러리
import time 

# com4: 아두이노 시리얼 연결 포트
arduino = serial.Serial("com4", 9600)
time.sleep(1)

while 1:
    var = input() # 터미널에서 입력된 문자열 저장

    if var == "1":
        # 아두이노에게 값을 전달하기 위해 바이트 형식으로 인코딩
        var = var.encode("utf-8")
        arduino.write(var) # 아두이노에 바이트 형식으로 변환된 "1"을 보냄
        print("LED ON")
        time.sleep(1)
    elif var == "0":
        var = var.encode("utf-8")
        arduino.write(var)
        print("LED OFF")
        time.sleep(1)
    else:
        break