# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

with open('RLE.txt', 'r') as f:
    lines = f.readlines()
with open('RLE1.txt', 'w') as f1:
    lines = f1.readlines()

def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: return '' 
    for char in data: 
        if char != prev_char:
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding

encode_value = rle_encode('AAAAASSSSSBBBBBBEEEEEDDDDZZZZ')
print(encode_value)