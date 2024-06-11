# KM Server

KM Server is a utility UDP server for KMBox-net designed to run on a secondary PC. This server allows for various remote operations such as mouse movements, keyboard actions, and other control functionalities.

## Requirements

- Python 3.11

## Usage

KM Server listens for UDP packets and performs actions based on the received commands. The commands should be in the format:

- `call,function_name,params...`
- `call_return,function_name,params...`

For multiple calls, use line breaks to separate each command.

### Example Call

```plaintext
call,move,100,200
call_return,isdown_left
```

## Available Functions

Below is a list of available functions you can call on the KM Server:

### Initialization

```plaintext
call,init,ip,port,mac
```

### Mouse Actions

```plaintext
call,move,x,y
call,left,isdown
call,middle,isdown
call,right,isdown
call,wheel,wheel_value
call,move_auto,x,y,time_ms
call,move_beizer,x,y,ms,x1,y1,x2,y2
```

### Keyboard Actions

```plaintext
call,keydown,vkey
call,keyup,vkey
```

### Monitoring

```plaintext
call,monitor,port
```

### Status Checks

```plaintext
call_return,isdown_left
call_return,isdown_middle
call_return,isdown_right
call_return,isdown_side1
call_return,isdown_side2
call_return,isdown_keyboard,vkey
```

### Mask Functions

```plaintext
call,mask_left,enable
call,mask_middle,enable
call,mask_right,enable
call,mask_side1,enable
call,mask_side2,enable
call,mask_wheel,enable
call,mask_x,enable
call,mask_y,enable
call,mask_keyboard,vkey,enable
```

### Unmask Functions

```plaintext
call,unmask_keyboard,vkey
call,unmask_all
```

### System Functions

```plaintext
call,reboot
call,setip_port,ip,port
```

### LCD Functions

```plaintext
call,lcd_color,rgb565
call,lcd_picture,buff_128_160
call,lcd_picture_bottom,buff_128_80
```

Boolean function parameters should be 0 or 1