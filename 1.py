from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import datetime


app = Flask(__name__)


CORS(app)

db = pymysql.connect(
    host="localhost",      
    user="root",       
    password="194066089",  
    database="mysql"  
)

@app.route('/post', methods=['POST'])
def hello_world():
    try:
        data = request.get_json()
        expression = data.get('calculation')
        result = data.get('value')
        print(str(calculation) + "=" + str(value))

        cursor = db.cursor()

        sql = "INSERT INTO calculations (calculation, value) VALUES (%s, %s)"
        values = (calculation, value)
        cursor.execute(sql, values)

        db.commit()

        cursor.close()
    except Exception as e:
        print("Error:", e)

@app.route('/get', methods=['GET'])
def get_calculation_data():
    try:
        cursor = db.cursor()

        sql = "SELECT expression, result FROM calculations ORDER BY id DESC LIMIT 10"
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()

        history_data = [{"calculation": item[0], "value": item[1]} for item in data]
        return jsonify({"data": history_data})
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    app.run(host='localhost', port=9000)

