import pyttsx3

if __name__ == '__main__':
    print("hello welcome to robo speaker 1.1")
    x = input("enter what you want to say:")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Convert the text to speech
    engine.say(x)

    # Wait for the speech to finish
    engine.runAndWait()
