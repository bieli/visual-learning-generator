"""
Concept from: http://www.visuallearningcenter.com/resources/

Author: Marcin Bielak <marcin.bieli@gmail.com>

Description: Only for educational/trainig reason (excluded commercial usage).
"""

import sys


from fpdf import FPDF, HTMLMixin
from random import randint


VERBOSE=True

CHARS__A_Z = [chr(character) for character in range(97, 123)]


CONTEXT_TEMPLATE = '''<p style="line-height: 1.2em;">{}</p><br /><br />
<p>Time: ________ min. ________ sec. </p><br /><br /><br />'''


class HTML2PDF(FPDF, HTMLMixin):
    pass


def gen_ascii_char(chars=CHARS__A_Z):
    return chars[randint(0, len(chars) - 1)]


def gen_world(min_chars=3, max_chars=7):
    return "".join([gen_ascii_char() for _ in range(randint(min_chars, max_chars))])


def generate_words(template, min_words=42, max_words=60, min_chars=2, max_chars=7):
    words = [remove_duplicates_from_word(gen_world(min_chars=min_chars, max_chars=max_chars)) for _ in range(randint(min_words, max_words))]
    return template.format(" ".join(words))

def remove_duplicates_from_word(word):
    return "".join(set(word))


def generate_words_with_alphabet(template, min_words=40, max_words=60, min_chars=3, max_chars=7, alphabet=CHARS__A_Z, verbose=False):
    words = []
    for letter in alphabet:
      empty_words = randint(0, 3)
      for _ in range(empty_words):
          empty_word = gen_world(min_chars=min_chars, max_chars=max_chars)
          words.append(empty_word)
          if verbose:
            print("empty word:", empty_word)

      word_without_alphabet_letter = gen_world(min_chars=min_chars, max_chars=max_chars)
      if verbose:
          print("word:", word_without_alphabet_letter)

      append_letter_on_position = randint(0, len(word_without_alphabet_letter) - 1)
      word_without_alphabet_letter_list = [char for char in word_without_alphabet_letter]
      if verbose:
          print("word_without_alphabet_letter_list:", word_without_alphabet_letter_list)
      word_without_alphabet_letter_list.insert(append_letter_on_position, letter)
      special_word = "".join(word_without_alphabet_letter_list)
      words.append(special_word)
      if verbose:
          print("============= word: {} -> {}, letter: {}\t\t[{}]".format(word_without_alphabet_letter, special_word, letter, append_letter_on_position))
    return template.format(" ".join(words))


def list_all_chars(chars=CHARS__A_Z):
  return " ".join(chars)


def generate_document(pdf, file_suffix):

    html = '''<h2 align="center">{}</h2>
    {}
    '''.format(
list_all_chars(),
"".join([generate_words_with_alphabet(CONTEXT_TEMPLATE, verbose=VERBOSE) for _ in range(3)])
)

    pdf.set_font_size(24.0)
    pdf.set_text_color(0, 0, 0)
    pdf.add_page()
    pdf.write_html(html)
    pdf.output('visuallearning{}.pdf'.format(file_suffix))


if __name__ == '__main__':
    file_suffix = ''
    if  len(sys.argv) >= 2:
        file_suffix = sys.argv[1]

    generate_document(HTML2PDF(), file_suffix)

