import pefile

if __name__ == '__main__':
    pe = pefile.PE(r'C:\Users\silyi\Downloads\file.exe')  # Путь к исполняемому файлу

    print(f'\n{pe.DOS_HEADER}')  # Выводим основные поля заголовка DOSHeader
    print(f'\n{pe.FILE_HEADER}')  # Выводим основные поля заголовка FileHeader
    print(f'\n{pe.OPTIONAL_HEADER}')  # Выводим основные поля заголовка OptionalHeader

    # Вывод таблиц директорий
    print("\nData directories:")
    for data_directory in pe.OPTIONAL_HEADER.DATA_DIRECTORY:
        print('\t' + data_directory.name)

    # Вывод основных полей заголовков SectionHeader
    print(f'\n{pe.sections[0]}')

    # Вывод сведений об импорте исполняемого файла
    print("\nListing imports:\n")
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print('\t' + entry.dll.decode('utf-8'))
