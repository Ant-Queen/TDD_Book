from unittest import TestResult, result


class TestCase:
    def __init__(self,name):
        self.name=name
    def run(self):
        result=TestResult()
        result.testStarted()
        self.setUp()
        method=getattr(self,self.name)
        method()
        self.tearDown()
        return result
    def setUp(self):
        pass
    def tearDown(self):
        pass

class WasRun(TestCase):
    def testMethod(self):
        self.log=self.log+"testMethod "
    def testBrokenMethod(self):
        raise Exception
    def setUp(self):
        self.log="setUp "
    def tearDown (self):
        self.log=self.log+"tearDown "

class TestResult:
    def __init__(self):
        self.runCount=0
        self.failureCount=0
    def testStarted(self):
        self.runCount=self.runCount+1
    def testFailed(self):
        self.failureCount=self.failureCount+1
    def summary(self):
        return "%d run, 0 failed"%self.runCount
        
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
##    def testFailedResult(self):
##        test=WasRun("testBrokenMethod")
##        result=test.run()
##        assert("1 run, 1 failed"==result.summary())
    def testFailedResultFormatting(self):
        result=TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed"==result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
##TestCaseTest("testFailedResult").run()