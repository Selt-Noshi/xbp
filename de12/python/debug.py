import requests

# 示例 headers 和 data
headers = {
    'Authorization': 'Bearer your_api_key',
    'Content-Type': 'application/json'
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [{'role': 'user', 'content': 'Hello, GPT!'}]
}

# 确保 URL 用引号括起来
response = requests.post("https://free.v36.cm", headers=headers, json=data)

# 打印响应内容以便调试
print(f"响应状态码: {response.status_code}")
print(f"响应内容: {response.text}")
