from flask import Flask, jsonify

app = Flask(__name__)

# 模拟的天气数据库
weather_data = {
    'Beijing': {'temperature': '22°C', 'condition': 'Sunny', 'humidity': '40%'},
    'Shanghai': {'temperature': '25°C', 'condition': 'Cloudy', 'humidity': '65%'},
    'Guangzhou': {'temperature': '28°C', 'condition': 'Rainy', 'humidity': '80%'},
    'New York': {'temperature': '18°C', 'condition': 'Cloudy', 'humidity': '60%'},
    'London': {'temperature': '15°C', 'condition': 'Rainy', 'humidity': '75%'}
}

@app.route('/weather/<string:city>', methods=['GET'])
def get_weather(city):
    """获取城市天气信息"""
    if city in weather_data:
        return jsonify({
            'city': city,
            'data': weather_data[city],
            'status': 'success'
        })
    else:
        return jsonify({
            'city': city,
            'message': 'City not found',
            'status': 'error'
        }), 404

@app.route('/weather/all', methods=['GET'])
def get_all_weather():
    """获取所有城市天气信息"""
    return jsonify({
        'data': weather_data,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)