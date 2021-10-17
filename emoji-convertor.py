def emoji_convertor():
    emoji_dictionary = {
        "happy": "😀",
        "sad": "😐",
        "excited": "🤓",
    }
    messages_list = message.split()
    output = ""
    for words in messages_list:
        output = output + emoji_dictionary.get(words, words) + " "
    print(output)


message = input("> ")
emoji_convertor()