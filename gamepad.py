import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

while True:

    # press a button to wake the device up
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.5)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    print(1)
    time.sleep(5)

    # press buttons and things
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.left_trigger_float(value_float=0.5)
    gamepad.right_trigger_float(value_float=0.5)
    gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.2)
    gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=1.0)

    gamepad.update()
    print(2)

    time.sleep(5)

    # release buttons and things
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.right_trigger_float(value_float=0.0)
    gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)

    gamepad.update()
    print(3)

    time.sleep(5)

    # reset gamepad to default state
    gamepad.reset()

    gamepad.update()
    print(4)

    time.sleep(5)