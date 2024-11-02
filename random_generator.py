import random

def generate_random_number(start, end):
    return random.randint(start, end)

if __name__ == "__main__":
    print("Random Number Generator")
    
    # Tentukan rentang untuk angka acak
    start = int(input("Masukkan nilai awal: "))
    end = int(input("Masukkan nilai akhir: "))
    
    random_number = generate_random_number(start, end)
    print(f"Angka acak antara {start} dan {end}: {random_number}")
