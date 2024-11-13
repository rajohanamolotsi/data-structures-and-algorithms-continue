from hashtable import Hashtable

def get_words_array(file):
    words = []
    with open(file, 'r') as f:
        for line in f:
            tokens = line.split(' ')
            if tokens == ['\n']:
                continue
            words += tokens # token.strip('.,;:\n!')

    words = [word.strip('.,;:\n!') for word in words]
    return words

def array_to_dict(words):
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

if __name__ == '__main__':
    t = Hashtable()
    file = 'poem.txt'
    words = get_words_array(file)
    word_count = array_to_dict(words)

    for word in word_count.items():
        t[word[0]] = word[1]

    print(f'diverged: {t['diverged']}')
    print(f'in: {t['in']}')
    print(f'I: {t['I']}')