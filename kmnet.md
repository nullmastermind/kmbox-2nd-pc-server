# KMNet Python Interface

## Initialization
- `init(ip: str, port: str, mac: str) -> None`
    - Initialize the connection with the given IP, port, and MAC address.

## Mouse Functions
- `move(x: int, y: int) -> None`
    - Move the mouse to the specified (x, y) coordinates.

- `left(isdown: bool) -> None`
    - Simulate a left mouse button click. `isdown` indicates whether the button is pressed down.

- `middle(isdown: bool) -> None`
    - Simulate a middle mouse button click. `isdown` indicates whether the button is pressed down.

- `right(isdown: bool) -> None`
    - Simulate a right mouse button click. `isdown` indicates whether the button is pressed down.

- `wheel(wheel: int) -> None`
    - Simulate a mouse wheel scroll. `wheel` indicates the scroll amount.

- `move_auto(x: int, y: int, time_ms: int) -> None`
    - Automatically move the mouse to the specified (x, y) coordinates over a given time in milliseconds.

- `move_beizer(x: int, y: int, ms: int, x1: int, y1: int, x2: int, y2: int) -> None`
    - Move the mouse to the specified (x, y) coordinates using a Bezier curve over a given time in milliseconds.

## Keyboard Functions
- `keydown(vkey: int) -> None`
    - Simulate a key press for the specified virtual key code.

- `keyup(vkey: int) -> None`
    - Simulate a key release for the specified virtual key code.

## Monitor Functions
- `monitor(port: int) -> None`
    - Monitor the specified port.

- `isdown_left() -> bool`
    - Check if the left mouse button is pressed.

- `isdown_middle() -> bool`
    - Check if the middle mouse button is pressed.

- `isdown_right() -> bool`
    - Check if the right mouse button is pressed.

- `isdown_side1() -> bool`
    - Check if the side button 1 is pressed.

- `isdown_side2() -> bool`
    - Check if the side button 2 is pressed.

- `isdown_keyboard(vkey: int) -> bool`
    - Check if the specified virtual key is pressed.

## Mask Functions
- `mask_left(enable: bool) -> None`
    - Mask the left mouse button. `enable` indicates whether to enable or disable the mask.

- `mask_middle(enable: bool) -> None`
    - Mask the middle mouse button. `enable` indicates whether to enable or disable the mask.

- `mask_right(enable: bool) -> None`
    - Mask the right mouse button. `enable` indicates whether to enable or disable the mask.

- `mask_side1(enable: bool) -> None`
    - Mask the side button 1. `enable` indicates whether to enable or disable the mask.

- `mask_side2(enable: bool) -> None`
    - Mask the side button 2. `enable` indicates whether to enable or disable the mask.

- `mask_wheel(enable: bool) -> None`
    - Mask the mouse wheel. `enable` indicates whether to enable or disable the mask.

- `mask_x(enable: bool) -> None`
    - Mask the mouse x-axis movement. `enable` indicates whether to enable or disable the mask.

- `mask_y(enable: bool) -> None`
    - Mask the mouse y-axis movement. `enable` indicates whether to enable or disable the mask.

- `mask_keyboard(vkey: int) -> None`
    - Mask the specified virtual key. `enable` indicates whether to enable or disable the mask.

- `unmask_keyboard(vkey: int) -> None`
    - Unmask the specified virtual key.

- `unmask_all() -> None`
    - Unmask all previously masked inputs.

## Miscellaneous Functions
- `reboot() -> None`
    - Reboot the system.

- `setip_port(ip: str, port: int) -> None`
    - Set the IP address and port.

- `lcd_color(rgb565: int) -> None`
    - Set the LCD color using the specified RGB565 value.

- `lcd_picture(buff_128_160: bytes) -> None`
    - Display a 128x160 picture on the LCD.

- `lcd_picture_bottom(buff_128_80: bytes) -> None`
    - Display a 128x80 picture on the bottom of the LCD.