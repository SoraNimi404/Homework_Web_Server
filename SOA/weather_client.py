import requests


def get_weather(city):
    """调用天气服务获取指定城市天气"""
    try:
        response = requests.get(f'http://localhost:5000/weather/{city}')
        data = response.json()

        if data['status'] == 'success':
            print(f"\n天气信息 - {data['city']}:")
            print(f"温度: {data['data']['temperature']}")
            print(f"条件: {data['data']['condition']}")
            print(f"湿度: {data['data']['humidity']}")
        else:
            print(f"错误: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"服务调用失败: {e}")


def get_all_weather():
    """获取所有城市天气"""
    try:
        response = requests.get('http://localhost:5000/weather/all')
        data = response.json()

        if data['status'] == 'success':
            print("\n所有城市天气信息:")
            for city, info in data['data'].items():
                print(f"\n{city}:")
                print(f"  温度: {info['temperature']}")
                print(f"  条件: {info['condition']}")
                print(f"  湿度: {info['humidity']}")
    except requests.exceptions.RequestException as e:
        print(f"服务调用失败: {e}")


if __name__ == '__main__':
    while True:
        print("\n天气查询系统")
        print("1. 查询单个城市天气")
        print("2. 查看所有城市天气")
        print("3. 退出")

        choice = input("请选择操作(1/2/3): ")

        if choice == '1':
            city = input("请输入城市名称: ")
            get_weather(city)
        elif choice == '2':
            get_all_weather()
        elif choice == '3':
            print("谢谢使用，再见!")
            break
        else:
            print("无效选择，请重新输入!")