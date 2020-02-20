#
#      Copyright (C) 2019-2020  Edgewurth & RPCS

#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.

#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
class crossWord(param):
    def getDictionary():
        dictionaryOpen = open('/usr/share/dict/words', 'r')
        dictionary = dictionaryOpen.read().split()
        dictionaryOpen.close()
        return dictionary


    def findWord (testWord, dictionary):
        unknownCount = len(testWord)-testWord.count('?')
        for word in dictionary:
            incLetter = 0
            numMatch = 0
            # Fairly simple pattern matching atm - should prob. refactor to use regex
            if len (word) == len (testWord):
                for letter in testWord:
                    if letter == word[incLetter]:
                        numMatch += 1
                        incLetter += 1
            if numMatch == unknownCount:
                return word
            else:
            return "Not Found"
