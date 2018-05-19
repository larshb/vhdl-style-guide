
import unittest

from vsg import junit

class testJunitClasses(unittest.TestCase):


    def test_failure_class_attributes(self):
        oFailure = junit.failure('Type1')
        self.assertTrue(oFailure)
        self.assertEqual(oFailure.type, 'Type1')
        self.assertEqual(oFailure.text, None)

    def test_failure_class_add_text(self):
        oFailure = junit.failure('type')
        oFailure.add_text('Text1')
        oFailure.add_text('Text2')
        oFailure.add_text('Text3')
        self.assertEqual(oFailure.type, 'type')
        self.assertEqual(oFailure.text[0], 'Text1')
        self.assertEqual(oFailure.text[1], 'Text2')
        self.assertEqual(oFailure.text[2], 'Text3')

    def test_failure_class_build_junit(self):
        oFailure = junit.failure('type')
        oFailure.add_text('Text1')
        oFailure.add_text('Text2')
        oFailure.add_text('Text3')
        dExpected = []
        dExpected.append('      <failure type="type">')
        dExpected.append('        Text1')
        dExpected.append('        Text2')
        dExpected.append('        Text3')
        dExpected.append('      </failure>')
        self.assertEqual(dExpected, oFailure.build_junit())

    def test_testcase_class_attributes(self):
        oTestcase = junit.testcase()
        self.assertTrue(oTestcase)
        self.assertEqual(oTestcase.name, None)
        self.assertEqual(oTestcase.time, None)
        self.assertEqual(oTestcase.classname, None)
        self.assertEqual(oTestcase.failures, None)

    def test_testcase_class_attribute_setting(self):
        oTestcase = junit.testcase('Name', 'Time', 'classname')
        self.assertEqual(oTestcase.name, 'Name')
        self.assertEqual(oTestcase.time, 'Time')
        self.assertEqual(oTestcase.classname, 'classname')
        self.assertEqual(oTestcase.failures, None)

    def test_testcase_class_add_failure(self):
        oTestcase = junit.testcase('Name', 'Time', 'classname')
        oTestcase.add_failure(junit.failure('Type1'))
        oTestcase.add_failure(junit.failure('Type2'))
        oTestcase.add_failure(junit.failure('Type3'))
        self.assertEqual(oTestcase.failures[0].type, 'Type1')
        self.assertEqual(oTestcase.failures[1].type, 'Type2')
        self.assertEqual(oTestcase.failures[2].type, 'Type3')
       
    def test_testcase_class_build_junit(self):
        oTestcase = junit.testcase('Name', 'Time', 'Classname')
        for i in range(0, 3):
            oFailure = junit.failure('Type' + str(i))
            for j in range(0, 3):
                oFailure.add_text('Text_' + str(i) + '_' + str(j))
            oTestcase.add_failure(oFailure)
        dExpected = []
        dExpected.append('    <testcase name="Name" time="Time" classname="Classname">')
        dExpected.append('      <failure type="Type0">')
        dExpected.append('        Text_0_0')
        dExpected.append('        Text_0_1')
        dExpected.append('        Text_0_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type1">')
        dExpected.append('        Text_1_0')
        dExpected.append('        Text_1_1')
        dExpected.append('        Text_1_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type2">')
        dExpected.append('        Text_2_0')
        dExpected.append('        Text_2_1')
        dExpected.append('        Text_2_2')
        dExpected.append('      </failure>')
        dExpected.append('    </testcase>')
        self.assertEqual(dExpected, oTestcase.build_junit())

    def test_testsuite_class_attributes(self):
        oTestsuite = junit.testsuite('Name', 'Time')
        self.assertTrue(oTestsuite)
        self.assertEqual(oTestsuite.name, 'Name')
        self.assertEqual(oTestsuite.time, 'Time')
        self.assertEqual(oTestsuite.testcases, None)

    def test_testsuite_class_add_testcase(self):
        oTestsuite= junit.testsuite('Name', 'Time')
        oTestsuite.add_testcase(junit.testcase('TC_Name0', 'TC_Time0', 'TC_Classname0'))
        oTestsuite.add_testcase(junit.testcase('TC_Name1', 'TC_Time1', 'TC_Classname1'))
        oTestsuite.add_testcase(junit.testcase('TC_Name2', 'TC_Time2', 'TC_Classname2'))
        self.assertEqual(oTestsuite.testcases[0].name, 'TC_Name0')
        self.assertEqual(oTestsuite.testcases[1].name, 'TC_Name1')
        self.assertEqual(oTestsuite.testcases[2].name, 'TC_Name2')

    def test_testsuite_class_build_junit(self):
        oTestsuite = junit.testsuite('Name', 'Time')
        for k in range(0, 3):
            oTestcase = junit.testcase('Name' + str(k), 'Time' + str(k), 'Classname' + str(k))
            for i in range(0, 3):
                oFailure = junit.failure('Type' + str(i))
                for j in range(0, 3):
                    oFailure.add_text('Text_' + str(i) + '_' + str(j))
                oTestcase.add_failure(oFailure)
            oTestsuite.add_testcase(oTestcase)
        
        dExpected = []
        dExpected.append('  <testsuite>')
        dExpected.append('    <properties>')
        dExpected.append('    </properties>')
        dExpected.append('    <testcase name="Name0" time="Time0" classname="Classname0">')
        dExpected.append('      <failure type="Type0">')
        dExpected.append('        Text_0_0')
        dExpected.append('        Text_0_1')
        dExpected.append('        Text_0_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type1">')
        dExpected.append('        Text_1_0')
        dExpected.append('        Text_1_1')
        dExpected.append('        Text_1_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type2">')
        dExpected.append('        Text_2_0')
        dExpected.append('        Text_2_1')
        dExpected.append('        Text_2_2')
        dExpected.append('      </failure>')
        dExpected.append('    </testcase>')
        dExpected.append('    <testcase name="Name1" time="Time1" classname="Classname1">')
        dExpected.append('      <failure type="Type0">')
        dExpected.append('        Text_0_0')
        dExpected.append('        Text_0_1')
        dExpected.append('        Text_0_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type1">')
        dExpected.append('        Text_1_0')
        dExpected.append('        Text_1_1')
        dExpected.append('        Text_1_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type2">')
        dExpected.append('        Text_2_0')
        dExpected.append('        Text_2_1')
        dExpected.append('        Text_2_2')
        dExpected.append('      </failure>')
        dExpected.append('    </testcase>')
        dExpected.append('    <testcase name="Name2" time="Time2" classname="Classname2">')
        dExpected.append('      <failure type="Type0">')
        dExpected.append('        Text_0_0')
        dExpected.append('        Text_0_1')
        dExpected.append('        Text_0_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type1">')
        dExpected.append('        Text_1_0')
        dExpected.append('        Text_1_1')
        dExpected.append('        Text_1_2')
        dExpected.append('      </failure>')
        dExpected.append('      <failure type="Type2">')
        dExpected.append('        Text_2_0')
        dExpected.append('        Text_2_1')
        dExpected.append('        Text_2_2')
        dExpected.append('      </failure>')
        dExpected.append('    </testcase>')
        dExpected.append('    <system-out>')
        dExpected.append('    </system-out>')
        dExpected.append('    <system-err>')
        dExpected.append('    </system-err>')
        dExpected.append('  </testsuite>')
        self.assertEqual(dExpected, oTestsuite.build_junit())
