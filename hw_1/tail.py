import click 
import sys 

@click.command()
@click.argument('filenames', nargs=-1) 
def tail(filenames):
    i = 0
    if filenames:
        for i, filename in enumerate(filenames):
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()

                if len(filenames) > 1:
                    if i > 0:
                        print()
                        print()
                    print(f"==> {filename} <==")

                last_lines = lines[-10:]
                for line in last_lines:
                    print(line, end='')

    else:
        lines = [] 
        print("Введите строки:")

        try:
            while True:
                for line in sys.stdin:
                    lines.append(line)  
        except KeyboardInterrupt:
            pass
        print("Результат:")
        for line in lines[-17:]:
            print(line, end='')

if __name__ == '__main__':
    tail()