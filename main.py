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
def alphabeticalSort(words):
    for i in range(len(words)):
        minWordIndex = i
        for j in range(i, len(words)):
            if words[j] < minWord:
                minWordIndex = j
        tmp = words[i]
        words[i] = words[minWordIndex]
        words[minWordIndex] = tmp
        

def main():
    print("Enter a list of words below, separated by spaces.")
    words = [pigLatin(i.lower()) for i in input.split()]
    alphabeticalSort(words)
    print("Sorted words.")
    print(words)

if __name__ == "__main__":
    main()
