# noinspection PyUnresolvedReferences
import kmNet


def init(ip: str, port: str, mac: str) -> None:
    kmNet.init(ip, port, mac)


def move(x: int, y: int) -> None:
    kmNet.move(x, y)


def left(isdown: int) -> None:
    kmNet.left(isdown)


def middle(isdown: int) -> None:
    kmNet.middle(isdown)


def right(isdown: int) -> None:
    kmNet.right(isdown)


def wheel(wheel_value: int) -> None:
    kmNet.wheel(wheel_value)


def move_auto(x: int, y: int, time_ms: int) -> None:
    kmNet.move_auto(x, y, time_ms)


def move_beizer(x: int, y: int, ms: int, x1: int, y1: int, x2: int, y2: int) -> None:
    kmNet.move_beizer(x, y, ms, x1, y1, x2, y2)


def keydown(vkey: int) -> None:
    kmNet.keydown(vkey)


def keyup(vkey: int) -> None:
    kmNet.keyup(vkey)


def monitor(port: int) -> None:
    kmNet.monitor(port)


def isdown_left() -> bool:
    return kmNet.isdown_left()


def isdown_middle() -> bool:
    return kmNet.isdown_middle()


def isdown_right() -> bool:
    return kmNet.isdown_right()


def isdown_side1() -> bool:
    return kmNet.isdown_side1()


def isdown_side2() -> bool:
    return kmNet.isdown_side2()


def isdown_keyboard(vkey: int) -> bool:
    return kmNet.isdown_keyboard(vkey)


# Mask Functions
def mask_left(enable: int) -> None:
    kmNet.mask_left(enable)


def mask_middle(enable: int) -> None:
    kmNet.mask_middle(enable)


def mask_right(enable: int) -> None:
    kmNet.mask_right(enable)


def mask_side1(enable: int) -> None:
    kmNet.mask_side1(enable)


def mask_side2(enable: int) -> None:
    kmNet.mask_side2(enable)


def mask_wheel(enable: int) -> None:
    kmNet.mask_wheel(enable)


def mask_x(enable: int) -> None:
    kmNet.mask_x(enable)


def mask_y(enable: int) -> None:
    kmNet.mask_y(enable)


def mask_keyboard(vkey: int, enable: int) -> None:
    kmNet.mask_keyboard(vkey, enable)


def unmask_keyboard(vkey: int) -> None:
    kmNet.unmask_keyboard(vkey)


def unmask_all() -> None:
    kmNet.unmask_all()


# Miscellaneous Functions
def reboot() -> None:
    kmNet.reboot()


def setip_port(ip: str, port: int) -> None:
    kmNet.setip_port(ip, port)


def lcd_color(rgb565: int) -> None:
    kmNet.lcd_color(rgb565)


def lcd_picture(buff_128_160: bytes) -> None:
    kmNet.lcd_picture(buff_128_160)


def lcd_picture_bottom(buff_128_80: bytes) -> None:
    kmNet.lcd_picture_bottom(buff_128_80)
