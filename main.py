print("Hello world!")

def pigLatin(phrase):
    out = []
    for word in phrase.split(' '):
        if word[0].lower() in 'aeiou':
            out.append(word + 'yay')
        else:
            out.append(word[1:] + word[0] + 'ay')
    return ' '.join(out)

print(pigLatin('This is a sentence'.split()))