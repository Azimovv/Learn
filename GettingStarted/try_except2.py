def count_word(filename, word):
    try:
        with open(filename, 'r', encoding='utf-8') as file_obj:
            counter = file_obj.read().lower().count(word)
            print("The word '{}' appears {} times".format(word, counter))
    except FileNotFoundError:
        print("Can't find the file")


filename = "dr_jekyll_mr_hyde.txt"
count_word(filename, 'the')