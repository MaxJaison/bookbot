def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words_count = count_words(file_contents)
        counted_letters = count_letters(file_contents)
        report_list = make_report(counted_letters)
        print_report(words_count, report_list)

def count_words(file_contents):
        words = file_contents.split()
        return len(words)

def count_letters(file_contents):
    dict = {}
    words = file_contents.lower().split()
    for word in words:
        for letter in word:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1    
    return dict

def make_report(dict):
    report_list = []
    for item in dict:
        if item.isalpha():
            report_list.append({"name": item, "num": dict[item]})
    report_list.sort(reverse=True, key=sort_on)    
    return report_list   

def sort_on(dict):
    return dict["num"]

def print_report(words_count, report_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    for char in report_list:
        print(f"The {char["name"]} character was found {char["num"]} times")
    print("--- End report ---")    

main()
