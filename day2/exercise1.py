# 1
print("Hello World"[8])

# 2
print("thinker"[2:5])

# 3
    # s="hello" // s[1] would output "e"
    # s="Sammy" // s[2:] would output "mmy"

# 4
def chars(word):
    for char in word:
        print(char)

chars("Mississippi")
    
# 5
def palindrome():
    output = ""
    results = []
    ignored_chars = "!.,'?"
    num = input("How many phrase would you like to test? ")
    for x in range(0, int(num)):
        phrase = input("Phrase: ")    
        phrase = phrase.lower().replace(" ", "")
        
        for char in ignored_chars:
            phrase = phrase.replace(char, "")
        
        results.append("Y") if phrase == phrase[::-1] else results.append("N")

    for x in results:
        output += f"{x} "
    
    print(output)
    
palindrome()