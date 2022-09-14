class TestCase:
    def __init__(self,name):
        self.name=name
    def run(self):
        result=TestResult()
        result.testStarted()
        self.setUp()
        try:
            method=getattr(self,self.name)
            method()
        except:
            result.testFailed()
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
        return "%d run, %d failed"%(self.runCount,self.failureCount)

class TestSuite:
    def __init__(self):
        self.tests=[]
    def add(self,test):
        self.tests.append(test)
#변경
    def run(self,result):
        for test in self.tests:
            tset.run(result)
#

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
    def testFailedResultFormatting(self):
        result=TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed"==result.summary())
    def testFailedResult(self):
        test=WasRun("testBrokenMethod")
        result=test.run()
        assert("1 run, 1 failed"==result.summary())
    def testSuite(self):
        suite=TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result=TestResult()
        suite.run(result)
        assert("2 run, 1 failed"==result.summary())

print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testFailedResultFormatting").run().summary())
print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testSuite").run().summary())