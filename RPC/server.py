import zmq


def calculate(num1, num2, op):
    """执行四则运算并返回结果"""
    try:
        num1 = float(num1)
        num2 = float(num2)

        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                return "错误：除数不能为零"
            return num1 / num2
        else:
            return "错误：无效的操作符"
    except ValueError:
        return "错误：请输入有效的数字"


def run_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("计算服务器启动，等待客户端请求...")

    try:
        while True:
            # 接收客户端请求 (num1, num2, op)
            message = socket.recv_json()
            print(f"收到请求: {message}")

            num1 = message['num1']
            num2 = message['num2']
            op = message['op']

            # 计算并返回结果
            result = calculate(num1, num2, op)
            socket.send_json({'result': str(result)})

    except KeyboardInterrupt:
        print("服务器关闭...")
    finally:
        socket.close()
        context.term()


if __name__ == "__main__":
    run_server()