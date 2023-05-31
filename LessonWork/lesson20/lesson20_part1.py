# GIL - Global Interpreter Lock
import multiprocessing
import time
# from random import randint
#
#
# def get_max():
#     print(max(list))
#
#
# def get_min():
#     print(min(list))
#
#
# if __name__ == '__main__':
#     list = str([randint(1, 10) for _ in range(100)]).split()
#     pr = multiprocessing.Process(target=get_max(), args=(list,))
#     pr2 = multiprocessing.Process(target=get_min(), args=(list,))
#     pr.start()
#     pr2.start()


# def lock_process(locker):
#     locker.acquire()
#     print(f'Процесс: {multiprocessing.current_process().name} завершен')
#     locker.release()
#
#
# def print_name():
#     print('Процесс: ', multiprocessing.current_process().name)
#
#
# if __name__ == '__main__':
#     locker = multiprocessing.RLock()
#     pr = multiprocessing.Process(target=lock_process, args=(locker,))
#     pr2 = multiprocessing.Process(target=print_name)
#     pr.start()
#     pr2.start()
#     print()


def get_name():
    name = multiprocessing.current_process().name
    print(f'Процесс {name} multiprocessing')
    time.sleep(2)
    print(multiprocessing.current_process().pid, 'завершен!')


if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    with multiprocessing.Pool(count) as p:
        p.map(get_name(), range(20))
        p.close()
        p.join()
