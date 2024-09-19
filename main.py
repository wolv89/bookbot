
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
        chars = {}
        for c in file_contents:
            if not c.isalpha():
                continue
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
        list = []
        for c in chars:
            list.append({"char": c, "count": chars[c]})
        
        list.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        print(words, " words found in the document")
        print()

        for l in list:
            print(f"The '{l['char']}' character was found {l['count']} times")
        
        print("--- End report ---")

def sort_on(dict):
    return dict["count"]

main()