import  json
data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()

    if word in data:
        return(data[word])
    else:
        return("invalid")

word = print("enter the text  you want to search")
word=input()
output=meaning(word)
if type(output)==list:
    for i in output:
        print(i)
