from dotenv import load_dotenv

load_dotenv()

import os

# noinspection PyUnresolvedReferences
import kmNet

DEBUG = os.environ.get("DEBUG") == "1"

print("DEBUG:", DEBUG)


def init(ip: str, port: str, mac: str) -> None:
    if DEBUG:
        return None
    kmNet.init(ip, port, mac)


def move(x: str, y: str) -> None:
    if DEBUG:
        return None
    kmNet.move(int(x), int(y))


def left(isdown: str) -> None:
    if DEBUG:
        return None
    kmNet.left(int(isdown))


def middle(isdown: str) -> None:
    if DEBUG:
        return None
    kmNet.middle(int(isdown))


def right(isdown: str) -> None:
    if DEBUG:
        return None
    kmNet.right(int(isdown))


def wheel(wheel_value: str) -> None:
    if DEBUG:
        return None
    kmNet.wheel(int(wheel_value))


def move_auto(x: str, y: str, time_ms: str) -> None:
    if DEBUG:
        return None
    kmNet.move_auto(int(x), int(y), int(time_ms))


def move_beizer(x: str, y: str, ms: str, x1: str, y1: str, x2: str, y2: str) -> None:
    if DEBUG:
        return None
    kmNet.move_beizer(int(x), int(y), int(ms), int(x1), int(y1), int(x2), int(y2))


def keydown(vkey: str) -> None:
    if DEBUG:
        return None
    kmNet.keydown(int(vkey))


def keyup(vkey: str) -> None:
    if DEBUG:
        return None
    kmNet.keyup(int(vkey))


def monitor(port: str) -> None:
    if DEBUG:
        return None
    kmNet.monitor(int(port))


def isdown_left() -> bool:
    if DEBUG:
        return False
    return kmNet.isdown_left()


def isdown_middle() -> bool:
    if DEBUG:
        return False
    return kmNet.isdown_middle()


def isdown_right() -> bool:
    if DEBUG:
        return False
    return kmNet.isdown_right()


def isdown_side1() -> bool:
    if DEBUG:
        return False
    return kmNet.isdown_side1()


def isdown_side2() -> bool:
    if DEBUG:
        return False
    return kmNet.isdown_side2()


def isdown_keyboard(vkey: str) -> bool:
    if DEBUG:
        return False
    return kmNet.isdown_keyboard(int(vkey))


# Mask Functions
def mask_left(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_left(int(enable))


def mask_middle(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_middle(int(enable))


def mask_right(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_right(int(enable))


def mask_side1(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_side1(int(enable))


def mask_side2(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_side2(int(enable))


def mask_wheel(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_wheel(int(enable))


def mask_x(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_x(int(enable))


def mask_y(enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_y(int(enable))


def mask_keyboard(vkey: str, enable: str) -> None:
    if DEBUG:
        return None
    kmNet.mask_keyboard(int(vkey), int(enable))


def unmask_keyboard(vkey: str) -> None:
    if DEBUG:
        return None
    kmNet.unmask_keyboard(int(vkey))


def unmask_all() -> None:
    if DEBUG:
        return None
    kmNet.unmask_all()


def reboot() -> None:
    if DEBUG:
        return None
    kmNet.reboot()


def setip_port(ip: str, port: str) -> None:
    if DEBUG:
        return None
    kmNet.setip_port(ip, int(port))


def lcd_color(rgb565: str) -> None:
    if DEBUG:
        return None
    kmNet.lcd_color(int(rgb565))


def lcd_picture(buff_128_160: str) -> None:
    if DEBUG:
        return None
    kmNet.lcd_picture(bytes(buff_128_160, "utf-8"))


def lcd_picture_bottom(buff_128_80: str) -> None:
    if DEBUG:
        return None
    kmNet.lcd_picture_bottom(bytes(buff_128_80, "utf-8"))


my_kmnet_functions = {
    "init": init,
    "move": move,
    "left": left,
    "middle": middle,
    "right": right,
    "wheel": wheel,
    "move_auto": move_auto,
    "move_beizer": move_beizer,
    "keydown": keydown,
    "keyup": keyup,
    "monitor": monitor,
    "isdown_left": isdown_left,
    "isdown_middle": isdown_middle,
    "isdown_right": isdown_right,
    "isdown_side1": isdown_side1,
    "isdown_side2": isdown_side2,
    "isdown_keyboard": isdown_keyboard,
    "mask_left": mask_left,
    "mask_middle": mask_middle,
    "mask_right": mask_right,
    "mask_side1": mask_side1,
    "mask_side2": mask_side2,
    "mask_wheel": mask_wheel,
    "mask_x": mask_x,
    "mask_y": mask_y,
    "mask_keyboard": mask_keyboard,
    "unmask_keyboard": unmask_keyboard,
    "unmask_all": unmask_all,
    "reboot": reboot,
    "setip_port": setip_port,
    "lcd_color": lcd_color,
    "lcd_picture": lcd_picture,
    "lcd_picture_bottom": lcd_picture_bottom,
}
