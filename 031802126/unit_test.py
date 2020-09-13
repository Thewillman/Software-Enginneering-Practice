import unittest
import test_as_function  # 引用一下计算程序，不然代码属实太长
from BeautifulReport import BeautifulReport

class TestForAllText(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("开始单元测试……")
    @classmethod
    def tearDown(self):
        print("已结束测试")

    def test_self(self):
        print("正在载入orig.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig.txt', 'ans.txt')

    def test_add(self):
        print("正在载入orig_0.8_add.txt")
        test_as_function.solve('sim_0.8\orig.txt','sim_0.8\orig_0.8_add.txt','ans.txt')

    def test_del(self):
        print("正在载入orig_0.8_del.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_del.txt', 'ans.txt')

    def test_dis_1(self):
        print("正在载入orig_0.8_dis_1.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_1.txt', 'ans.txt')

    def test_dis_3(self):
        print("正在载入orig_0.8_dis_3.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_3.txt', 'ans.txt')

    def test_dis_7(self):
        print("正在载入orig_0.8_dis_7.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_7.txt', 'ans.txt')

    def test_dis_10(self):
        print("正在载入orig_0.8_dis_10.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_10.txt', 'ans.txt')

    def test_dis_15(self):
        print("正在载入orig_0.8_dis_15.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_15.txt', 'ans.txt')

    def test_mix(self):
        print("正在载入orig_0.8_mix.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_mix.txt', 'ans.txt')

    def test_rep(self):
        print("正在载入orig_0.8_rep.txt")
        test_as_function.solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_rep.txt', 'ans.txt')

    def test_My_database1_add(self):
        print("正在载入My_database1\\orig_add.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_add.txt', 'ans.txt')

    def test_My_database1_del(self):
        print("正在载入My_database1\\orig_del.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_del.txt', 'ans.txt')

    def test_My_database1_dis_1(self):
        print("正在载入My_database1\\orig_dis_1.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_dis_1.txt', 'ans.txt')

    def test_My_database1_dis_3(self):
        print("正在载入My_database1\\orig_dis_3.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_dis_3.txt', 'ans.txt')

    def test_My_database1_dis_7(self):
        print("正在载入My_database1\\orig_dis_7.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_dis_7.txt', 'ans.txt')

    def test_My_database1_dis_10(self):
        print("正在载入My_database1\\orig_dis_10.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_dis_10.txt', 'ans.txt')

    def test_My_database1_dis_15(self):
        print("正在载入My_database1\\orig_dis_15.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_dis_15.txt', 'ans.txt')

    def test_My_database1_mix(self):
        print("正在载入My_database1\\orig_mix.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_mix.txt', 'ans.txt')

    def test_My_database1_rep(self):
        print("正在载入My_database1\\orig_rep.txt")
        test_as_function.solve('My_database1\orig.txt', 'My_database1\orig_rep.txt', 'ans.txt')

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestForAllText('test_self'))
    suite.addTest(TestForAllText('test_add'))
    suite.addTest(TestForAllText('test_del'))
    suite.addTest(TestForAllText('test_dis_1'))
    suite.addTest(TestForAllText('test_dis_3'))
    suite.addTest(TestForAllText('test_dis_7'))
    suite.addTest(TestForAllText('test_dis_10'))
    suite.addTest(TestForAllText('test_dis_15'))
    suite.addTest(TestForAllText('test_mix'))
    suite.addTest(TestForAllText('test_rep'))
    suite.addTest(TestForAllText('test_My_database1_add'))
    suite.addTest(TestForAllText('test_My_database1_del'))
    suite.addTest(TestForAllText('test_My_database1_dis_1'))
    suite.addTest(TestForAllText('test_My_database1_dis_3'))
    suite.addTest(TestForAllText('test_My_database1_dis_7'))
    suite.addTest(TestForAllText('test_My_database1_dis_10'))
    suite.addTest(TestForAllText('test_My_database1_dis_15'))
    suite.addTest(TestForAllText('test_My_database1_mix'))
    suite.addTest(TestForAllText('test_My_database1_rep'))
    runner = BeautifulReport(suite)
    runner.report(
        description='论文查重测试报告',  # => 报告描述
        filename='nlp.html',  # => 生成的报告文件名
        log_path='.'  # => 报告路径
    )
