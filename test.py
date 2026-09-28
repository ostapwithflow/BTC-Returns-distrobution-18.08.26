from pathlib import Path
import csv

folder = Path(__file__).resolve().parent /"csv"/ "1d"

files = sorted(folder.glob("BTCUSDT-1d-????-??.csv"))
merged = folder / "BTCUSDT-1d-merged.csv"


def count_rows(path, has_header=False):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        # Читаємо записи CSV, пропускаючи порожні рядки
        rows = (row for row in csv.reader(file) if row)

        if has_header:
            next(rows, None)  # Пропускаємо заголовок

        return sum(1 for _ in rows)


if not files:
    raise FileNotFoundError("Не знайдено початкових CSV")

print("Рахую рядки...", flush=True)

original_count = sum(count_rows(file) for file in files)
merged_count = count_rows(merged, has_header=True)

print(f"Початкових файлів: {len(files)}")
print(f"Рядків у початкових файлах разом: {original_count:,}")
print(f"Рядків даних у merged:           {merged_count:,}")

if original_count == merged_count:
    print("Кількість рядків збігається.")
else:
    print("Кількість НЕ збігається — оригінали не видаляй.")
    print(f"Різниця: {merged_count - original_count:+,}")


#1m - Збігається
#5m - Збігається
#15m - Збігається
#30m - Збігається
#1h - Збігається
#4h - Збігається
#1d - Збігається