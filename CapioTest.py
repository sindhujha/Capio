import unittest
import os
import Capio
import json
import ast
import pprint
class TestCapio(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_fetch_from_api(self):
        status,response = Capio.fetch_from_api("https://api.capio.ai/v1/speech/transcript/", "",
                                        "262ac9a0c9ba4d179aad4c0b9b02120a")

        self.assertEqual(status, "error")
        self.assertEqual(response,"Invalid response")
        status,response = Capio.fetch_from_api("https://api.capio.ai/v1/speech/transcript/", "593f237fbcae700012ba8fcd",
                                        "")
        self.assertEqual(status, "error")

        status,response = Capio.fetch_from_api("https://api.capio.ai/v1/speech/transcript/", "593f237fbcae700012ba8fcd",
                                        "262ac9a0c9ba4d179aad4c0b9b02120a")
        self.assertEqual(status, "success")

    def test_parse_json(self):
        json_str = '[{u"result": [{u"alternative": [{u"confidence": 1,u"transcript": u"um",u"words": [{u"confidence": 1,u"from": 0.6899999976158142,u"to": 1.2899999618530273,u"word": u"um"}]}],u"final": True}],u"result_index": 0}]'
        json_data = ast.literal_eval(json_str)
        Capio.parse_json(json_data,"ParseJsonOutput.docx")
        print'success'

    def tearDown(self): 
        if os.path.exists("ParseJsonOutput.docx"):
            os.remove("ParseJsonOutput.docx")



if __name__ == '__main__':
    unittest.main()
