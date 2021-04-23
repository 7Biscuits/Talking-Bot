import random
import pyttsx3

user_text = ["Text", "text", "TEXT"]

user_speak = ["Speak", "speak", "SPEAK"]

greeting = ['hi', 'hello', 'wassup', 'hey', 'hey there']

user_bye = ['bye', 'cya', 'talk to you later']

swears = ["Fuck","fuck","bitch","Bitch","Asshole","Mother fucker","asshole","mother fucker","mother Fucker","son of a bitch","Son of a bitch"]

responses = ['ok', 'fine', 'yes for sure', 'i see', 'yes lol', 'haha lol','It is certain.',
                'Without a doubt.',
                'You may rely on it.',
                'Yes definitely.',
                'It is decidedly so.',
                'As I see it, yes.',
                'Most likely.',
                'Yes.',
                'Outlook good.',
                'Signs point to yes Neutral Answers.',
                'nope.',
                'no.',
                'never.',
                'maybe.',
                'probably.',
                'probably not.',
                'could be.',
                'sounds good', 'kinda', 'oh', 'i see']

swear_respond = ["Hey don't swear pls", "Yo don't use these words pls"]

def main():
    def user_ask_function():
        user_ask = input("Do you want me to speak or reply in text: ")
        return user_ask

    user_ask_response = user_ask_function()

    if user_ask_response in user_text:
        
        def user_prompt():
            while True:
                inp_ = input('Type: ')
                if inp_ in greeting:
                    print(random.choice(greeting))

                elif inp_ in user_bye:
                    print(random.choice(user_bye))

                elif inp_ in swears:
                    print(random.choice(swear_respond))

                elif inp_ == 'end':
                    break

                else:
                    print(random.choice(responses))

        user_prompt()

    elif user_ask_response in user_speak:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0])

        def speak(audio):
            engine.say(audio)
            engine.runAndWait

        def user_speak_prompt():
            while True:
                inp = input('Type: ')
                if inp in greeting:
                    speak(random.choice(greeting))

                elif inp in user_bye:
                    speak(random.choice(user_bye))

                elif inp in swears:
                    speak(random.choice(swear_respond))

                elif inp == "end":
                    break

                else:
                    speak(random.choice(responses))

        user_speak_prompt()

    else:
        while True:
            print("Invalid Input")
            user_ask_valid = input("Do you want to try again? ")
            if user_ask_valid == "yes":
                main()

            elif user_ask_valid == "no":
                break

main()
