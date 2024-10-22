from pipeline import generate_and_process_primes

def main():
    result = generate_and_process_primes()
    print(f"Контрольная сумма первых 1000 простых чисел: {result}")

if __name__ == "__main__":
    main()
