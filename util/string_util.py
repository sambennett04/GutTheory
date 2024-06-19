from typing import List

#class that enables list and string cleaning functionality to be used in food_analyzer and food_classifier 
#in its own module so that, through its init file, it can be connected to the food_analyzer and food_classifier moduals and have its functionality imported into them
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