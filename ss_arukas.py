import re,base64,qrcode
import requests,json
from requests.auth import HTTPBasicAuth

#参数
user = 'xxxxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
headers = {'Content-Type':'application/vnd.api+json','Accept':'application/vnd.api+json'}
url = 'https://app.arukas.io/api/containers'

#列出容器
containers = json.loads(requests.get(url,headers=headers,auth=HTTPBasicAuth(user, password)).text)
guogle_docker = containers['data'][1]['attributes']['port_mappings'][0][0] #匹配出服务器信息
host = guogle_docker['host'].replace('-','.')
port = guogle_docker['service_port']
#匹配器
pattern = re.compile(r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)')
ip = pattern.search(host).group()
#二维码生成并显示
ss_info = ('#加密方式#:#密码#@'+str(ip)+':'+str(port))
qrcode_text = 'ss://'+base64.b64encode(ss_info.encode(encoding="utf-8")).decode('utf-8')
img = qrcode.make(qrcode_text)
img.show()

print (guogle_docker,'\n',ip,'\n',port)
