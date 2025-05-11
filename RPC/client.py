import zmq
import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("远程计算器")

        # 初始化ZeroMQ连接
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5555")

        # 创建UI
        self.create_widgets()

    def create_widgets(self):
        # 数字1输入
        tk.Label(self.root, text="数字1:").grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        # 运算符选择
        tk.Label(self.root, text="运算符:").grid(row=1, column=0, padx=5, pady=5)
        self.op_var = tk.StringVar(value='+')
        tk.Radiobutton(self.root, text="+", variable=self.op_var, value='+').grid(row=1, column=1, sticky='w')
        tk.Radiobutton(self.root, text="-", variable=self.op_var, value='-').grid(row=2, column=1, sticky='w')
        tk.Radiobutton(self.root, text="×", variable=self.op_var, value='*').grid(row=3, column=1, sticky='w')
        tk.Radiobutton(self.root, text="÷", variable=self.op_var, value='/').grid(row=4, column=1, sticky='w')

        # 数字2输入
        tk.Label(self.root, text="数字2:").grid(row=5, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=5, column=1, padx=5, pady=5)

        # 计算按钮
        calc_btn = tk.Button(self.root, text="计算", command=self.calculate)
        calc_btn.grid(row=6, column=0, columnspan=2, pady=10)

        # 结果显示
        tk.Label(self.root, text="结果:").grid(row=7, column=0, padx=5, pady=5)
        self.result_label = tk.Label(self.root, text="", bg='white', width=20, anchor='w')
        self.result_label.grid(row=7, column=1, padx=5, pady=5)

    def calculate(self):
        # 获取输入值
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        op = self.op_var.get()

        # 验证输入
        if not num1 or not num2:
            messagebox.showerror("错误", "请输入两个数字")
            return

        try:
            # 发送请求到服务器
            self.socket.send_json({
                'num1': num1,
                'num2': num2,
                'op': op
            })

            # 接收响应
            response = self.socket.recv_json()
            self.result_label.config(text=response['result'])

        except Exception as e:
            messagebox.showerror("错误", f"计算时发生错误: {str(e)}")

    def __del__(self):
        # 清理ZeroMQ资源
        self.socket.close()
        self.context.term()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()