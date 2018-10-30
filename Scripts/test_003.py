import allure

import pytest
# 严重级别
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

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="我是登录操作方法1")
    def test_001(self):
        #调用方法
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="我是登录操作方法2")
    def test_002(self):
        #调用方法
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="我是登录操作方法3")
    def test_003(self):
        #调用方法
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="我是登录操作方法4")
    def test_004(self):
        #调用方法
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="我是登录操作方法5")
    def test_005(self):
        #调用方法
        assert False
