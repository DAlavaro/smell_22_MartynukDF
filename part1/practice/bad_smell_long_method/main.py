# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_read(file):
    return [i.split(';') for i in file.split('\n')]


def _filter(file):
    return list(filter(lambda x: int(x[1]) > 10, file))


def _sorted(file):
    return sorted(file, key=lambda x: x[1])

def _map(file):
    return list(map(lambda x: {'name': x[0], 'age': int(x[1])}, file))






if __name__ == '__main__':
    file = get_read(csv)
    file = _filter(file)
    file = _sorted(file)
    print(_map(file))
