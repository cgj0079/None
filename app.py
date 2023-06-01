from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB 연결 설정
client = MongoClient('mongodb+srv://cgj0079:00791004@cluster0.p6xynpw.mongodb.net/')
db = client['science']  # MongoDB 데이터베이스 선택
collection = db['name']  # MongoDB 컬렉션 선택

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.form['data']  # HTML 폼에서 입력된 데이터 가져오기

    # MongoDB에 데이터 저장하기
    collection.insert_one({'data': data})

    return "데이터가 성공적으로 저장되었습니다!"

@app.route('/show')
def show_data():
    # MongoDB에서 데이터 조회하기
    data_list = collection.find()

    return render_template('index.html', data_list=data_list)

if __name__ == '__main__':
    app.run()
