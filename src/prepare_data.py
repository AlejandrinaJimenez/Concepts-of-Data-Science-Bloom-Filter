# prepare_data.py
with open("data/words.txt", "r") as f:
    all_words = [line.strip().lower() for line in f if line.strip()]

# Shuffle to avoid any ordering bias
import random
random.seed(42)
random.shuffle(all_words)

# Split: 70% for insertion, 30% for testing false positives
split = int(0.7 * len(all_words))

insert_words = all_words[:split]
not_insert_words = all_words[split:]

with open("data/inserted_words.txt", "w") as f:
    f.write("\n".join(insert_words))

with open("data/not_inserted_words.txt", "w") as f:
    f.write("\n".join(not_insert_words))

print(f"Created inserted_words.txt: {len(insert_words):,} words")
print(f"Created not_inserted_words.txt: {len(not_insert_words):,} words")