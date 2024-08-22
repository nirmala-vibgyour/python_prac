def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!!"
    print(msg)

if __name__ == '__main__':

    # Parser for command-line options, arguments and sub-commands
    # generic operating system services

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument("-n", "--name", metavar="name", required=True, help="True name of the person to greet.")

    parser.add_argument("-l", "--lang", metavar="language", required=True, choices=["English","Spanish","German"], \
                        help="The of langugae of greeting.")
    
    args = parser.parse_args()

    hello(args.name, args.lang)
