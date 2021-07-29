import os
from operator import itemgetter


def get_a_list_of_text_files():
    folder_path = os.getcwd()
    path_to_text_files = f"{folder_path}/files"

    all_files_in_dir = os.listdir(path_to_text_files)
    list_of_text_files = []
    for file in all_files_in_dir:
        if file.endswith(".txt"):
            list_of_text_files.append(file)

    return list_of_text_files

def get_final_file():
    folder_path = os.getcwd()
    path_to_text_files = f"{folder_path}/files/"
    list_of_text_files = get_a_list_of_text_files()

    list_for_counting_text_files = []
    for file_txt in list_of_text_files:
        with open(path_to_text_files + file_txt, "r", encoding="utf-8") as file:
            data_file = path_to_text_files + file_txt
            line_count = 0
            for line in file:
                line_count += 1
            dict_file_txt = {'count': None, 'data': data_file, 'file_name': file_txt}
            dict_file_txt['count'] = line_count
            dict_file_txt['data'] = path_to_text_files + file_txt
            dict_file_txt['file_name'] = file_txt
            list_for_counting_text_files.append(dict_file_txt)

    sort_files = sorted(list_for_counting_text_files, key=itemgetter('count'))

    for data_file in sort_files:
        number_of_lines = data_file['count']
        file_path = data_file['data']
        file_name = data_file['file_name']
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()
            with open("final_file.txt", "a", encoding="utf-8") as file:
                file.write(f"{file_name}\n{number_of_lines}\n{file_contents}\n")

    with open("final_file.txt", "r", encoding="utf-8") as file:
        final_file = file.read()

    return print(final_file)


get_final_file()