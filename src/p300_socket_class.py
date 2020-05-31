import threading
import socket
import time


class p300_socket:
    """Принимающий сокет. (Информация о P300)"""
    def __init__(self, ip, port, condition):
        """Коснтруктор ip, port - приёмника, condition - не используется"""
        self.__udp_ip = ip
        self.__udp_port = port
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.settimeout(1)  # Таймаут, чтобы не было залипания
        self.__sock.bind((self.__udp_ip, self.__udp_port))
        self.__condition = condition
        self.__need_work = True
        self.__receive_thread = None
        self.__flag = False
        self.__lock = threading.Lock()

    def check_flag(self):
        """Проверка флага, осуществляет тот, кому это важно, например демонстратор"""
        return self.__flag

    def drop_flag(self):
        """После проверки демонстратор должен положить флаг"""
        self.__flag = False

    def start_receive(self):
        """Запуск асинхронного приёма"""
        self.__receive_thread = threading.Thread(target=self.__thread_receive)
        self.__receive_thread.start()

    def __thread_receive(self):
        """Поток приёма, -генерирует событие- поднимает флаг при появлении P300"""
        while self.__need_work:
            try:
                data, address = self.__sock.recvfrom(1024)
                #self.__condition.set()
                self.__flag = True
            except socket.timeout:
                continue

    def stop_receive(self):
        """Остановка потока приёма, закрытие сокета"""
        self.__lock.acquire()
        self.__need_work = False
        self.__lock.release()
        self.__receive_thread.join()
        self.__sock.close()


def main():
    """Пример использования"""
    #event = threading.Event()
    mySock = p300_socket("localhost", 9000, None)
    mySock.start_receive()
    while True:
        time.sleep(0.1)
        if mySock.check_flag():
            print("Событие произошло")
            mySock.drop_flag()
    mySock.stop_receive()
    print("Socket stopped")


if __name__ == '__main__':
    print("Hello")
    main()
