## Замер среднего FPS игры kkrieger:

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:VorVorsky/avgFPSstatistic.git
```

```
cd avgFPSstatistic
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Установить FRAPS и настроить его:

* Ссылка: https://fraps.com/download.php
1. Установить и запустить программу
2. В пункте FPS устанавливаем путь "Folder to save benchmarks in", как:"path\to\avgFPSstatistic\fraps_report" 
3. Проверяем, что Benchmarking Hotkey "F10" и отмечаем пункт MinMaxAvg
4. А также Stop benchmark after {time} seconds, где time = 15

Важно:
* Перед запуском скрипта FRAPS должен быть открыт
* Если для запуска kkrieger проишлось поставить режим совместимости с Windows XP (Пакет обновления 2), то IDE должен запускаться от имени администратора
* Во избежания конфликтов и неправильной работы, во время запуска скрипта должна стоять английския раскладка (US)

Запустить проект и он сам совершит необходимые манипуляции, закроет игру и выйдет на рабочий стол:

```
python reportAVGfps.py <path\to\kkrieger> <path\to\output>
```
Для наглядности так выглядел скрипт у меня:

```
python reportAVGfps.py S:/Dev/avgFPSstatistic/kkrieger.exe S:/Dev/avgFPSstatistic/example_report2
```