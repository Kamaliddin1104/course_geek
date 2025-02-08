"""
В будущем придётся работать с байтами.
Например: когда нужно работать с Mp3 jpeg или png
ибо когда нужно передавать информацию по сети нужно
конвертировать данные в байты и работать с ними
"""
eng_text, rus_text = 'Hello world!', 'Привет мир!'
rus_byte, eng_byte = rus_text.encode('utf-8'), eng_text.encode()
print(rus_byte, eng_byte)


# Поочерёдное записывание большой информации в файл с использованием
# генератора, чтобы не нагружать память
def copy_large_file(src, dest, chunk_size=1024):
    with open(src, "rb") as f_src, open(dest, "wb") as f_dest:
        for chunk in iter(lambda: f_src.read(chunk_size), b""):
            f_dest.write(chunk)

# Использование
copy_large_file("Скороговорка_лигурия.txt", "destination.txt")

