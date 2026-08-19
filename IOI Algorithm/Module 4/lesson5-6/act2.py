# POWER MAP
# Topics: Power Set | Binary Mask | Bit Probe | Subset Enumeration | Bit Difference

items = ["A", "B", "C"]
n = len(items)
total = 2 ** n

print("=== Power Map ===")
print("Items:", items)
print("Elements:", n, "  Total subsets: 2 ^", n, "=", total)
print()

# PART 1: Binary mask table
# Each number from 0 to (total - 1) is a binary mask
# Bit position j = 1 means items[j] is IN the subset
print("Mask table (n =", n, "):")
mask = 0
while mask < total:
    bit2 = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1
    print("  mask", mask, "-> [C][B][A] =", bit2, bit1, bit0)
    mask = mask + 1
print()

# PART 2: Build each subset using a bit probe
# 1 << j makes a probe with only bit j set
# mask & probe > 0 means bit j IS set in mask -> include items[j]
print("All subsets (bit probe):")
mask = 0
while mask < total:
    subset = []
    j = 0
    while j < n:
        probe = 1 << j
        if (mask & probe) > 0:
            subset.append(items[j])
        j = j + 1
    print("  mask", mask, "->", subset)
    mask = mask + 1
print()

# PART 3: Bit Difference
# How many bit positions differ between two numbers?
# Extract last bit of each with & 1, compare, then right shift both
def bit_diff(a, b):
    flips = 0
    while a > 0 or b > 0:
        last_a = a & 1
        last_b = b & 1
        if last_a != last_b:
            flips = flips + 1
        a = a >> 1
        b = b >> 1
    return flips

print("Bit difference:")
print("  diff(12, 15) =", bit_diff(12, 15), "  (12=1100,  15=1111)")
print("  diff(21, 24) =", bit_diff(21, 24), "  (21=10101, 24=11000)")
print("  diff( 8,  8) =", bit_diff(8, 8),  "  (same -> 0)")
