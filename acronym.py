# function to create acronym
def acr(phrase):
    a = phrase.split()
    out = ''

    for i in a:
        # do not print such of word like [of, the, ...]
        if len(i) <= 3:
            continue
        else:
            out += i[0]
    return out.upper()

# output acronym
User = input('Insert Your Phrase:  ')
print(f" acronym of your phrase is : {acr(User)}")
