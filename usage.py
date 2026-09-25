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
            пример: python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000'''
    )