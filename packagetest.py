from rpg_dice import roll
import emoji
from text_generator import generate

print("testing rpg dice")
testRoll = roll("2d6")
print("this is the dice roll ")
print(testRoll)

print(emoji.emojize('testing emoji package :thumbsup: I think it works :smile:', use_aliases=True))

print("testing random text generator")
code = generate()
print(f"Generated code is -> {code}")