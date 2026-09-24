import pandas as pd
import glob
import os

# Вкажи шлях до папки з файлами
folder_path = r'C:\Users\Admin\Desktop\CSS\data ai'

# Визначаємо розширення файлів (зміни на '.xlsx', якщо це формат Excel)
file_extension = '*.csv'


def combine_reddit_data(prefix, output_filename):
    # Шукаємо файли з відповідним префіксом (RS_ або RC_) та сортуємо їх
    # Сортування за алфавітом автоматично дасть хронологічний порядок
    search_pattern = os.path.join(folder_path, f'{prefix}_{file_extension}')
    file_list = sorted(glob.glob(search_pattern))

    if not file_list:
        print(f"Файлів з префіксом {prefix} не знайдено.")
        return

    print(f"Об'єднання {len(file_list)} файлів для {prefix}...")

    # Зчитуємо файли. Якщо це дійсно .xlsx, заміни pd.read_csv на pd.read_excel
    dataframes = [pd.read_csv(file, low_memory=False) for file in file_list]

    # Зводимо в один датасет і скидаємо індекси
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Зберігаємо результат
    # Якщо потрібно зберегти в Excel, використовуй .to_excel(output_filename, index=False)
    combined_df.to_csv(output_filename, index=False)
    print(f"Збережено у {output_filename}\n")


# Спочатку об'єднуємо публікації (RS)
combine_reddit_data('RS', 'combined_reddit_submissions.csv')

# Потім об'єднуємо коментарі (RC)
combine_reddit_data('RC', 'combined_reddit_comments.csv')
