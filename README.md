### Hexlet tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/DzmitrySha/python-project-lvl2)

[![Actions Status](https://github.com/DzmitrySha/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/DzmitrySha/python-project-lvl2/actions)

[![workflow](https://github.com/DzmitrySha/python-project-lvl2/actions/workflows/linter-check.yml/badge.svg)](https://github.com/DzmitrySha/python-project-lvl2/actions/workflows/linter-check.yml)

## Пример работы скрипта "Вычислитель отличий" (gendiff)

Запуск справки: `gendiff -h`

Запуск скрипта: `gendiff file_path1.json file_path1.json`

Сравнение двух плоских файлов формата JSON.

[![asciicast](https://asciinema.org/a/B2pi2NsEY6WNM7aU9OBIBodvM.png)](https://asciinema.org/a/B2pi2NsEY6WNM7aU9OBIBodvM)

Результат работы скрипта - строка, с обнаруженными в файлах отличиями. 

_Отсутствие плюса или минуса говорит о том, что ключ есть в обоих файлах, и его значения совпадают. Во всех остальных ситуациях значение по ключу либо отличается, либо ключ есть только в одном файле._ 