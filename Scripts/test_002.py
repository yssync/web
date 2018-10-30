import allure
# 步骤和描述
class Test_001:

    @allure.step(title="输入用户名")
    def input_name(self):
        # 点击登录
        allure.attach("登录/注册按钮","我是测试，点击登录按钮的描述")
        # 点击输入框
        allure.attach("输入框", "我是输入框描述")

        # 输入用户名
        allure.attach("用户名", "我是用户名描述描述")

    @allure.step(title="输入密码")
    def input_passwd(self):
        pass

    @allure.step(title="我是登录操作方法")
    def test_002(self):
        #调用方法
        self.input_name()
        self.input_passwd()
        assert True



    """
    结果：
        我是登录        --步骤
            输入用户名  ---步骤
                登录注册
                    我是测试，点击登录按钮
                输入框
                    我是输入框
                用户名
                    我是用户名秒速
            输入密码    --步骤
            
    
    """