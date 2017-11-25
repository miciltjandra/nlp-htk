import os

monophones = []

def add_to_monophones(phone):
    if phone not in monophones:
        monophones.append(phone)

def f(x):
    return {
        'ai': 'ai',
        'au': 'au',
        'kh': 'kh',
        'ng': 'ng',
        'ny': 'ny',
        'oi': 'oi',
        'sy': 'sy',
        'dj': 'j',
        'ch': 'h'
    }.get(x, 'a')

def transform_to_phonem(word):
    phonems = ""
    idx = 0
    while idx < len(word):
        if idx+1 < len(word):
            phone = f(word[idx:idx+2])
            if phone != 'a':
                phonems += phone + ' '
                add_to_monophones(phone)
                idx += 1
            else:
                if word[idx] == 'v':
                    phonems += 'f '
                    add_to_monophones('f')
                elif word[idx] == 'q':
                    phonems += 'k '
                    add_to_monophones('k')
                elif word[idx] == 'x':
                    if idx == 0:
                        phonems += 's '
                        add_to_monophones('s')
                    else:
                        phonems += 'k s '
                        add_to_monophones('k')
                        add_to_monophones('s')
                elif word[idx] == '-' or word[idx] == '\'':
                    phonems += ''
                else:
                    phonems += word[idx] + ' '
                    add_to_monophones(word[idx])
        else:
            if word[idx] == 'v':
                phonems += 'f '
                add_to_monophones('f')
            elif word[idx] == 'q':
                phonems += 'k '
                add_to_monophones('k')
            elif word[idx] == 'x':
                if idx == 0:
                    phonems += 's '
                    add_to_monophones('s')
                else:
                    phonems += 'k s '
                    add_to_monophones('k')
                    add_to_monophones('s')
            elif word[idx] == '-' or word[idx] == '\'':
                phonems += ''
            else:
                phonems += word[idx] + ' '
                add_to_monophones(word[idx])
        idx += 1
    return phonems

write_list = []
read_list = {}

with open('all_set_clean.txt','r') as myfile:
    text = myfile.read()
    arr = text.split('\n')
    for line in arr:
        write = line.split('\t')[0]
        read = line.split('\t')[1]
        write_words = write.split(' ')
        read_words = read.split(' ')
        if len(write_words) == len(read_words):
            idx = 0
            for word in write_words:
                if word not in write_list:
                    write_list.append(word)
                    read_list[word] = read_words[idx]
                idx += 1
        else:
            print(write_words)
            print(read_words)

# print(read_list)

out = open('dict', 'w')

with open('wordlist') as myfile:
    text = myfile.read()
    arr = text.split('\n')
    for line in arr:
        out.write(line)
        out.write('\t')
        out.write(transform_to_phonem(read_list[line]))
        out.write('\n')

out.close()

out = open('monophones0', 'w')
for phone in monophones:
    out.write(phone)
    out.write('\n')

out.close()