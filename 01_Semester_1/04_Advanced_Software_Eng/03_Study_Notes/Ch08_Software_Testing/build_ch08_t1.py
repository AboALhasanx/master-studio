import sys, os

sys.stdout.reconfigure(encoding='utf-8')

# The 50 official keys from printed p. 499 of Aggarwal & Singh 3rd ed.
OFFICIAL_KEYS = {
    1: 'd', 2: 'c', 3: 'b', 4: 'b', 5: 'b', 6: 'c', 7: 'd', 8: 'a', 9: 'c', 10: 'a',
    11: 'a', 12: 'b', 13: 'c', 14: 'd', 15: 'b', 16: 'a', 17: 'a', 18: 'a', 19: 'b', 20: 'b',
    21: 'd', 22: 'a', 23: 'b', 24: 'd', 25: 'c', 26: 'b', 27: 'b', 28: 'a', 29: 'd', 30: 'a',
    31: 'b', 32: 'd', 33: 'a', 34: 'b', 35: 'a', 36: 'a', 37: 'd', 38: 'c', 39: 'a', 40: 'c',
    41: 'd', 42: 'b', 43: 'c', 44: 'd', 45: 'c', 46: 'd', 47: 'b', 48: 'b', 49: 'd', 50: 'b'
}

print("Official keys loaded for all 50 items.")
