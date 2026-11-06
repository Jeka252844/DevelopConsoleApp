def print_help():
    print(
        '''mathtool- калькулятор: уравнения, статистика, ряды, интегралы.

        Использование:
        python mathtool.py <команда> [параметры]

        Команды:

        quadratic   решение уравнения
            -a, -b, -c   коэффициенты (целые, |x| ≤ 10000)
            пример: python mathtool.py quadratic -a 1 -b -3 -c 2

        stats       показатели последовательности
            --input FILE   файл с числами (без него - stdin)
            пример: python mathtool.py stats --input numbers.txt

        series      сумма ряда
            --func NAME    ряд: sqplus, third
            --terms N      сколько слагаемых (1..10000)
            --eps E        точность (0 < E ≤ 0.0001)
            пример: python mathtool.py series --func sqplus --terms 6

        integrate   численное интегрирование
            --func NAME    функция: ratio, root
            --from A       нижний предел
            --to B         верхний предел (B > A)
            --steps N      число шагов (1..100000)
            пример: python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000
            
        fill        генерация массива
            -c, --count N  количество элементов (1..100000)
            --min A        минимум (≥ -1000000)
            --max B        максимум (≤ 1000000, B ≥ A)
            --seed S       зерно генератора
            -o, --output FILE   файл для записи
            пример: python mathtool.py fill -c 10 --min 1 --max 100
            
        sort        сортировка массива
            -m, --method NAME   метод сортировки: bubble, insertion, selection, quick
            --order ORDER       порядок: asc, desc (по умолчанию asc)
            -i, --input FILE    входной файл (по умолчанию stdin)
            -o, --output FILE   выходной файл (по умолчанию stdout)
            пример: python mathtool.py sort -m quick --order desc -i input.txt -o output.txt
            
        search      поиск в массиве
            -v, --value N   искомое значение (|N| ≤ 1000000)
            -i, --input FILE    входной файл (по умолчанию stdin)
            пример: python mathtool.py search -v 42 -i input.txt'''
    )