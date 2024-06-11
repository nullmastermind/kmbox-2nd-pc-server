import time

import my_kmnet

if __name__ == "__main__":
    my_kmnet.init("192.168.2.188", "8357", "73E55C53")
    my_kmnet.monitor(10000)

    try:
        my_kmnet.mask_left(1)
        while 1:
            if my_kmnet.isdown_left():
                print("left button is down")
            if my_kmnet.isdown_right():
                print("right button is down")
            if my_kmnet.isdown_middle():
                print("middle button is down")
            if my_kmnet.isdown_side1():
                print("side1 button is down")
            if my_kmnet.isdown_side2():
                print("side2 button is down")
            time.sleep(0.5)
    except:
        my_kmnet.unmask_all()
