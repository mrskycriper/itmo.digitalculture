import re


def Levrnsthein_range(current_word_for_fix, current_word_from_dictionary):
    len_fix_word, len_dict_word = len(current_word_for_fix), len(current_word_from_dictionary)
    if len_fix_word > len_dict_word:
        current_word_for_fix, current_word_from_dictionary = current_word_from_dictionary, current_word_for_fix
        len_fix_word, len_dict_word = len_dict_word, len_fix_word

    current_row = range(len_fix_word + 1)

    for i in range(1, len_dict_word + 1):
        previous_row, current_row = current_row, [i] + [0] * len_fix_word
        for j in range(1, len_fix_word + 1):
            add_symbol, delete_symbol, change_symbol = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if current_word_for_fix[j - 1] != current_word_from_dictionary[i - 1]:
                change_symbol += 1
            current_row[j] = min(add_symbol, delete_symbol, change_symbol)

    return current_row[len_fix_word]


wrong_words = []
unic_words = []
counter = 0

output_file = open("out.txt", 'w', encoding='WINDOWS-1251')
dict_file = open("dict1.txt", 'r', encoding='WINDOWS-1251')
input_file = open("brain042.txt", 'r', encoding='WINDOWS-1251')

input_string = input_file.read()
dict_string = dict_file.read()

input_string = re.sub(r'\n', ' ', input_string)
dict_string = re.sub(r'\n', '  ', dict_string)

words = input_string.split()
dict1 = dict_string.split("  ")

for i in range(0, len(words)):
    words[i] = re.sub(r'[,!();:«»]', '', words[i])
    words[i] = words[i].replace('.', '')
    words[i] = words[i].replace('.', '')
    words[i] = words[i].replace('?', '')
    words[i] = words[i].lower()

for i in range(0, len(words)):
    if unic_words.count(words[i]) == 0:
        unic_words.append(words[i])

for i in range(0, len(unic_words)):
    counter_tmp = counter
    for j in range(0, len(dict1)):
        dict_line = dict1[j].partition(" ")
        if unic_words[i] == dict_line[0]:
            counter += 1
    if counter == counter_tmp:
        wrong_words.append(unic_words[i])

output_string = input_string

for i in range(0, len(wrong_words)):
    replacer = "не найдено"
    min_range = ">2"
    for j in range(0, len(dict1)):
        dict_line = dict1[j].partition(" ")
        if Levrnsthein_range(wrong_words[i], dict_line[0]) == 1:
            if min_range == "2" or min_range == ">2":
                replacer = dict_line[0]
                min_range = "1"
            break
        if Levrnsthein_range(wrong_words[i], dict_line[0]) == 2:
            if min_range == ">2":
                replacer = dict_line[0]
                min_range = "2"
    if replacer != "не найдено":
        output_string = output_string.replace(wrong_words[i], replacer)
    print(wrong_words[i], "-", replacer, "-", min_range)


output_file.write(output_string)


print("До исправления ошибок:")
print("Словоформ в тексте:", len(words))
print("Уникальных словоформ в тексте:", len(unic_words))
print("Уникальных словоформ из словаря в тексте:", counter)
print("Количество потенциальных ошибок:", len(unic_words) - counter)

wrong_words_corrected = []
unic_words_corrected = []
counter_corrected = 0
words_corrected = output_string.split()
for i in range(0, len(words_corrected)):
    words_corrected[i] = re.sub(r'[,!();:«»]', '', words_corrected[i])
    words_corrected[i] = words_corrected[i].replace('.', '')
    words_corrected[i] = words_corrected[i].replace('.', '')
    words_corrected[i] = words_corrected[i].replace('?', '')
    words_corrected[i] = words_corrected[i].lower()

for i in range(0, len(words_corrected)):
    if unic_words_corrected.count(words_corrected[i]) == 0:
        unic_words_corrected.append(words_corrected[i])

for i in range(0, len(unic_words_corrected)):
    counter_corrected_tmp = counter_corrected
    for j in range(0, len(dict1)):
        dict_line = dict1[j].partition(" ")
        if unic_words_corrected[i] == dict_line[0]:
            counter_corrected += 1
    if counter == counter_corrected_tmp:
        wrong_words_corrected.append(unic_words_corrected[i])


print("После исправления ошибок:")
print("Словоформ в тексте:", len(words_corrected))
print("Уникальных словоформ в тексте:", len(unic_words_corrected))
print("Уникальных словоформ из словаря в тексте:", len(unic_words_corrected) - counter_corrected)

dict_file.close()
input_file.close()
output_file.close()
