import os

# Invented word entry: "promnesia (n.) — forgetting what you asked your agent
# to do the moment it starts doing it."
# Verified count: 90 characters, 92 UTF-8 bytes (em-dash U+2014 is 3 bytes).
ENTRY = "promnesia (n.) — forgetting what you asked your agent to do the moment it starts doing it."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
if output_dir:
    output_path = os.path.join(output_dir, "entry.txt")
else:
    output_path = "/output/entry.txt"

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

print(f"wrote {len(ENTRY.encode('utf-8'))} bytes to {output_path}")
