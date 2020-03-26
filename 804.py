class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_list=[]
        for word in words:
            morse=""
            for char in word:
                morse=morse+(m[(ord(char)-97)])
            if morse not in morse_list:
                morse_list.append(morse)
        return len(morse_list)
