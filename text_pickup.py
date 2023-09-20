import os
import re
from google.colab import drive
drive.mount('/content/drive')
# テキストファイルのパスを指定します
text_file_path = '/content/drive/MyDrive/siri_choice/Pre_Finished/okinawa_mix_highpass_output.txt'

# 抽出したいワードのリストを指定します
target_words = ['heysiri', 'google', 'ありがとう', 'やめる', 'タイマー', '予定', '電話', 'ストップ', '終わる', 'へいしり', '５分', 'Google', '天気']

# ファイルを読み取りモードで開きます
with open(text_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# テキストファイルから特定のワードに引っ掛かりそうなワードを抽出し、音声ファイル名も抜き出します
matches = []
for line in lines:
    for word in target_words:
        if re.search(word, line):
            audio_filename = line.split(':')[0]
            matches.append(f'{audio_filename}:{line.strip()}')

# 抽出結果を出力するテキストファイルのパスを指定します
output_file_path = '/content/drive/MyDrive/siri_choice/word_choose/okinawa_mix3_word_choose.txt'

# 抽出結果をテキストファイルに書き込みます
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(matches))
