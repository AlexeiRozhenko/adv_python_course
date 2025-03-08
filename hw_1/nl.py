import click 
import sys 

@click.command()
@click.argument('filename', required=False)
def nl(filename):
    if filename:
        with open(filename, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                print(f"{i}: {line}", end='')

    else:
        lines = [] 
        print("Введите строки:")

        try:
            while True:
                for line in sys.stdin:
                    lines.append(line)  
        except KeyboardInterrupt:
            pass

        for i, line in enumerate(lines, start=1):
            print(f"{i}: {line}", end='')


if __name__ == '__main__':
    nl()