import pytest
from ..util.string_util import StringUtil

class TestStringUtil:

    def test_clean_string(self):
        input = "  xyz  "
        cleaned = StringUtil.clean_string(input=input)
        assert cleaned == "XYZ"
    
    def test_clean_list(self):
        input = [" xyz  ", "abc ", " DeF"]
        cleaned = StringUtil.clean_list(input=input)
        assert cleaned[0] == "XYZ"
        assert cleaned[1] == "ABC"
        assert cleaned[2] == "DEF"