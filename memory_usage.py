"""
Skrypt do sprawdzania zużycia pamięci, CPU i czasu wykonania
przy różnych metodach wczytywania danych z pliku CSV.
"""

import os
import psutil
import csv
import time

def get_process_memory_usage():
    """Zwraca zużycie pamięci RAM przez proces w MB"""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)  # MB

def get_process_cpu_percent(interval=0.1):
    """Zwraca użycie CPU przez proces (%) po krótkim interwale"""
    process = psutil.Process(os.getpid())
    return process.cpu_percent(interval=interval)

def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=",")
        return [row for row in csv_reader]

def read_file_to_generator(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            yield row

def create_test_csv(file_path, num_rows=100000):
    """Tworzy testowy plik CSV jeśli nie istnieje"""
    with open(file_path, "w", newline='') as file:
        writer = csv.writer(file)
        for i in range(num_rows):
            writer.writerow([i, f"tekst{i}", i * 2])

def main():
    file_path = "data.csv"
    raport_path = "raport.txt"
    raport_lines = []
    separator = "-" * 50

    def log(msg):
        print(msg)
        raport_lines.append(msg)

    log("=== TEST ZUŻYCIA PAMIĘCI, CPU I CZASU ===")
    log(f"Początkowe zużycie pamięci: {get_process_memory_usage():.2f} MB\n")

    if not os.path.exists(file_path):
        log("Plik testowy nie istnieje — tworzę go...")
        create_test_csv(file_path)

    # --- LISTA ---
    log("\n[1] Wczytywanie pliku do listy...")
    start_time = time.perf_counter()
    memory_before_list = get_process_memory_usage()
    cpu_before_list = get_process_cpu_percent()

    data_list = read_file_to_list(file_path)

    cpu_after_list = get_process_cpu_percent()
    memory_after_list = get_process_memory_usage()
    elapsed_list = time.perf_counter() - start_time

    log(f"  Czas wczytania do listy: {elapsed_list:.4f} s")
    log(f"  Zużycie pamięci po wczytaniu: {memory_after_list:.2f} MB (+{memory_after_list - memory_before_list:.2f})")
    log(f"  Użycie CPU: {cpu_after_list:.1f} %")
    log(separator)

    # --- USUNIĘCIE LISTY ---
    log("[2] Usuwanie listy z pamięci...")
    start_time = time.perf_counter()
    del data_list
    time.sleep(1)  # pozwól Pythonowi na cleanup
    memory_after_del = get_process_memory_usage()
    elapsed_del = time.perf_counter() - start_time
    log(f"  Czas usuwania listy: {elapsed_del:.4f} s")
    log(f"  Zużycie pamięci po usunięciu listy: {memory_after_del:.2f} MB")
    log(separator)

    # --- GENERATOR ---
    log("[3] Tworzenie generatora i iteracja po pierwszych 10 wierszach...")
    start_time = time.perf_counter()
    memory_before_gen = get_process_memory_usage()
    cpu_before_gen = get_process_cpu_percent()

    data_generator = read_file_to_generator(file_path)
    for i, row in enumerate(data_generator):
        if i < 10:
            log(f"    {row}")
        else:
            break

    cpu_after_gen = get_process_cpu_percent()
    memory_after_gen = get_process_memory_usage()
    elapsed_gen = time.perf_counter() - start_time
    log(f"\n  Czas odczytu przez generator: {elapsed_gen:.4f} s")
    log(f"  Zużycie pamięci po generatorze: {memory_after_gen:.2f} MB (+{memory_after_gen - memory_before_gen:.2f})")
    log(f"  Użycie CPU: {cpu_after_gen:.1f} %")
    log(separator)

    # --- ZAPIS DO PLIKU ---
    with open(raport_path, "w", encoding="utf-8") as raport_file:
        raport_file.write("\n".join(raport_lines))

    log(f"\nRaport zapisany do pliku: {raport_path}")

if __name__ == "__main__":
    main()
