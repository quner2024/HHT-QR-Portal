import requests
import json
import qrcode
# 请修改这一行url即可 
url = "https://api.215123.cn/web-app/auth/certificateLogin?openId=???&unionId=???"

# 发送GET请求以获取JSON数据
response = requests.get(url)
# 检查响应是否成功
if response.status_code == 200:
    # 解析JSON响应
    data_dict = json.loads(response.text)
    # 提取"token"信息
    token = data_dict["data"]["token"]
    # 打印token
    print("Token:", token)
else:
    print("请求失败，状态码:", response.status_code)

# 设置请求头
headers = {
    "satoken": token,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/en",
    "Referer": "https://servicewechat.com/wx2660b404a3b7575a/97/page-frame.html"
}
# 发送GET请求
url = "https://api.215123.cn/pms/welcome/make-code-info"
response = requests.get(url, headers=headers)
# 检查响应是否成功
if response.status_code == 200:
    # 获取整个响应内容
    response_content = response.text
    # 解析JSON响应
    data_dict_2 = json.loads(response.content)
    # 提取"token"信息
    token = data_dict_2["data"]["qrCode"]
    # 打印token
    print("qrCode:", token)
else:
    print("请求失败，状态码:", response.status_code)

# 创建QR码对象
qr = qrcode.QRCode(
    version=1,  # 版本号，可以是1到40之间的整数，表示QR码的大小
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 错误纠正级别，可选值包括L（低）、M（中）、Q（高）、H（最高）
    box_size=10,  # 每个QR码块的像素大小
    border=4,  # QR码的边距大小
)

# 将文本添加到QR码中
qr.add_data(token)
qr.make(fit=True)

# 创建QR码图像
img = qr.make_image(fill_color="black", back_color="white")

# 显示QR码图像
img.show()
