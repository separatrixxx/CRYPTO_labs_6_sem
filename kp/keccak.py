def ROL(value, bits, width=64):
    return ((value << bits) % (1 << width)) | (value >> (width - bits))

def theta(A):
    C = [0] * 5
    D = [0] * 5

    for x in range(5):
        C[x] = A[x][0] ^ A[x][1] ^ A[x][2] ^ A[x][3] ^ A[x][4]

    for x in range(5):
        D[x] = C[(x - 1) % 5] ^ ROL(C[(x + 1) % 5], 1)

    for x in range(5):
        for y in range(5):
            A[x][y] ^= D[x]

    return A

def rho(A):
    rotations = [
        [0,  1,  62, 28, 27],
        [36, 44, 6,  55, 20],
        [3,  10, 43, 25, 39],
        [41, 45, 15, 21, 8],
        [18, 2,  61, 56, 14]
    ]

    B = [[0] * 5 for _ in range(5)]

    for x in range(5):
        for y in range(5):
            B[x][y] = ROL(A[x][y], rotations[x][y])

    return B

def pi(A):
    B = [[0] * 5 for _ in range(5)]

    for x in range(5):
        for y in range(5):
            B[x][y] = A[(x + 3*y) % 5][x]

    return B

def chi(A):
    B = [[0] * 5 for _ in range(5)]

    for x in range(5):
        for y in range(5):
            B[x][y] = A[x][y] ^ ((~A[(x + 1) % 5][y]) & A[(x + 2) % 5][y])

    return B

def iota(A, round_idx):
    RC = [0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
          0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
          0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
          0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
          0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
          0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
          0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
          0x8000000000008080, 0x0000000080000001, 0x8000000080008008]
    
    A[0][0] ^= RC[round_idx]

    return A

def keccak_f(S, rounds):
    A = [[0] * 5 for _ in range(5)]

    for x in range(5):
        for y in range(5):
            for z in range(64):
                byte_index = (64 * (5 * y + x) + z) // 8
                bit_index = z % 8
                A[x][y] |= ((S[byte_index] >> bit_index) & 1) << z
    
    # Применение заданного количества раундов
    for round_idx in range(rounds):
        A = theta(A)
        A = rho(A)
        A = pi(A)
        A = chi(A)
        A = iota(A, round_idx)
    
    # Преобразование обратно в байты
    for x in range(5):
        for y in range(5):
            for z in range(64):
                byte_index = (64 * (5 * y + x) + z) // 8
                bit_index = z % 8
                
                if (A[x][y] >> z) & 1:
                    S[byte_index] |= 1 << bit_index
                else:
                    S[byte_index] &= ~(1 << bit_index)

    return S

def pad_message(M, r):
    if isinstance(M, str):
        M = M.encode('utf-8')

    P = M + b'\x01'  # Добавляем 0x01 к сообщению
    padding_length = (-len(P) * 8 % r) // 8

    if padding_length > 0:
        P += b'\x00' * (padding_length - 1) + b'\x80'  # 0x00...0x80
    else:
        P = M[:-1] + b'\x81'  # Заменяем последний байт на 0x81, если нужно добавить только один байт

    return P

def keccak(M, r, rounds, output_length):
    S = bytearray(200)  # Инициализация начального состояния S размером 1600 бит
    P = pad_message(M, r)
    block_size = r // 8

    for i in range(0, len(P), block_size):
        block = P[i:i+block_size]

        for j in range(block_size):
            S[j] ^= block[j]
            
        S = keccak_f(S, rounds)  # Применяем функцию перестановки с указанным количеством раундов

    return S[:output_length]
