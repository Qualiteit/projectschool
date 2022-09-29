from tello import tello
import sys
from datetime import datetime
import time
import argparse

def parse_args(args):

    parser = argprarse.ArgumentParser('Tello Flight Commander',
    epilog='One-Off Coder https://www.oneoffcoder.com')

    parser.add_argument('-f', '--file', help='command file', required=True)
    return parser.parse_args(args)

    def start(file_name): 

        start_time = str(datetime.now())

        with open(file_name, 'r') as f:
            commands = f.readlines()

            tello = Tello()
            for command in commands:
                if command != '' and command != '\n':
                    command = command.rstrip()

                    if command.find('delay') != -1:
                        sec = float(command.partition('delay')[2])
                        print(f'delay {sec}')
                        time.sleep()
                        pass
                    else:
                        tello.send_command(command)

                        with open(f'log/{start_time}.txt', 'w') as out:
                            log = tello.get_log()

                            for stat in log:
                                stat.print_stats()
                                out.write(s)

                                if __name__ == '__main__':
                                    args = parse_args(sys.args[1:])
                                    file_name = args.file
                                    start(file_name)
