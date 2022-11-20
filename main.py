from rotator import word_rotator_core as r_func

# print(r_func(input("Enter a sentence or a word: ")))


# TODO throwing exception in word_rotator_core() method
# TODO capital letter detector
# TODO cyclic input from the CLI (prompt: ri| )
# TODO redirect i/o from/to file.txt
data_results = []

with open("input_test_files.txt", encoding='utf-8') as data_rotator:
    for item in data_rotator.readlines():
        line_string = str(item)
        data_results.append(r_func(line_string)+'\n')

print(data_results)

with open("output_file.txt", 'w+', encoding='utf-8') as output:
    output.write(''.join([str(item) for item in data_results]))
