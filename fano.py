# declare structure node
class Node:
    def __init__(self):
        # for storing symbol
        self.sym = ''
        # for storing probability or frequency
        self.pro = 0.0
        self.arr = [0] * 20
        self.top = 0


# function to find shannon code
def shannon(l, h, p):
    pack1 = 0
    pack2 = 0
    diff1 = 0
    diff2 = 0
    if l + 1 == h or l == h or l > h:
        if l == h or l > h:
            return
        p[h].top += 1
        p[h].arr[p[h].top] = 0
        p[l].top += 1
        p[l].arr[p[l].top] = 1
        return
    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if diff1 < 0:
            diff1 = diff1 * -1
        j = 2
        while j != h - l + 1:
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].pro
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if diff2 < 0:
                diff2 = diff2 * -1
            if diff2 >= diff1:
                break
            diff1 = diff2
            j += 1
        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 1
        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 0
        # Invoke shannon function
        shannon(l, k, p)
        shannon(k + 1, h, p)


# Function to sort the symbols
# based on their probability or frequency
def sortByProbability(n, p):
    temp = Node()
    for j in range(1, n):
        for i in range(n - 1):
            if p[i].pro > p[i + 1].pro:
                temp.pro = p[i].pro
                temp.sym = p[i].sym
                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym
                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym


# function to display shannon codes
def compress(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    n = len(text)
    p = [Node() for _ in range(n)]

    for i in range(n):
        p[i].sym = text[i]

    freq_table = {char: text.count(char) / n for char in set(text)}
    for i in range(n):
        p[i].pro = freq_table[p[i].sym]

    sortByProbability(n, p)
    for i in range(n):
        p[i].top = -1

    shannon(0, n - 1, p)

    code_table = {}
    for i in range(n):
        code_table[p[i].sym] = ''.join(str(p[i].arr[j]) for j in range(p[i].top + 1))

    encoded_text = ''.join(code_table[char] for char in text)

    with open(output_file, 'w') as f:
        f.write(encoded_text)

    # Retorna a lista p e o dicionário de códigos
    return p, code_table


def decompress(input_file, output_file, code_table):

    with open(input_file, 'r', encoding='utf-8') as f:
        encoded_text = f.read()

    decoded_text = ""
    current_code = ""

    # Inverta o dicionário de códigos para mapear códigos para caracteres
    reverse_code_table = {code: char for char, code in code_table.items()}

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_code_table:
            char = reverse_code_table[current_code]
            decoded_text += char
            current_code = ""

    with open(output_file, 'w') as f:
        f.write(decoded_text)
    return decoded_text,

if __name__ == '__main__':
    input_file = "input.txt"
    compressed_file = "compressed.txt"
    decompressed_file = "decompressed.txt"

    # Comprimir o arquivo e obter a lista p
    compress(input_file, compressed_file)

    # Criar o dicionário de códigos
    code_table = {}

    # Descomprimir o arquivo usando o dicionário de códigos
    decompress(compressed_file, decompressed_file, code_table)
