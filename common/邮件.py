

import zipfile
import os

import yagmail as yagmail


class EmailServe:

    @staticmethod
    def zip_report(file_path: str, out_path: str):
        """
        压缩指定文件夹
        :param file_path: 目标文件夹路径
        :param out_path: 压缩文件保存路径+xxxx.zip
        :return: 无
        """
        #file_path = f"{file_path}/test_report"
        zip = zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(file_path):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(file_path, '')

            for filename in filenames:
                zip.write(
                    os.path.join(
                        path, filename), os.path.join(
                        fpath, filename))
        zip.close()

    @staticmethod
    def send_email(setting: dict, file_path):
        """
        入参一个字典
        :param user: 发件人邮箱
        :param password: 邮箱授权码
        :param host: 发件人使用的邮箱服务 例如：smtp.163.com
        :param contents: 内容
        :param addressees: 收件人列表
        :param title: 邮件标题
        :param enclosures: 附件列表
        :param file_path: 需要压缩的文件夹
        :return:
        """


        print('开始将allure报告压缩zip包')
        EmailServe.zip_report(
            file_path=file_path,
            out_path=setting['enclosures'])

        print('压缩打包allure报告完成')
        yag = yagmail.SMTP(
            setting['user'],
            setting['password'],
            setting['host'])
        # 发送邮件

        print('开始发送邮件……')

        yag.send(
            setting['addressees'],
            setting['title'],
            # result_data_test,
            setting['enclosures'])
        # setting['contents']
        # 关闭服务
        yag.close()
        print("邮件发送成功！")


# if __name__ == '__main__':
#     EmailServe.zip_report('../reports', '../reports.zip')
#     file_path='../reports.zip'
#     from common.read_file import ReadFile
#
# # setting = ReadFile.read_config('$.email')
#     setting = ReadFile.get_config_dict()['email']
#
#
#     EmailServe.send_email(setting,file_path)
