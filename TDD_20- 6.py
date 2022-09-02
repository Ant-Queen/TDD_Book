class TestCase:
    def __init__(self,name):
        self.name=name
    def run(self):
        self.setUp()
        method=getattr(self,self.name)
        method()
    def setUp(self):
        pass

class WasRun(TestCase):
    def testMethod(self):
        self.wasRun=1
        self.log=self.log+"testMethod "
    def setUp(self):
        self.wasRun=None
        self.log="setUp "

class TestCaseTest(TestCase):
    def setUp(self):
        self.test=WasRun("testMethod")
    def testTemplateMethod(self):
        self.test.run()
        assert("setUp testMethod tearDown "==self.test.log)

TestCaseTest("testTemplateMethod").run()