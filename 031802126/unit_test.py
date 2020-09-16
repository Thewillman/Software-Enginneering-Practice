import unittest
import test_as_function  # 引用一下计算程序，不然代码属实太长
from BeautifulReport import BeautifulReport

class TestForAllTextTfIdf(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("开始单元测试……")
    @classmethod
    def tearDown(self):
        print("已结束测试")

    def test_self_tfidf(self):
        print("正在载入orig.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig.txt', 'ans.txt')

    def test_add_tfidf(self):
        print("正在载入orig_0.8_add.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt','sim_0.8\orig_0.8_add.txt','ans.txt')

    def test_del_tfidf(self):
        print("正在载入orig_0.8_del.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_del.txt', 'ans.txt')

    def test_dis_1_tfidf(self):
        print("正在载入orig_0.8_dis_1.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_1.txt', 'ans.txt')

    def test_dis_3_tfidf(self):
        print("正在载入orig_0.8_dis_3.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_3.txt', 'ans.txt')

    def test_dis_7_tfidf(self):
        print("正在载入orig_0.8_dis_7.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_7.txt', 'ans.txt')

    def test_dis_10_tfidf(self):
        print("正在载入orig_0.8_dis_10.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_10.txt', 'ans.txt')

    def test_dis_15_tfidf(self):
        print("正在载入orig_0.8_dis_15.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_15.txt', 'ans.txt')

    def test_mix_tfidf(self):
        print("正在载入orig_0.8_mix.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_mix.txt', 'ans.txt')

    def test_rep_tfidf(self):
        print("正在载入orig_0.8_rep.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_rep.txt', 'ans.txt')

    def test_My_database1_add(self):
        print("正在载入My_database1\\orig_add.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_add.txt', 'ans.txt')

    def test_My_database1_del(self):
        print("正在载入My_database1\\orig_del.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_del.txt', 'ans.txt')

    def test_My_database1_dis_1(self):
        print("正在载入My_database1\\orig_dis_1.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_dis_1.txt', 'ans.txt')

    def test_My_database1_dis_3(self):
        print("正在载入My_database1\\orig_dis_3.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_dis_3.txt', 'ans.txt')

    def test_My_database1_dis_7(self):
        print("正在载入My_database1\\orig_dis_7.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_dis_7.txt', 'ans.txt')

    def test_My_database1_dis_10(self):
        print("正在载入My_database1\\orig_dis_10.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_dis_10.txt', 'ans.txt')

    def test_My_database1_dis_15(self):
        print("正在载入My_database1\\orig_dis_15.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_dis_15.txt', 'ans.txt')

    def test_My_database1_mix(self):
        print("正在载入My_database1\\orig_mix.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_mix.txt', 'ans.txt')

    def test_My_database1_rep(self):
        print("正在载入My_database1\\orig_rep.txt")
        test_as_function.solve_tfidf('My_database1\orig.txt', 'My_database1\orig_rep.txt', 'ans.txt')

    # 异常处理，IndexError和TextDifferentError是在调试过程中使用的，目前程序已经没有这个问题
    def test_NoChineseError_tfidf(self):
        print("开始无汉字异常测试QAQ:")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_NoChinese.txt', 'ans.txt')

    def test_TextSameError_tfidf(self):
        print("开始文本相同异常测试QAQ:")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_copy.txt', 'ans.txt')

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestForAllTextTfIdf('test_self_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_add_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_del_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_1_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_3_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_7_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_10_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_15_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_mix_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_rep_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_add'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_del'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_dis_1'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_dis_3'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_dis_7'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_dis_10'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_dis_15'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_mix'))
    suite.addTest(TestForAllTextTfIdf('test_My_database1_rep'))
    suite.addTest(TestForAllTextTfIdf('test_NoChineseError_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_TextSameError_tfidf'))
    runner = unittest.TextTestRunner()
    runner = BeautifulReport(suite)
    runner.report(
        description='论文查重测试报告',  # => 报告描述
        filename='nlp_TFIDF.html',  # => 生成的报告文件名
        log_path='.'  # => 报告路径
    )