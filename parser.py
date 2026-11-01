import re

def parse_matrix(text: str) -> list[list[int]]:
    """
    Приводит загруженную в виде строки матрицу к списку ее строк. 
    
    Например,
    матрица вида:

    +-----+-----+-----+-----+
    |  10 |  20 |  30 |  40 |
    +-----+-----+-----+-----+
    |  50 |  60 |  70 |  80 |
    +-----+-----+-----+-----+

    преобразуется в список: 

    [[10, 20, 30, 40], [50, 60, 70, 80]]
    """
    def recurse_parse(text: str, matrix: List[List[int]]) -> List[List[int]]:
        pattern = r'^.*\d.*$'
        match = re.search(pattern, text, re.MULTILINE)
        if not match: return matrix
        string_cur = str(match.group())
        matrix_string = [int(s) for s in string_cur.split()]
        matrix.append(matrix_string)
        return recurse_parse(text[match.end():], matrix)
    text = re.sub(r'[^0-9\n]', ' ', text)
    return recurse_parse(text, [])

if __name__ == "__main__":
    text = ("+-----+-----+-----+-----+\n" + 
        "|  10 |  20 |  30 |  40 |\n" + 
        "+-----+-----+-----+-----+\n" +
        "|  50 |  60 |  70 |  80 |\n" +
        "+-----+-----+-----+-----+\n" +
        "|  90 | 100 | 110 | 120 |\n" +
        "+-----+-----+-----+-----+\n" +
        "| 130 | 140 | 150 | 160 |\n" +
        "+-----+-----+-----+-----+")
    print('Пример исходной матрицы-строки: \n \n', text)
    print()
    print('Результат выполнения - матрица в виде списка строк: \n', parse_matrix(text))