from pipeline import generate_and_process_primes

def main():
    test_list = [1, 2, 6, 24]
    result = checksum(test_list)
    print(f"Контрольная сумма для {test_list}: {result}")

if __name__ == "__main__":
    main()