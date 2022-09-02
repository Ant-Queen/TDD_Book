class TestCase:
    def __init__(self,name):
        self.name=name
    def run(self):
        self.setUp()
        method=getattr(self,self.name)
        method()
        self.tearDown()
    def setUp(self):
        pass

class WasRun(TestCase):
    def testMethod(self):
        self.log=self.log+"testMethod "
    def setUp(self):
        self.log="setUp "
    def tearDown (self):
        self.log=self.log+"tearDown "
        
class TestCaseTest(TestCase):
    def setUp(self):
        self.test=WasRun("testMethod")
    def testTemplateMethod(self):
        self.test.run()
        assert("setUp testMethod tearDown "==self.test.log)

TestCaseTest("testTemplateMethod").run()