import pandas as pd


def clean_reddit_data(file_name, text_column='body'):
    print(f"Починаємо очищення файлу: {file_name}...")

    # Зчитуємо CSV файл
    df = pd.read_csv(
        file_name,
        low_memory=False,  # Завантажує колонки цілком, усуваючи DtypeWarning
        lineterminator='\n',  # Коректно обробляє коментарі, що містять кілька абзаців
        on_bad_lines='skip',  # Ігнорує зламані рядки у CSV замість зупинки скрипта
        encoding='utf-8',  # Запобігає помилкам кодування через емодзі чи спецсимволи
        engine='c'
    )
    # Перевіряємо, чи є колонка 'author' (автор)
    if 'author' in df.columns:
        # Шукаємо 'bot' в імені користувача (без урахування великих/малих літер)
        is_bot_name = df['author'].str.contains('bot', case=False, na=False)

        # Точні збіги для відомих ботів, які не мають слова 'bot' у назві
        known_bots = ['AutoModerator', 'transcribersofreddit']
        is_known_bot = df['author'].isin(known_bots)
    else:
        is_bot_name = False
        is_known_bot = False

    # Перевіряємо, чи є колонка з текстом
    if text_column in df.columns:
        # Список типових фраз, які залишають боти
        bot_phrases = [
            'I am a bot, and this action was performed automatically',
            'beep boop',
            'Good bot',
            'Bad bot',
            'automated response'
        ]
        # Об'єднуємо фрази у регулярний вираз (АБО)
        bot_pattern = '|'.join(bot_phrases)

        # Шукаємо ці фрази у тексті
        is_bot_text = df[text_column].str.contains(bot_pattern, case=False, na=False)
    else:
        is_bot_text = False

    # Об'єднуємо всі умови: якщо хоча б одна з них True, вважаємо рядком бота
    all_bots = is_bot_name | is_known_bot | is_bot_text

    # Залишаємо лише ті рядки, де all_bots є False (не боти)
    df_clean = df[~all_bots]

    # Зберігаємо очищений датасет у новий файл
    clean_file_name = f"cleaned_{file_name}"
    df_clean.to_csv(clean_file_name, index=False)

    # Виводимо результати
    bots_removed = len(df) - len(df_clean)
    print(f"Готово! Видалено {bots_removed} записів від ботів.")
    print(f"Очищені дані збережено у файл: {clean_file_name}\n")


if __name__ == "__main__":
    # Очищення коментарів (зазвичай текст зберігається у колонці 'body')
    # Замініть 'body', якщо ваша колонка з текстом називається інакше у combined_reddit_comments.csv
    clean_reddit_data('combined_reddit_comments.csv', text_column='body')

    # Очищення постів (зазвичай текст зберігається у колонці 'selftext' або 'title')
    # Замініть 'selftext', якщо колонка називається інакше у combined_reddit_submissions.csv
    clean_reddit_data('combined_reddit_submissions.csv', text_column='selftext')