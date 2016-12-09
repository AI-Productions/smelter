import Smelter

smelter = Smelter.Smelter()

print("There are {} words in the whitelist".format(smelter.number_of_whitelisted_words()))  # There are 3499 words in the whitelist

print(smelter.filter_sentence("I am a human."))  # I am a human.

print(smelter.filter_sentence("You suck."))  # You heck
