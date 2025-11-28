# Template Matcher

Простой инструмент для сопоставления входных данных с шаблонами.

## Зависимости

1. Python 3.6+.
2. tinydb
## Использование
```python data_processor.py ```   
Запуск через командную строку:

```bash
python data_processor.py find --field=value --field2=value2
```
Пример:

```bash
python data_processor.py find --email="user@example.com" --phone="+7 123 456 78 90"
```
``` python template_matcher.py ```


```bash
python template_matcher.py
```
## Формат данных
Поддерживаемые типы полей:

```email``` (например, user@example.com)

```phone``` (например, +7 123 456 78 90)

```date``` (например, 2025-12-31 или 31/12/2025)

```string``` (любые другие строки)

