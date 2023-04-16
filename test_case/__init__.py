

from utils.requestutil import SenApi


class Test():


    def setup_class(self):
        self.sendRequests = SenApi()

    def setup_function(self):
        print('\n', '============还不够与供应供应============' * 9)


    def teardown_function(self):
        print('\n', '===================================' * 9)

    def setup(self):
        pass



    def teardown(self):
        pass


    def teardown_setup_method(self):
        print('======================================')
        pass
