import machine
import time
"""
思想：在泰坦陨落2中，最后结尾菜单中的头盔有闪烁的画面(Ascii编码)。
实现：以短亮代表0，以长亮代表1，以此来展示编码内容。
"""

def light_status(status):
    single_list = list(status)
    for single in single_list:
        if int(single):
            pin2.value(1)
            time.sleep(0.4)
        else:
            pin2.value(1)
            time.sleep(0.1)
        pin2.value(0)
        time.sleep(0.1)


if __name__ == '__main__':
    pin2 = machine.Pin(2, machine.Pin.OUT)
    morse_string = "00000111 00000001 00001010 00000101 00001100"
    morse_list = morse_string.split(" ")
    for morse in morse_list:
        light_status(morse)
        pin2.value(0)
        time.sleep(1)
