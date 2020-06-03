# StimulusPresentation
* Программа показывает стимулы, и реагирует на информацию о P300, которая приходит по UDP
* Вычисляет на какую команду была реакция
* Для построение графического интерфейса используется инструмент PsychoPy

# Директории проекта
* .idea - информация для IDE (TODO добавить в .gitignore)
* src - содержит исходные коды модулей, подробнее будет рассмотрено далее
* stimulus_pics - содержит изображения стимулов
* venv - виртуальное окружение, содержит информацию о подключённых библиотеках в проекте

## Директория src
* [main.py](https://github.com/CatLearned/StimulusPresentation/blob/master/src/main.py) - запускаемый модуль, отображает GUI и реагирует на информацию с сокета
* [p300_demonstartion.py](https://github.com/CatLearned/StimulusPresentation/blob/master/src/p300_demonstartion.py) - не используется
* [p300_socket_class.py](https://github.com/CatLearned/StimulusPresentation/blob/master/src/p300_socket_class.py) - содержит описание асинхронного UDP сокета

### src/main.py
Общие параметры для отображения и расчёта команды:
* duration - задержка в секундах между демонстрациями стимулов
* type_show - тип отображения. (0 - всё кроме стимула, 1 - стимул, другое - режим демонстрации все стимулы)
* p300_delay - задержка появления P300 (Параметр необходимо откалибровать при реальных экспериментах)

Инициализация сокета
`p300_info = p300_socket("localhost", 9000, None)`
параметры:
1. IP адрес слушателя, должен быть таким же как и в проекте [FakeP300](https://github.com/CatLearned/FakeP300)
2. Порт слушателя, должен быть таким же как и в проекте [FakeP300](https://github.com/CatLearned/FakeP300)
3. Указатель на событие, сейчас не используется нужно передавать `None`

# Работа в комбинации с [FakeP300](https://github.com/CatLearned/FakeP300)
[FakeP300](https://github.com/CatLearned/FakeP300) используется для отправке сигнала о наличии [P300](https://en.wikipedia.org/wiki/P300_(neuroscience))

[StimulusPresentation](https://github.com/CatLearned/StimulusPresentation) принимает сигнал и интерпретирует в команду.

Порядок работы:
1. Выставить в [src/main.py](https://github.com/CatLearned/StimulusPresentation/blob/master/src/main.py) проекта [StimulusPresentation](https://github.com/CatLearned/StimulusPresentation) type_show равным 0 или 1.
2. Выбрать стимул, который нам интересен, например команда вперёд.
3. При появлении (при `type_show == 1`, иначе оно должно наоборот пропасть) изоражения вперёд (Стрелка вверх). В консоле программы [FakeP300](https://github.com/CatLearned/FakeP300) нажать Enter
4. В консоли [StimulusPresentation](https://github.com/CatLearned/StimulusPresentation) должна появиться выбранная команда.

## Команды <---> Изображения

| Команда вперёд | Команда стоп | Команда назад | Команда направо | Команда налево |
| :------------: | :----------: | :-----------: | :-------------: | :------------: |
| ![Команда вперёд!](https://github.com/CatLearned/StimulusPresentation/blob/master/stimulus_pics/stimulus_forward.png "Команда вперёд") | ![Команда стоп!](https://github.com/CatLearned/StimulusPresentation/blob/master/stimulus_pics/stimulus_stop.png "Команда стоп") | ![Команда назад!](https://github.com/CatLearned/StimulusPresentation/blob/master/stimulus_pics/stimulus_back.png "Команда назад") | ![Команда направо!](https://github.com/CatLearned/StimulusPresentation/blob/master/stimulus_pics/stimulus_right.png "Команда направо") | ![Команда налево!](https://github.com/CatLearned/StimulusPresentation/blob/master/stimulus_pics/stimulus_left.png "Команда налево") |
