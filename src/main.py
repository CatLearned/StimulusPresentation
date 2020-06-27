from psychopy import core, visual
from psychopy import prefs
from psychopy.hardware import keyboard
from p300_socket_class import p300_socket
import time


def number_to_direction(num):
    if num == 0:
        return "Stop"
    elif num == 1:
        return "Forward"
    elif num == 2:
        return "Back"
    elif num == 3:
        return "Right"
    elif num == 4:
        return "Left"
    else:
        return "Error"


# Инициализация клавиатуры, для проверки "ESC"
defaultKeyboard = keyboard.Keyboard()
# Файл для записи эксперимента
f = open('ExperimentStimulusPresentation.txt', 'w')
# Количество секунд между демонстрациями
duration = 1
# Тип вывода
# 0 - всё кроме стимула
# 1 - только стимул
# Остальные - вывести всё
type_show = 0
p300_delay = 0.3

p300_info = p300_socket("localhost", 9000, None)

# Создаём окно
window = visual.Window((700, 700), allowGUI=False)

# Создаём набор стимулов, размещаем их по окружности, в центре команда "Стоп"
stop = visual.ImageStim(win=window, pos=(0, 0), image='../stimulus_pics/stimulus_stop.png', size=(0.25, 0.25))
forward = visual.ImageStim(win=window, pos=(0, 0.5), image='../stimulus_pics/stimulus_forward.png', size=(0.25, 0.25))
back = visual.ImageStim(win=window, pos=(0, -0.5), image='../stimulus_pics/stimulus_back.png', size=(0.25, 0.25))
right = visual.ImageStim(win=window, pos=(0.5, 0), image='../stimulus_pics/stimulus_right.png', size=(0.25, 0.25))
left = visual.ImageStim(win=window, pos=(-0.5, 0), image='../stimulus_pics/stimulus_left.png', size=(0.25, 0.25))

# Упаковываем стимулы в массив для удобства
stimulus_arr = [stop, forward, back, right, left]

# Инициализируем таймер
trialClock = core.Clock()
# Сброс таймера
last_action_time = 0
t = 0
_timeToFirstFrame = window.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# Номер активного стимула
actual_stimulus_num = 0
p300_info.start_receive()

# Отображение и работа со стимулами производится в цикле
try:
    while True:
        # Получаем текущее время
        t = trialClock.getTime()
        tThisFlip = window.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = window.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # Количество отрисованных кадров
        # print(t, frameN)
        if t - last_action_time >= duration:
            last_action_time = t
            actual_stimulus_num = (actual_stimulus_num + 1) % (len(stimulus_arr))

        if type_show == 0:
            for itt in range(0, len(stimulus_arr)):
                if itt == actual_stimulus_num:
                    continue
                stimulus_arr[itt].draw(window)
        elif type_show == 1:
            stimulus_arr[actual_stimulus_num].draw(window)
        else:
            for stimulus in stimulus_arr:
                stimulus.draw(window)
        if p300_info.check_flag():
            print("Был P300! Время", t)
            p300_info.drop_flag()
            if type_show == 0 or type_show == 1:
                if t - p300_delay < last_action_time:
                    back_count = ((last_action_time - t - p300_delay) // duration) + 1
                    print("Command is", number_to_direction((actual_stimulus_num - back_count) % len(stimulus_arr)))
                else:
                    print("Command is", number_to_direction(actual_stimulus_num))
                ts = time.time()
                print(ts)
                f.write(str(ts) + '\n')
        if defaultKeyboard.getKeys(keyList=["escape"]):
            print("Was esc")
            break
        window.flip()
except KeyboardInterrupt:
    print('interrupted!')
print("Out of cicle")
f.close()
window.flip()
print("Out of after flip")
window.close()
print("Out of after close")
core.quit()
print("Out of after flip")

