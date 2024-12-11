# fantastic-rotary-phone
电商接口测试

# 下载第三方包:
 pip install -r XXX.txt
 #本项目执行一下命令就可下载对于的包: 需要进入requirements文件目录才可以进行下载
  pip install -r requirements.txt 
  
commom-

    --cace_template.py  用例模板格式写入
    --debug.py  变量函数结合read_case_data.py文件使用，可以在用例内使用函数变量
    --encryption.py 数据的加密和解密
    --exchange_data.py  变量处理存放处理（已废弃）
    --operator_yaml.py  yaml文件的操作
    --read_case_data.py 读取测试用例的方法
    --read_excel.py     excel文件的操作
    --read_file.py      读取配置文件的方法
    --setting.py        部分设置
    --write_case_result_data.py     把接口返回的结果写入用例的result中，全字段断言使用
    --邮件.py     打包文件发送邮件，邮件的配置项在config的config.yaml中
    
config

    --config.yaml   邮件配置项
    --environment.yaml      环境配置
    --read_environment.py   读取环境配置
    
datas
    用例数据存放
    
    
log
    日志存放
    
    
test_cace  
    用例代码存放处
    ``
    
    
utils

    --asst.py   断言的方法
    --logutil.py    日志记录
    --mails.py  邮件发送
    --mysqlutil.py  数据库的操作
    --requestutil.py 接口请求的操作