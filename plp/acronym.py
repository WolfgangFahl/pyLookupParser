'''
Created on 2023-01-01

@author: wf
'''
import re
class Acronym:
    """
    
    helper class to check for acronyms
     
    see e.g. definition at https://www.merriam-webster.com/dictionary/acronym
        
        " ... formed from the initial letter or letters of each of the successive parts or major parts of a compound term "
        
        or https://en.wikipedia.org/wiki/Acronym
        
        "An acronym is a word or name formed from the initial components of a longer name or phrase. Acronyms are usually formed from the initial letters of words, as in NATO (North Atlantic Treaty Organization), but sometimes use syllables, as in Benelux (short for Belgium, the Netherlands, and Luxembourg). They can also be a mixture, as in radar (Radio Detection And Ranging). "
    
    """

    @classmethod
    def expand_acronym(cls,acronym:str,text:str)->str:
        """
        expand the given acronym is an acronym for the given text
        
        Args:
            acronym(str): the acronym to check
            text(str): the text to check
            
        Returns:
            str: f acronym is formed from the initial 
            letter or letters of each of the successive parts or major parts of a compound term
            return the corresponding string e.g. NATO, North Atlantic Treaty Organization -> North Atlantic Treaty Organization
        
        """
        # see https://stackoverflow.com/questions/7331462/check-if-a-string-is-a-possible-abbrevation-for-a-name
        if not text:
            return None
        words=re.findall(r"\w+",text)
        if len(acronym)<1:
            return None
        expanded=""
        delim=""
        current_index=0
        for word in words:
            # ignore acronym itself
            if word.startswith(acronym):
                continue
            firstLetter=word[0]
            current_letter=acronym[current_index]
            if firstLetter==current_letter:
                expanded=f"{expanded}{delim}{word}"
                delim=" "
                if current_index==len(acronym)-1:
                    return expanded
                else:
                    current_index+=1
        return None