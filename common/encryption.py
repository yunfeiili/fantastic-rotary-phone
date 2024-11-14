import hashlib,base64


class EncryPtion():
    """
    加密使用
    """

    def MD5_Encryption(self,text):
        md5_new = hashlib.md5(text.encode())
        return md5_new.hexdigest()



    def base64_Encryption(self,text):
        return base64.b64encode(text.encode('utf-8')).decode()




    def base64_Decrypt(self,text):
        return base64.b64decode(text.encode('utf-8')).decode()




# if __name__ == '__main__':
#     shuju = EncryPtion()
    # print(shuju.MD5_Encryption("ksdjksjfks"))
#     print(shuju.base64_Encryption('skjkdsfjkdsjk'))
#     print(shuju.base64_Decrypt("c2tqa2RzZmprZHNqaw=="))

