# PCR编程

这是一个使用PyZMQ实现的简单的四则运算

## 框架
C/S（客户端-服务器）架构：

### 客户端（Client）：

使用 Tkinter 提供 GUI 界面，用户输入数字和运算符。

使用 REQ Socket 向服务器发送计算请求 {num1, num2, op}。

接收服务器返回的计算结果并显示。

### 服务器（Server）：

使用 REP Socket 监听客户端请求。

解析 num1、num2 和 op，执行四则运算。

返回计算结果 {result}。

## 通信流程
![](RPC结构.png "标题")

## 心得：
我们选取的包：ZeroMQ优势在于，相比传统 Socket 编程，ZeroMQ 封装了底层细节（如连接管理、消息分帧），开发更简单。
而且REQ-REP 模式 适用于 RPC 场景，不过需要注意严格的消息顺序（必须一问一答）。
其次，Tkinter + ZeroMQ 的结合： Tkinter 提供友好的 GUI，ZeroMQ 负责网络通信，两者结合可实现 分布式 GUI 应用。

### 运行界面
![](RPCserver.png "标题")
![](RPCclient.png "标题")