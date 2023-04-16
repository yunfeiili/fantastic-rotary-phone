import colorlog
import logging,time,os
from common.setting import get_long_path

STREAM = True
'''日志颜色配置'''
log_colors_config = {
    #颜色支持 blue蓝，green绿色，red红色，yellow黄色，cyan青色
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

class LogUtil():
    def __init__(self):
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            self.logmane = '{}.log'.format(time.strftime("%Y_%m_%d",time.localtime()))
        self.log_path_file = os.path.join(get_long_path(),self.logmane)
        fh = logging.FileHandler(self.log_path_file,encoding='utf-8',mode='a+')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(filename)s[line:%(lineno)d ] - %(levelname)s: %(message)s "
        )
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        fh.close()

        console_formatter = colorlog.ColoredFormatter(
            # 输出那些信息，时间，文件名，函数名等等
            fmt='%(log_color)s[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            # 时间格式
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors=log_colors_config
        )

        if STREAM:
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(console_formatter)
            self.logger.addHandler(sh)

    def log(self):
        return self.logger


logger =  LogUtil().log()

# if __name__ == '__main__':
#     logger.debug('颜色')
#     logger.info('绿色测试日志保存路径{}')
#     logger.warning('颜色')
#     logger.error('error')
#     logger.critical('critical')
