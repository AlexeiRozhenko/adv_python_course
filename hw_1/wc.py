import click
import sys

def count_stats(text):
    lines = text.splitlines()
    words = text.split()
    chars = len(text)
    return len(lines), len(words), chars

def print_stats(lines, words, chars, filename=None):
    if filename:
        print(f"{lines} {words} {chars} {filename}")
    else:
        print(f"{lines} {words} {chars}")

@click.command()
@click.argument('filenames', nargs=-1)
def wc(filenames):
    total_lines, total_words, total_chars = 0, 0, 0

    if filenames:
        for filename in filenames:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                lines, words, chars = count_stats(content)
                print_stats(lines, words, chars, filename)
                total_lines += lines
                total_words += words
                total_chars += chars

        if len(filenames) > 1:
            print_stats(total_lines, total_words, total_chars, "total")
    else:
        print("Ввод:")
        content = ""
        try:
            while True:
                for line in sys.stdin:
                    content += line
        except KeyboardInterrupt:
            pass
        
        lines, words, chars = count_stats(content)
        print_stats(lines, words, chars)

if __name__ == '__main__':
    wc()
