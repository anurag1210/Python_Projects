import re
import collections
from PyPDF2 import PdfReader

path = '/Users/anuraggupta/Desktop/Desktop - Anurag’s MacBook Pro/Python_Projects/DailyPython/Arthashastra_of_Chanakya_-_English.pdf'
output_file = 'output_word_count.txt'


def count_words(pdf_path, output_path):
    print('Processing the PDF file and generating the word count report...')

    # Extract text from the PDF
    try:
        reader = PdfReader(pdf_path)
        all_text = ""
        for page in reader.pages:
            all_text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return

    # Find and count words
    all_words = re.findall(r"[0-9a-zA-Z-']+", all_text)
    all_words = [word.upper() for word in all_words]
    total_words = len(all_words)

    word_count = collections.Counter(all_words)
    top_20_words = word_count.most_common(20)

    # Write results to a text file
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('Word Count Analysis\n')
            file.write('===================\n\n')
            file.write(f'Total Words: {total_words}\n\n')
            file.write('Top 20 Words:\n')
            file.write('Word\tCount\n')
            file.write('----\t-----\n')
            for word, count in top_20_words:
                file.write(f'{word}\t{count}\n')
        print(f"Word count analysis saved to {output_path}")
    except Exception as e:
        print(f"Error writing to output file: {e}")


# Call the function
count_words(path, output_file)