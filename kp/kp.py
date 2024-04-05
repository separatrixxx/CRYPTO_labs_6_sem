import matplotlib.pyplot as plt
from keccak import keccak


def differential_analysis(message1, message2, r, round, output_length):
    hash1 = keccak(message1, r, round, output_length)
    hash2 = keccak(message2, r, round, output_length)
    
    diff_bits = sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(hash1, hash2))
    return diff_bits

def main():
    r = 1088
    output_length = 32

    message1 = b"Hello, world!"
    message2 = b"Hello, world?"

    rounds = range(1, 25)
    differences = [differential_analysis(message1, message2, r, round, output_length) for round in rounds]

    plt.plot(rounds, differences)
    plt.xlabel('Количество раундов')
    plt.ylabel('Количество отличающихся бит')
    plt.title('Дифференциальный криптоанализ Keccak-256')
    plt.show()

main()
