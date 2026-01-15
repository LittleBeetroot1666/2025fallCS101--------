import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    key_input = input_data[0]
    n = int(input_data[1])
    plaintexts = input_data[2:]

    # 使用replace函数把'j'全部转换为'i'
    key = key_input.lower().replace('j', 'i')
    alpha = 'abcdefghiklmnopqrstuvwxyz'
    matrix_chars = []
    seen = set()

    for char in key:
        if char not in seen:
            seen.add(char)
            matrix_chars.append(char)

    for char in alpha:
        if char not in seen:
            seen.add(char)
            matrix_chars.append(char)

    matrix = [matrix_chars[i: i + 5] for i in range(0, 25, 5)]
    pos_map = {char: (i // 5, i % 5) for i, char in enumerate(matrix_chars)}

    def encrypt_text(text):
        # 使用replace函数把'j'全部转换为'i'
        text = text.lower().replace('j', 'i')
        res = []
        i = 0
        length = len(text)

        while i < length:
            a = text[i]
            b = ''

            if i + 1 < length:
                b = text[i + 1]

                if a == b:
                    b = 'q' if a == 'x' else 'x'
                    i += 1
                else:
                    i += 2
            else:
                b = 'q' if a == 'x' else 'x'
                i += 1

            # 使用pos_map获取行数和列数
            r1, c1 = pos_map[a]
            r2, c2 = pos_map[b]
            if r1 == r2:
                res.append(matrix[r1][(c1 + 1) % 5])
                res.append(matrix[r2][(c2 + 1) % 5])
            elif c1 == c2:
                res.append(matrix[(r1 + 1) % 5][c1])
                res.append(matrix[(r2 + 1) % 5][c2])
            else:
                res.append(matrix[r1][c2])
                res.append(matrix[r2][c1])

        return ''.join(res)

    for text in plaintexts:
        print(encrypt_text(text))


if __name__ == '__main__':
    solve()
