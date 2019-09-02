import os #For Clearing Lines

#These set of variables are to specify a place for each part of speech
#in the world list and to prompt the user with a phrase to enter.
#Reference for list method and modified main() https://github.com/noltron000/mad-libs/blob/master/mad-libs.py
noun = '> Enter a Noun\n'
noun2 = '> Enter a Noun\n'
propnoun = '>Enter a Proper Noun\n'
verb = '> Enter a Verb\n'
verb2 = '> Enter a Verb\n'
adjective = '>Enter an adjective\n'

#Introduction to the game
intro = 'Welcome to Mad Libs\nWhen prompted for a word type it and press enter.\n'

#Putting in place each word in the list to be replaced later.
wordlist = [noun, verb, adjective, propnoun, verb2, noun2]

#Prompts user for input and returns value
def user_input(prompt):
    response = input(prompt)
    return response

#Lists through wordlist and prints out each one. Then continues until the end
#of the list and replaces each one with the users input.
def main():
    counter = 0
    for word in wordlist:
        wordlist[counter] = user_input(wordlist[counter])
        counter += 1
    os.system('clear')

print(intro)
main()

#Story for the game, fills with words inputed into wordlist
story = f'''
    You find yourself lost and the first thing you see is a
    {wordlist[0]}. You consider touching the {wordlist[0]}
    however you {wordlist[1]} away when you see it start to transform.
    The {wordlist[2]} object is morphing into {wordlist[3]},
    your worst fear. You run and {wordlist[4]} but there is nowhere
    to go in the void you find yourself in.  The last thing you see before
    it consumes you is a {wordlist[5]}. You are relieved now.\n'''

print(story)
