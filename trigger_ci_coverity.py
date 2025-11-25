import os
import json
import requests

# GitHub 仓库信息
OWNER = "peihuafeng"
REPO = "coverity_scan_checksql"
EVENT_TYPE = "ci-coverity"  # 自定义事件名

# 从环境变量读取 GitHub Token
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("请先在环境变量 GITHUB_TOKEN 中配置 GitHub Personal Access Token")

# REST API 端点
url = f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches"

# 请求头
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# 事件数据，可以在 client_payload 里传额外参数
payload = {
    "event_type": EVENT_TYPE,
    "client_payload": {
        "triggered_by": "python-script",
        "message": "Coverity scan requested"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 204:
    print("自定义事件触发成功！")
else:
    print(f"触发失败，状态码: {response.status_code}")
    print(response.text)