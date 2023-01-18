print("Hello world!")

def pigLatin(phrase):
    out = []
    for word in phrase.split(' '):
        if word[0].lower() in 'aeiou':
            out.append(word + 'yay')
        else:
            out.append(word[1:] + word[0] + 'ay')
    return ' '.join(out)

def alphabeticalSort(words):
    for i in range(len(words)):
        minWordIndex = i
        for j in range(i, len(words)):
            if words[j] < words[minWordIndex]:
                minWordIndex = j
        tmp = words[i]
        words[i] = words[minWordIndex]
        words[minWordIndex] = tmp

def main_user():
    print("Enter some words.")
    words = [i.lower() for i in pigLatin(input()).split()]
    alphabeticalSort(words)
    print("Sorted words.")
    print(words)

def main_testing():
    f = open("test.txt")
    data = ' '.join(f.read().splitlines())
    words = [i.lower() for i in pigLatin(data).split()]
    alphabeticalSort(words)

if __name__ == "__main__":
    main_testing()