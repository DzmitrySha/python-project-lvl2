# Вычислитель отличий:

[![Actions Status](https://github.com/DzmitrySha/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/DzmitrySha/python-project-lvl2/actions)
[![workflow](https://github.com/DzmitrySha/python-project-lvl2/actions/workflows/pyci-check.yml/badge.svg)](https://github.com/DzmitrySha/python-project-lvl2/actions/workflows/pyci-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/14d8f0ef4843b93cd1d9/maintainability)](https://codeclimate.com/github/DzmitrySha/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/14d8f0ef4843b93cd1d9/test_coverage)](https://codeclimate.com/github/DzmitrySha/python-project-lvl2/test_coverage)

## Пример работы скрипта "Вычислитель отличий" (gendiff)

Запуск справки: `gendiff -h`

Запуск скрипта: `gendiff <file_path1> <file_path2>`

ПРИМЕР: Сравнение двух плоских файлов: JSON.

[![asciicast](https://asciinema.org/a/B2pi2NsEY6WNM7aU9OBIBodvM.svg)](https://asciinema.org/a/B2pi2NsEY6WNM7aU9OBIBodvM)

ПРИМЕР: Сравнение двух плоских файлов: YAML(YML).

[![asciicast](https://asciinema.org/a/6goaDnMwFvwPpbIWO2NhsC3Sq.svg)](https://asciinema.org/a/6goaDnMwFvwPpbIWO2NhsC3Sq)

ПРИМЕР: Сравнение двух файлов c рекурсивной структурой: YAML(YML) или JSON.

[![asciicast](https://asciinema.org/a/6jZ3XV9H5TrxOdujYCRSfI1rg.svg)](https://asciinema.org/a/6jZ3XV9H5TrxOdujYCRSfI1rg)

ПРИМЕР: Плоский формат отображения - cравнение двух файлов c рекурсивной структурой YAML(YML) или JSON.

[![asciicast](https://asciinema.org/a/3L3J2MUTMNwJSQZ3Q9UkiaxNf.svg)](https://asciinema.org/a/3L3J2MUTMNwJSQZ3Q9UkiaxNf)

ПРИМЕР: вывод отображения сравнения двух файлов в формате JSON.

[![asciicast](https://asciinema.org/a/IqWwqnjCVx7z6BTszNQyYmDQA.svg)](https://asciinema.org/a/IqWwqnjCVx7z6BTszNQyYmDQA)

Результат работы скрипта - строка, с обнаруженными в файлах отличиями. 

_Отсутствие плюса или минуса говорит о том, что ключ есть в обоих файлах, и его значения совпадают. Во всех остальных ситуациях значение по ключу либо отличается, либо ключ есть только в одном файле._ 
