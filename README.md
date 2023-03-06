### MQTT


### 开发说明
### TODO
1. 熟悉各个云平台的基本功能    
2. 理解MQTT，为什么用订阅模式，为什么省电，存在什么问题。怎么区分client的身份，能否假冒消息。

#### 项目说明  
1. 目录结构：  
```
$tree -L 1
.
├── README.md
├── apps                 # 各个云平台的基本功能的完整Demo
├── cloud-api-demo       # 云平台的Notebook文档和代码段
├── python-linkkit-examples     #Aliyun Python预注册和免注册代码
└── requirements.txt

```

2. Python版本3.9 or 3.10  <font color=red>如果使用linkkit需要使用Python3.8</font>
建议用PyCharm开发，notebook可在浏览器中开发，这里我们使用的jupter lab，为了兼容notebook所以indent都用space(4)。  
在notebook上开发各平台的API demo，好处是能添加注释以及在文档中保留代码运行结果。  
```
pip3 install -r requirements.txt  

jupyter lab
# 然后在浏览器打开 jupyter的url，例如：http://127.0.0.1:8888/?token=xxx
```
