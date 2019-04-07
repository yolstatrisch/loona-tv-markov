import glob
import os
import random
import re

def build_string(codon):
    output_string = codon

    while codon[-1] != '\0':
        next_letter = random.choice(codons[codon])
        output_string += next_letter
        codon = output_string[-codon_size:]

    print(output_string)

def build_markov():
    for file in glob.glob(os.path.join(path, '*.vtt')):
        with open(file, 'r+') as f:
            str = re.sub(trim_re, '', f.read())
            for i in range(len(str)):
                codon = str[i: i + codon_size]
                if i == 0:
                    starting_codons.append(codon)

                try:
                    next_letter = str[i + codon_size]
                except IndexError:
                    next_letter = '\0'

                if codon not in codons:
                    codons[codon] = []

                codons[codon].append(next_letter)

    starting_codon = random.choice(starting_codons)
    build_string(starting_codon)

if __name__ == '__main__':
    trim_re = r'(\d+:\d+:\d+\.\d+ \-\-\> \d+:\d+:\d+\.\d+)|\n{2}|WEBVTT\n|Kind: captions\n|Language: en\n'

    path = 'subs_raw/'
    codon_size = 8
    codons = {}
    starting_codons = []

    build_markov()
