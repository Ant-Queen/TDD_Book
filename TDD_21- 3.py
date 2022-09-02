from unittest import TestResult


class TestCase:
    def __init__(self,name):
        self.name=name
    def run(self):
        self.setUp()
        method=getattr(self,self.name)
        method()
        self.tearDown()
        return TestResult()
    def setUp(self):
        pass
    def tearDown(self):
        pass

class WasRun(TestCase):
    def testMethod(self):
        self.log=self.log+"testMethod "
    def setUp(self):
        self.log="setUp "
    def tearDown (self):
        self.log=self.log+"tearDown "

class TestResult:
    def summary(self):
        return "1 run, 0 failed"
        
class TestCaseTest(TestCase):
    def setUp(self):
        self.test=WasRun("testMethod")
    def testTemplateMethod(self):
        self.test.run()
        assert("setUp testMethod tearDown "==self.test.log)
    def testResult(self):
        test=WasRun("testMethod")
        result=test.run()
        assert("1 run, 0 failed" == result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()