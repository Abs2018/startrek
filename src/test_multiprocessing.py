# import time


# def sleepy_man():
#     print('Starting to sleep')
#     time.sleep(1)
#     print('Done sleeping')


# tic = time.time()
# sleepy_man()
# sleepy_man()
# toc = time.time()

# print('Done in {:.4f} seconds'.format(toc-tic))

import multiprocessing
import time

core = multiprocessing.cpu_count() - 2


def myfunction(x, y):
    # print('Starting to sleep')
    # time.sleep(1)
    # print('Done sleeping')
    print(str(x)+", "+str(y))


if __name__ == '__main__':
    toc = time.time()
    x = 50
    process_list = []
    mystartx = x * -1
    myendx = x + 1
    mystarty = x * -1
    myendy = x + 1

    # for i in range(core):
    for y in range(mystarty, myendy):
        for x in range(mystartx, myendx):
            myfunction(x, y)
    #         p = multiprocessing.Process(target=myfunction(x, y))
    #         p.start()
    #         process_list.append(p)

    # for process in process_list:
    #     process.join()
    tic = time.time()

    print('Done in {:.4f} seconds'.format(tic-toc))
