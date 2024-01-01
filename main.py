from pynput import mouse
import vgamepad as vg

gamepad = vg.VX360Gamepad()

# Глобальная переменная для отслеживания текущего положения колеса мыши
current_position = 0

# Обработчик события прокрутки колеса мыши
def on_scroll(x, y, dx, dy):
    global current_position
    # Увеличиваем или уменьшаем текущее положение в зависимости от направления прокрутки
    current_position += dy * 1000

    # Устанавливаем значения осей виртуального геймпада
    gamepad.left_joystick(x_value=current_position, y_value=0)
    #gamepad.right_trigger(value=0)  # value between 0 and 255

    gamepad.update()

    print(f"Current Position: {current_position} degrees")

# Создаем объект слушателя мыши
mouse_listener = mouse.Listener(on_scroll=on_scroll)

# Запускаем слушателя в фоновом режиме
mouse_listener.start()

# Ожидаем завершения программы (можно использовать KeyboardInterrupt для прерывания)
mouse_listener.join()
