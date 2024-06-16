from typing import List

class StringUtil(object):

    @staticmethod
    def clean_string(input:str) -> str:
        cleaned = input.strip()
        cleaned = cleaned.upper()
        return cleaned
    
    @staticmethod
    def clean_list(input:List[str]) -> List[str]:
        cleaned = [StringUtil.clean_string(s) for s in input]
        return cleaned