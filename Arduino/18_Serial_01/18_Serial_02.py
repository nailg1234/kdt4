from flask import Flask, request, jsonify
from flask_cors import CORS
import serial
import time

SERIAL_PORT = 'COM4'
BAUD = 9600

arduino = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
time.sleep(2)

app = Flask(__name__)
CORS(app) # 다른 출처(파일/로컬 서버)에서 접근할 수 있도록 허용
state = "off"

@app.post("/led")

def led():
  global state
  data = request.get_json(force=True)
  desired = data.get("state") # 값이 on이나 off로 저장됨

  if desired == "on":
    arduino.write(b'1')
    state = "on"
  elif desired == "off":
    arduino.write(b'0')
    state = "off"
  else:
    return jsonify({"전송": False, "에러": "state는 'on이나 'off'만 가능합니다."}), 400
  
  # led라는 함수의 return문
  return jsonify({"전송": True, "state": state})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False, threaded=False)