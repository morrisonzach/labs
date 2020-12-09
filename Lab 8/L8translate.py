#
#   purpose: translate between pig latin and english
#   author: zachary morrison
#   date written: 12/01/2020
#   Version: 1.0.0
#

#   creating constants
VOWELS = ("a", "e", "i", "o", "u")
CONSONANT = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
             "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")

#   class will handle translating between Piglatin and English


class Translator:
    def __init__(self):
        self.languages = ("english", "piglatin")
        self.__start()

    #   runs when the class is initialized
    def __start(self):
        print("Piglatin and English Translator")
        print("===============================\n===============================\n\n")
        print("This translator lets the user\nchoose between Piglatin and\nEnglish then translates the\ninputted sentence.\n\n")
        #   starts the translate method using the get_language function as the argument
        print(self.translate(self.get_language()))

    #   gets user input to decide what language the program will be translating from
    def get_language(self):
        lang = str(input(
            "what language are you going to be translating today? [P(iglatin) or E(nglish)] ")).lower()
        if lang == "e" or lang == self.__languages[0]:
            return self.languages[0]
        elif lang == "p" or lang == self.__languages[1]:
            return self.languages[1]
        else:
            print("sorry it looks like that isn't a valid input! try again\n")
            return self.get_language()

    #   translates the provided string from english to piglatin or vice versa
    def translate(self, lang):
        sentence = str(input(
            "enter the " + str(lang) + " sentence that you would like to translate: "))
        words = sentence.lower().split(" ")
        sentence = ""
        for word in words:
            if word[0] in VOWELS:
                copy = word + "yay"
                word = (copy + ".")[:-1]
                sentence += word + " "
            if word[0] in CONSONANT:
                copy = word[1:] + word[0] + "ay"
                word = (copy + ".")[:-1]
                sentence += word + " "

        return sentence


#   object instance
translator = Translator()
