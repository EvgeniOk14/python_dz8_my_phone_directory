import os
from data_create_file import id_number, name_data, surname_data, phone_data, adress_data

def input_data():
    print('Введите данные для записи в файл:\n ')
    id = id_number()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()

    with open('file_name.txt','a', encoding = 'utf-8') as file:
        file.write(f'{id}; {name }; {surname }; {phone}; {adress}; \n')
        

def print_data():
    if os.path.exists('file_name.txt'):
        print('Вывод данных из файла:\n ')
        with open('file_name.txt', 'r', encoding = 'utf-8') as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print('Файла не существует!!! ')



def filter_data(filter_string):
    with open('file_name.txt', 'r', encoding = 'utf-8') as file:
        list_data = file.readlines()
        if '; ' in filter_string:
            list_filter = filter_string.split('; ')
        else:
            list_filter = [filter_string]

        is_found = False

        for element in list_data:    # данные из файла записаны в list_data
            temp_record = element.split('; ') # записываем первую из list_data 
                                              #запись через ; в temp_record
            #count = 0
            for record in temp_record: # идём по элементам первой записи из файла
                for element_filter in list_filter: # идём по элементам запроса пользователя
                    if element_filter.lower() in record.lower() and len(element_filter.lower())==len(record.lower()):
                        print(element)
                        #count+=1
                        is_found = True
                # if count == len(list_filter):
                #         #print(element) 
                #         is_found= True
        if is_found == False:                   
            print('Таких записей как: ', element_filter,' нет ')

        

def delete_data(delete_string):
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        list_data = file.readlines()

        Flag = False

        for line_i in range(len(list_data)):
            if Flag: 
                break

            record_list_data = list_data[line_i].split('; ')
            for element in range(len(record_list_data)):
                if delete_string in record_list_data[element]:
                    del record_list_data[element]

                    new_line = '; '.join(record_list_data)
                    list_data[line_i] = new_line
                    Flag = True
                    break

    with open('file_name.txt', 'w', encoding='utf-8') as file:
        for line in list_data:
            file.write(line + '\n')
    print('Введённый Вами элемент успешно удалён! Для просмотра результата запустите программу снова! ')



def swap_value(old_value, new_value):
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        Flag = False

        for line_i in range(len(list_data)):
            if Flag: break

            record_list_data = list_data[line_i].split('; ')
            for element in range(len(record_list_data)):
                if  old_value in record_list_data[element]:
                    record_list_data[element] = new_value

                    new_line = '; '.join(record_list_data)
                    list_data[line_i] = new_line
                    Flag = True
                    break

        with open('file_name.txt', 'w', encoding='utf-8') as file:
            for line in list_data:
                file.write(line + '\n')           
        print('Введённый Вами элемент успешно заменён! Для просмотра результата запустите программу снова! ')

        


    


