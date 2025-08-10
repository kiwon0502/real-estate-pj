from flask import Flask

# Flask 애플리케이션 생성
app = Flask(__name__)


# URL 경로('/')에 접속했을 때 실행될 함수 정의
@app.route('/')
def hello_world():
    return 'Hello, World!'


# 이 파일이 직접 실행될 경우 개발 서버 구동
if __name__ == '__main__':
    app.run(debug=True)
