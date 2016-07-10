from Tkinter import*
import Tkinter as ttk

# Pig Latin helper function
    """Returns the (simplified) Pig Latin version of the word.
        a made-up language formed from English by transferring the initial consonant
        or consonant cluster of each word to the end of the word and adding a vocalic
        syllable (usually ˈpiɡ ˌlatn: so chicken soup would be translated to
        ickenchay oupsay . Pig Latin is typically spoken playfully, as if to convey secrecy.
    """

def pig_latin(word):
      first_letter = word[0], [a], [e], [i], [u]
      rest_of_word = word[1 : ]
