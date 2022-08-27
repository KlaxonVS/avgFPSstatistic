import os
import sys
from sys import argv
import time

import cv2
import numpy as np
import PIL.ImageGrab
import pyautogui as pag
import psutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GAME_PROCESS = 'kkrieger.exe'

GAME = argv[1]
REPORT = argv[2]

# Если директория REPORT не существует, то она будет создана
if not os.path.isdir(REPORT):
    os.mkdir(REPORT)

# Шаблоны для нахождения объектов на экране
after_load_tepm = cv2.imread(
    os.path.join(BASE_DIR, 'sample_img/after_load.png'),
    cv2.IMREAD_GRAYSCALE
)
start_tepm = cv2.imread(
    os.path.join(BASE_DIR, 'sample_img/start.png'),
    cv2.IMREAD_GRAYSCALE
)
quit_tepm = cv2.imread(
    os.path.join(BASE_DIR, 'sample_img/quit.png'),
    cv2.IMREAD_GRAYSCALE
)
exit_tepm = cv2.imread(
    os.path.join(BASE_DIR, 'sample_img/exit.png'),
    cv2.IMREAD_GRAYSCALE
)


def match_find(screenshots, object) -> bool:
    """Находит на скриншоте искомый объект"""
    gray_frame = cv2.cvtColor(screenshots, cv2.COLOR_BGR2GRAY)
    comparison = cv2.matchTemplate(
        gray_frame, object, cv2.TM_CCOEFF_NORMED
    )
    obj_location = np.where(comparison >= 0.9)
    return bool(obj_location[0].size > 0)


def game_shutdown() -> None:
    """Завершает процесс игры"""
    for process in psutil.process_iter():
        if process.name() == GAME_PROCESS:
            process.kill()


def report_file() -> None:
    """Создаёт по указанному пути REPORT txt файл с отчетом"""
    fraps_report = os.path.join(BASE_DIR, 'fraps_report')
    logs = '/FRAPSLOG.txt'
    message = ''
    with open(fraps_report+logs) as log:
        for i, line in enumerate(log):
            if i == 1:
                message = line
    fps_list = message.split(' - ')
    avg_fps = fps_list[2].split(': ')
    final_report = open(REPORT + '/final_report.txt', mode='w')
    final_report.write(f'Средний FPS: {avg_fps[1]}')
    final_report.close()


def main():
    os.startfile(GAME)
    time.sleep(5)
    kk = pag.getWindowsWithTitle('kk')
    while kk[0]:
        screenshots = np.array(PIL.ImageGrab.grab())
        if match_find(screenshots, after_load_tepm):
            pag.keyDown('space')
            time.sleep(1)
            pag.keyUp('space')
        if match_find(screenshots, start_tepm):
            pag.keyDown('enter')
            time.sleep(1)
            pag.keyUp('enter')
            time.sleep(1)
            PIL.ImageGrab.grab().save(f'{REPORT}/start_scene.png', 'PNG')
            pag.press('f11')
            time.sleep(1)
            pag.keyDown('w')
            time.sleep(15)
            pag.keyUp('w')
            time.sleep(1)
            PIL.ImageGrab.grab().save(f'{REPORT}/end_scene.png', 'PNG')
            pag.keyDown('esc')
            time.sleep(1)
            pag.keyUp('esc')
            game_shutdown()
            break
    report_file()
    sys.exit()


if __name__ == "__main__":
    main()
