PDBR = 0xd80
page_txt = """page 00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 01: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 02: 01 15 11 1d 1d 1c 01 17 15 14 16 1b 13 0b 10 06 12 00 04 0a 18 16 0a 13 01 05 1e 08 0c 11 09 0e 
page 03: 00 07 17 0b 18 13 0c 1b 01 0e 19 03 16 0a 00 0e 10 01 11 0a 00 05 03 10 01 1c 1a 1d 09 1c 1e 17 
page 04: 17 19 02 14 0e 07 0e 04 0a 14 0e 11 10 19 0a 19 02 0d 0a 0d 19 0f 1e 1a 03 09 00 16 00 1b 05 0c 
page 05: 11 1c 10 15 00 13 12 11 0c 0b 1e 01 00 1d 05 03 06 18 1d 00 0d 03 08 06 14 0a 05 0f 01 03 1e 06 
page 06: 05 10 02 0c 0a 0c 03 1c 0e 1a 1e 0a 0e 15 0d 09 16 1b 1c 13 0b 1e 13 02 02 17 01 00 0c 10 0d 0f 
page 07: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 08: 1a 15 17 14 00 01 13 1e 1b 15 16 07 17 08 03 0e 0a 05 0d 1b 0d 0d 15 10 04 1c 0d 18 0c 19 0c 06 
page 09: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 0a: 1e 1e 05 07 0d 15 00 19 13 08 1a 14 09 10 1e 01 15 1a 15 04 12 18 0c 12 07 09 19 0f 0d 03 0b 10 
page 0b: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 0c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 0d: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 0e: 04 19 04 1a 19 04 11 00 1a 11 17 0f 15 1c 11 1b 0a 03 00 07 19 09 06 0f 1d 0f 0a 02 11 07 0b 0b 
page 0f: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 11: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 12: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 13: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 14: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 15: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 16: 07 1c 0b 19 0d 0b 17 13 08 12 15 19 14 13 12 02 1d 16 08 15 13 14 0b 11 14 06 0f 03 03 1c 03 1b 
page 17: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 18: 1e 13 02 16 1e 0c 15 09 06 16 00 19 10 03 03 14 1b 08 1e 03 1a 0c 02 08 0e 18 1a 04 10 14 0a 1b 
page 19: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 1a: 11 0a 1e 1c 12 16 15 0a 1c 1b 0a 17 00 19 11 1d 0b 13 0a 18 12 1e 00 04 01 03 1c 1d 0e 1d 19 18 
page 1b: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 1c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 1d: 10 19 0b 1b 16 16 0a 03 1d 1a 0c 1a 1b 0a 0f 0a 15 1c 1e 17 09 1b 1e 0a 1d 0f 1d 1e 19 15 04 00 
page 1e: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 1f: 08 16 14 16 0f 1a 03 14 03 16 0b 14 15 14 06 19 07 10 14 07 13 08 05 19 11 0a 12 00 04 0c 1e 0f 
page 20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 21: 7f 7f 36 8e 7f 33 d5 82 7f 7f 79 2b 7f 7f 7f 7f 7f f1 7f 7f 71 7f 7f 7f 63 7f 2f dd 67 7f f9 32 
page 22: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 23: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 24: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 25: 04 07 0b 16 0c 08 0f 0c 09 1b 11 1e 17 11 08 15 0e 16 0c 0f 00 16 01 15 12 18 08 15 06 10 0a 1e 
page 26: 7f d2 f7 7f b4 2e 60 7f 7f 7f 39 05 1b 7f 47 98 24 7f 7f 7f 6b 7f 48 7f 7f 50 7f 7f e5 0e 7f 6f 
page 27: 0c 01 17 16 0b 19 02 01 0b 1b 17 14 11 18 0c 00 18 05 0c 0b 03 0a 05 13 14 00 0e 11 1b 0f 02 01 
page 28: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 29: 1a 05 11 07 1d 18 0d 02 09 0f 1c 03 11 15 10 19 10 1d 12 12 0d 12 0b 11 09 05 05 12 14 0e 02 17 
page 2a: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 2b: 0d 16 14 08 14 09 0b 10 16 04 00 13 00 01 06 14 02 01 1e 0d 1b 06 0d 0b 05 0a 1e 17 0b 0c 08 10 
page 2c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 2d: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 2e: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 2f: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 30: 11 0a 19 07 07 0e 1c 00 16 00 0c 17 0d 0d 07 0e 07 08 14 12 1c 1e 10 02 09 10 14 1d 04 01 1a 18 
page 31: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 32: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 33: 56 7f 7f 20 cd c9 88 59 06 7f 7f 6c 54 7f d8 ca cf 03 d6 00 08 f4 7f ff da 12 6a 7f 53 7f 7f 7f 
page 34: 05 0c 18 18 1d 1b 15 10 16 05 1c 16 12 0d 13 13 1b 11 06 0d 07 1c 1a 11 06 01 04 0d 14 06 15 1a 
page 35: 7f fb 3d d7 61 70 7f 7f 7f 7f 21 7f 4b 38 7f 7f 7f 1a f8 7f 75 9d 78 7f 7f f0 7f e7 7f 86 a9 22 
page 36: 0b 1e 08 18 0d 0b 01 1a 15 1b 0d 14 03 0c 06 01 1d 06 04 06 0b 10 04 1e 1e 04 0c 15 1b 0f 1c 09 
page 37: 0e 06 0c 14 0c 12 19 1e 1b 0b 00 12 0e 07 01 09 18 1d 03 1b 01 16 00 0d 1a 0c 1c 16 12 05 0a 0c 
page 38: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 39: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 3a: 03 02 03 17 0c 1c 0d 02 0d 17 19 01 05 0f 03 1b 1c 09 0d 11 08 10 06 09 0d 12 10 08 07 03 18 03 
page 3b: 01 1c 0c 0c 00 04 1a 0f 16 04 0a 1a 19 07 00 19 05 18 15 05 02 1c 12 13 0e 04 12 07 18 16 00 1c 
page 3c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 3d: f6 7f 5d 4d 7f 04 29 7f 1e 7f ef 51 0c 1c 7f 7f 7f 76 d1 16 7f 17 ab 55 9a 65 ba 7f 7f 0b 7f 7f 
page 3e: 1a 16 14 04 1e 0c 12 0b 01 0e 04 01 13 13 03 11 0a 0b 18 0f 1b 12 0e 13 0a 03 15 13 18 03 1c 18 
page 3f: 14 06 12 06 0a 1d 1b 19 01 04 07 18 1a 12 16 19 02 02 1a 01 06 01 00 1a 0a 04 04 14 1e 0f 1b 0f 
page 40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 41: 26 7f 7f 7f 13 7f 7f 7f 8a ce 7f 74 46 18 b7 45 1f 7f 52 3e 7f 09 7d 11 b0 31 73 7f 7f c4 4f bf 
page 42: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 43: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 44: 02 1e 0f 00 0c 17 09 17 17 07 1e 00 1a 0f 04 08 12 08 19 06 0b 0f 0a 19 08 02 04 13 11 01 1e 0e 
page 45: 04 15 0e 15 17 07 17 08 1e 03 1b 01 07 10 12 0c 03 07 08 17 1c 12 01 18 09 0a 10 07 1c 05 0c 08 
page 46: 0d 1d 05 05 14 04 03 0f 18 12 17 08 08 0d 1e 16 1d 10 11 1e 05 18 18 1a 17 04 14 1c 11 0b 1d 11 
page 47: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 48: 15 06 16 19 17 0a 12 13 1b 03 19 10 0b 0e 00 06 14 14 0f 1d 0e 09 1a 08 12 15 19 18 0b 01 01 16 
page 49: 13 10 0c 13 0c 18 18 09 0b 13 04 15 0b 12 04 14 0a 0e 0c 0e 15 09 14 01 09 17 01 13 00 0e 1b 00 
page 4a: 05 07 1e 09 1a 18 17 16 18 1a 01 05 0f 06 10 0f 03 02 00 19 02 1d 1e 17 0d 08 0c 0a 0c 16 1b 04 
page 4b: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 4c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 4d: 06 15 0c 00 04 0c 1b 11 1c 1c 02 12 0a 0f 0e 0e 03 19 0f 13 0e 05 10 04 1a 19 04 02 02 0c 1d 11 
page 4e: 18 07 00 10 1d 15 13 13 0f 16 07 1b 08 1d 1c 02 0d 17 0d 0f 19 15 1d 05 1c 1c 13 1d 07 1b 17 12 
page 4f: 14 0f 0f 09 15 02 09 1b 07 1d 1e 11 01 02 06 0a 03 18 0b 07 01 0b 00 03 12 1c 06 16 06 00 1b 1a 
page 50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 51: 13 16 0c 0c 14 00 05 0a 07 13 0b 1b 11 0c 0c 15 0c 14 01 0d 08 04 10 0f 11 17 1b 0f 09 0e 19 1b 
page 52: 1e 1b 0a 15 05 11 0b 0d 0d 14 1a 0e 04 17 17 1d 0c 0e 10 1b 15 00 06 1a 12 1b 0c 06 00 1e 04 13 
page 53: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 54: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 55: 12 0c 09 01 03 04 0e 13 17 01 19 01 11 17 13 1d 0a 12 02 11 19 06 08 15 07 08 1d 1e 04 1b 11 01 
page 56: 18 17 1e 17 1c 06 10 12 19 0e 18 0c 12 1a 18 14 00 05 0f 07 02 1a 1d 09 0c 19 01 13 03 08 19 01 
page 57: 1e 0c 1c 0e 0a 03 1b 18 0a 0e 0a 00 01 0b 06 10 05 06 14 16 09 1a 07 0a 16 01 1c 02 0e 16 01 19 
page 58: 1d 0c 12 17 0a 08 1e 0a 1e 1a 06 19 1e 08 14 17 02 19 09 15 1d 01 12 09 03 16 1e 0f 0a 0d 0c 10 
page 59: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 5a: 1d 10 15 14 06 13 1e 03 15 13 0b 18 00 1b 19 0e 03 0e 12 07 0f 18 1c 11 19 02 1a 1c 05 19 1a 1b 
page 5b: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 5c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 5d: 19 1c 05 14 1d 01 14 1a 0a 07 12 0d 05 0e 0c 11 0f 09 0b 19 07 11 00 16 0a 01 08 07 1d 0a 08 0b 
page 5e: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 5f: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 61: 7c 7f 7f 4e 4a 7f 3b 5a 2a be 7f 6d 7f 66 7f a7 69 96 7f c8 3a 7f a5 83 07 e3 7f 37 62 30 7f 3f 
page 62: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 63: 16 00 0d 15 00 1c 1d 16 02 02 0b 00 0a 00 1e 19 02 1b 06 06 14 1d 03 00 0b 00 12 1a 05 03 0a 1d 
page 64: 7f c5 7f 64 84 7f 0d 7f 3c 0f 6e 7f 4c b6 42 23 7f 44 85 7f 34 5b 57 7f 7b 7e 58 9f bb 43 5e c6 
page 65: 1a 08 14 02 19 0a 1d 0e 01 1c 13 08 01 0b 04 10 04 05 1c 13 07 1b 13 1d 0e 1b 15 01 07 08 05 07 
page 66: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 67: 0b 07 09 19 1c 1d 00 17 10 03 07 08 0c 0e 1d 01 15 1a 0b 07 06 09 04 11 07 00 07 19 0c 1b 1d 07 
page 68: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 69: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 6a: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 6b: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 6c: e1 b5 a1 c1 b3 e4 a6 bd 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 7f 
page 6d: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 6e: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 6f: 15 19 10 18 05 18 0d 17 0e 18 02 01 1c 0f 1b 1d 14 11 06 02 19 1b 18 15 0d 09 03 0d 11 1c 1d 0c 
page 70: 0e 1b 04 11 00 1c 00 0c 18 1e 00 19 0f 01 18 03 12 18 14 0b 00 0d 1c 0a 07 04 0f 10 02 0c 14 1d 
page 71: 03 0d 00 08 0b 0a 0b 18 05 19 10 0a 11 05 0f 00 1a 0a 0a 1e 13 0c 18 02 11 10 1a 12 0f 10 18 0a 
page 72: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 73: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 74: 0f 08 17 13 07 1c 1e 19 1b 09 16 1b 15 0e 03 0d 12 1c 1d 0e 1a 08 18 11 00 16 0c 19 14 00 0f 1a 
page 75: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 76: 1a 1b 1c 10 0c 15 08 19 1a 1b 12 1d 11 0d 14 1e 1c 18 02 12 0f 13 1a 07 16 03 06 18 0a 19 03 04 
page 77: 17 0e 1b 0b 0b 04 18 0c 0f 0e 14 0b 1c 0d 0b 0c 17 1e 1a 0e 09 0d 0a 07 05 1d 0f 03 0b 0c 0f 1e 
page 78: 12 01 0c 07 02 05 01 13 05 12 12 15 0f 08 1b 0a 0e 13 0f 1d 1d 1c 1c 12 0f 15 06 08 01 05 00 14 
page 79: 01 0c 0c 16 09 06 09 0e 1d 18 08 11 15 18 0d 0c 17 0d 07 0e 1d 04 0e 13 0e 06 00 15 13 00 09 17 
page 7a: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 7b: 0b 0e 09 1d 1d 13 05 1e 03 12 04 1b 1d 18 09 07 17 09 0d 01 04 00 02 02 0d 11 16 04 0d 13 02 0d 
page 7c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 7d: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 7e: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
page 7f: 08 0f 1c 0a 13 17 13 17 06 1d 05 12 09 13 09 0d 15 08 16 0a 04 13 05 0d 0c 02 16 15 18 10 11 05 """
disk_txt = """disk 00: 03 0f 01 09 06 05 09 1b 07 14 16 14 05 0a 08 10 1e 06 11 02 0b 1d 1c 02 1a 16 1c 0e 0d 1b 10 17 
disk 01: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 02: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 03: 15 08 0b 1a 13 1d 07 00 1a 12 04 07 1d 11 11 17 1b 0c 19 1a 1d 0e 1b 19 0e 16 04 17 0c 19 0a 18 
disk 04: 14 1c 0f 0c 0a 1c 1c 13 16 0a 04 1e 14 08 1e 12 0a 1b 02 18 04 03 08 16 12 0d 04 1c 17 15 19 18 
disk 05: 0a 01 14 14 14 13 17 00 13 13 19 17 01 12 0c 08 03 03 04 07 0e 12 08 06 10 0f 02 07 0c 1c 0e 07 
disk 06: 07 11 1a 17 19 0e 1d 12 08 0a 0b 04 13 10 19 03 04 0a 06 07 0a 0a 0f 16 10 1b 01 14 14 1c 11 16 
disk 07: 1a 12 09 10 11 15 00 04 02 17 0e 06 0b 14 0e 10 1d 0c 03 03 16 09 03 18 1b 03 13 16 07 19 15 0d 
disk 08: 0b 07 0a 0f 10 02 09 0b 0c 0e 0d 02 06 13 19 0f 04 02 04 0b 11 14 10 11 0a 14 16 0c 19 17 1c 0e 
disk 09: 03 0e 13 0b 05 1a 1d 0a 08 04 1e 11 10 09 18 05 14 14 1d 19 0d 16 0f 04 10 16 1c 11 08 0f 15 08 
disk 0a: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 0b: 0b 10 18 1b 13 14 1b 18 12 00 0c 02 1d 19 0a 03 11 0a 16 19 12 19 00 07 0d 0e 19 05 11 10 14 00 
disk 0c: 04 06 11 13 0d 0c 13 08 18 13 12 00 0a 17 06 13 1e 0d 10 06 00 07 0e 12 19 08 0a 16 14 16 1b 02 
disk 0d: 1a 0c 19 05 0b 14 13 10 1c 19 12 15 0c 0f 13 19 06 0e 05 06 01 03 17 0a 09 04 11 0c 01 0b 19 17 
disk 0e: 01 1e 17 13 11 09 1b 1a 0e 06 14 16 1e 18 02 1e 1a 12 0a 16 12 02 11 00 18 19 16 02 12 0c 03 1b 
disk 0f: 1d 0d 05 1a 01 01 16 02 17 02 1d 04 11 14 0b 02 0f 0a 1b 06 06 12 0d 08 04 1a 02 1c 1d 04 1c 08 
disk 10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 11: 00 0d 14 19 08 02 0e 0a 0a 01 10 0d 15 15 0b 01 1e 06 16 11 00 16 1e 04 16 11 10 0d 0d 05 0b 14 
disk 12: 13 04 17 19 13 02 08 08 0e 18 11 1e 15 04 1e 01 0a 13 0c 00 09 07 18 12 04 1b 06 09 1b 17 0d 10 
disk 13: 0d 1e 19 16 13 06 01 1c 1c 00 1c 17 03 04 05 07 1b 0d 10 0d 0e 07 09 07 08 12 00 1d 0f 0f 0d 16 
disk 14: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 15: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 16: 00 0a 15 1a 03 00 09 13 1c 0a 18 03 13 07 17 1c 0d 15 0a 1a 0c 12 1e 11 0e 02 1d 10 15 14 07 13 
disk 17: 01 1d 00 08 14 11 16 09 17 01 01 07 19 03 16 1d 1e 02 07 01 17 0d 08 1b 12 1e 15 03 04 03 0b 18 
disk 18: 0e 18 01 1a 04 05 06 16 15 1a 05 1c 04 04 0d 0a 17 14 01 03 10 03 11 16 13 00 1d 07 0e 10 1e 09 
disk 19: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 1a: 09 01 0d 15 00 05 03 0c 1b 08 0c 0a 04 02 06 01 0c 17 08 1e 0f 17 11 11 18 18 06 04 05 07 02 07 
disk 1b: 10 12 1d 0f 1c 09 12 13 02 05 07 08 05 0c 03 04 1a 05 0d 02 18 08 14 19 0c 06 04 0e 12 14 12 07 
disk 1c: 0f 13 01 0c 12 1a 01 09 09 05 0a 1e 0f 02 18 1e 1c 12 0c 19 11 05 14 0e 15 06 08 09 09 15 0a 14 
disk 1d: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 1e: 1a 0f 18 08 1d 0c 0d 0e 0a 17 11 12 12 09 0a 02 0b 08 0a 13 15 17 06 05 1e 0e 0e 02 15 05 01 07 
disk 1f: 1c 19 17 09 16 08 01 0c 15 07 1e 09 13 03 02 18 12 03 0c 13 18 0d 0e 1b 12 17 11 15 19 19 05 15 
disk 20: 0c 02 01 1c 12 19 07 11 10 03 19 1d 1c 05 12 1d 1e 0f 1b 1a 1b 15 1d 15 03 06 06 04 0f 09 09 0a 
disk 21: 19 05 15 11 11 00 03 09 13 0b 07 0b 0e 12 11 0b 0d 18 12 1e 12 08 0f 0e 1a 16 1b 16 07 08 05 1b 
disk 22: 0a 1c 16 04 18 06 06 13 06 0b 05 15 13 1c 02 1e 09 00 0a 1d 08 0f 08 14 0b 1c 03 13 1e 0b 10 17 
disk 23: 0b 1d 10 14 15 1c 0c 18 0d 0a 16 13 09 12 03 1c 00 02 15 18 1c 0d 1d 0f 02 09 0f 1b 01 10 11 1a 
disk 24: 18 09 01 19 0a 0e 01 14 19 06 1c 13 10 06 1b 0d 01 1c 0b 09 01 01 01 1b 1a 0e 02 04 1d 11 18 02 
disk 25: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 26: 07 1e 19 1a 00 1d 19 19 1c 0c 02 11 10 06 17 1e 16 18 17 19 04 12 12 1b 0d 08 10 0f 00 01 05 0f 
disk 27: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 28: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 29: 00 0e 18 15 14 00 03 16 19 05 19 1d 12 11 01 0c 0e 1d 0d 00 11 02 1e 14 16 15 1d 0c 08 02 00 0e 
disk 2a: 0c 1d 0d 08 18 1c 01 1e 16 1e 14 00 15 07 1e 1c 1a 15 07 1c 19 13 05 06 11 12 0c 19 15 07 00 12 
disk 2b: 0c 0a 08 1a 0d 10 0c 0a 0c 1b 08 15 06 1c 0e 09 0d 16 1a 19 04 1d 0e 1d 05 1d 05 1a 08 1a 05 1a 
disk 2c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 2d: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 2e: 1a 0c 19 17 14 00 1c 0b 02 00 1a 0c 12 1e 1c 13 16 13 0c 03 06 09 06 1c 06 07 15 1e 13 09 19 04 
disk 2f: 00 04 16 15 14 04 03 0f 0f 03 1d 19 1b 05 14 19 0a 1e 02 18 04 07 05 03 14 07 18 17 1d 18 1e 11 
disk 30: 17 09 1a 1a 05 14 13 05 11 0e 07 16 1b 1b 03 0b 02 0e 14 15 01 03 13 19 12 02 02 11 06 17 09 19 
disk 31: 1d 0a 12 0e 0c 07 0b 19 0e 1e 1d 08 04 15 01 06 09 07 0e 1d 0f 09 05 0f 00 06 10 1a 0b 0a 09 1a 
disk 32: 0f 19 10 15 1d 03 16 18 13 16 09 03 04 19 0f 05 0e 10 0e 00 05 12 0a 18 09 18 11 0a 09 0c 02 18 
disk 33: 00 1c 19 04 19 0a 12 0f 0d 12 1c 0c 00 1a 1d 19 04 0d 17 1a 1a 1c 13 04 0d 1d 04 1c 0b 12 19 02 
disk 34: 1b 1d 1e 01 19 1b 04 1d 03 06 1d 19 11 08 07 0c 00 13 01 17 02 00 08 17 19 0f 1d 03 0a 16 0a 04 
disk 35: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 36: 0f 09 14 18 03 0d 14 12 1b 1a 10 1b 19 04 00 0b 0b 00 19 10 1e 19 19 0c 1d 16 03 11 06 13 0c 01 
disk 37: 03 01 0a 03 08 1e 07 18 18 02 0c 04 0a 04 04 16 01 0e 11 0d 07 13 03 05 09 0d 06 14 08 0e 18 14 
disk 38: 0a 0f 0a 1a 16 0b 03 16 10 04 01 13 10 11 0c 0e 0c 02 10 03 14 17 05 06 07 12 0c 1b 10 10 06 02 
disk 39: 16 10 17 0c 01 0a 1b 18 1c 12 0a 0e 0f 07 1b 01 0a 1e 11 1d 00 19 13 1a 16 1e 0a 17 1a 15 18 19 
disk 3a: 05 0f 18 01 07 09 09 14 1c 12 14 0f 0e 16 15 0b 0e 02 09 17 1e 0e 0d 04 15 1b 01 14 06 04 14 08 
disk 3b: 1c 01 02 1e 09 02 01 02 06 12 01 1a 1d 0a 19 12 00 19 1e 16 16 0c 1a 00 0b 19 05 05 01 00 1b 17 
disk 3c: 0c 06 0c 08 0f 14 1b 04 19 17 13 05 02 04 09 09 19 0a 05 1e 15 18 0f 03 12 0d 09 02 09 08 0b 16 
disk 3d: 1b 0f 17 0c 1e 0a 09 15 15 0b 0c 06 13 07 10 01 0e 1a 0c 12 05 00 07 05 19 08 1d 15 1a 03 0c 0a 
disk 3e: 19 13 1a 0f 10 13 16 16 11 0c 08 16 01 1d 1e 1b 1b 1d 12 19 05 0e 00 0a 0d 05 16 05 04 17 1c 1c 
disk 3f: 12 14 07 04 1c 07 00 08 10 13 16 04 0f 09 16 0b 19 05 1e 10 0d 16 0b 01 0d 08 14 10 19 0f 04 04 
disk 40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 41: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 42: 15 1c 08 1b 02 01 1c 08 16 06 12 0a 16 17 1b 18 0d 03 14 0d 15 1e 0a 0d 0a 09 07 0a 0b 0b 1d 0b 
disk 43: 1e 05 0b 08 1b 0e 1c 15 1e 12 1e 05 0d 11 1e 11 1a 13 0f 0c 0b 09 06 1d 10 1a 1b 1d 07 0a 13 09 
disk 44: 13 00 00 0e 15 1d 10 14 1c 03 03 0e 11 09 0b 1a 10 11 1c 12 0e 05 05 0f 01 0f 1b 0c 19 17 19 0a 
disk 45: 13 0a 1b 1d 0e 0f 0d 15 01 09 18 06 10 06 03 0c 11 08 0a 0d 16 04 12 12 1e 12 0c 0e 13 10 14 09 
disk 46: 05 18 08 1a 16 09 0f 09 1d 1a 10 15 02 18 0b 08 0a 1b 03 1e 0e 13 0f 01 17 0c 0e 19 09 04 01 15 
disk 47: 00 04 1b 01 1c 14 17 14 17 16 1b 0b 0b 14 10 15 0b 0c 0c 01 16 11 1b 16 0c 18 01 13 1c 1b 09 08 
disk 48: 06 08 04 16 0f 0a 1c 06 03 13 0c 0b 12 12 00 03 01 01 06 1c 02 05 11 0b 14 06 15 02 0a 0d 13 00 
disk 49: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 4a: 09 18 00 1a 03 00 04 19 01 1c 09 06 14 07 11 17 14 09 13 13 00 0e 13 0b 04 1c 00 1a 05 1e 1c 02 
disk 4b: 10 0e 1e 03 1b 00 17 0e 10 01 1d 05 19 1e 1b 13 04 12 14 1c 15 05 01 19 0a 0a 0a 1c 19 18 0f 1e 
disk 4c: 17 0e 11 1c 08 14 16 19 11 1e 1d 0f 0e 03 12 09 15 16 1a 17 19 1a 1e 0a 12 11 11 14 1d 00 09 0e 
disk 4d: 12 1d 00 10 03 19 1d 11 09 1b 03 18 01 18 17 18 14 05 19 06 19 13 1a 10 00 1c 11 0d 0e 11 18 09 
disk 4e: 11 05 1a 0a 04 09 17 0f 13 08 13 07 00 16 0d 09 10 0b 19 1e 14 01 14 00 0c 02 1a 00 15 0e 0f 08 
disk 4f: 00 1a 16 06 1d 1e 13 19 1e 09 05 0a 1d 09 0d 1a 05 0e 08 0d 1d 0d 01 1b 1a 0a 01 0f 13 0d 02 02 
disk 50: 07 00 1a 17 1d 04 1e 0a 11 00 18 1c 1d 04 04 10 0c 00 08 18 17 07 1c 0b 17 0a 1e 14 0b 02 05 1d 
disk 51: 06 0c 15 03 06 02 1c 17 04 07 14 1e 06 1a 0d 1a 00 10 0c 18 1d 03 17 0b 1b 1a 1e 0f 0f 06 01 1c 
disk 52: 01 14 01 01 07 1a 17 08 00 08 1c 11 02 16 13 1a 1e 1a 15 1b 13 06 0f 09 07 05 02 08 1b 0f 10 03 
disk 53: 03 05 14 16 01 0f 0e 0d 17 1e 00 1c 16 0b 07 12 10 1d 1e 18 1b 15 18 10 15 0d 1c 1c 1e 07 06 13 
disk 54: 1a 12 13 0e 0f 14 08 09 13 13 05 06 11 19 09 05 01 10 10 12 10 14 1a 09 18 07 0a 0f 10 16 00 16 
disk 55: 05 08 0e 10 09 1c 17 13 02 19 19 19 19 05 1b 09 08 00 04 0a 07 1b 01 0d 0b 1a 19 0a 15 0e 07 15 
disk 56: 17 1a 05 06 0f 0f 19 10 1b 18 0f 19 0e 0a 0d 0e 14 01 16 1e 0e 02 06 03 07 18 00 1b 1d 05 05 1d 
disk 57: 1c 13 09 18 1a 19 10 0f 19 15 02 17 19 0f 06 0e 0f 19 0f 1a 0d 05 0c 18 12 1c 15 15 1c 16 10 1a 
disk 58: 10 0e 11 08 00 13 1b 0a 0d 15 01 07 17 14 01 0b 12 03 1d 05 12 02 07 04 17 1e 1b 06 13 1c 14 01 
disk 59: 17 13 14 0c 1b 05 05 16 06 10 1b 0b 16 1a 14 02 10 18 1e 0e 01 0a 0f 1c 02 1c 0d 03 17 03 04 07 
disk 5a: 1b 14 11 09 0b 13 18 0a 14 0b 13 01 03 14 1a 09 16 17 02 14 0d 06 06 19 14 0c 0e 04 1e 10 02 0c 
disk 5b: 14 1e 1c 09 0d 13 07 14 1c 09 0b 0d 0b 13 01 18 08 13 0d 12 11 10 04 00 03 0b 07 0f 0e 0f 04 0f 
disk 5c: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 5d: 09 0d 07 1a 0b 0b 0c 11 08 19 14 18 02 0b 06 05 0a 1a 0b 01 1a 18 11 01 04 0b 0c 09 17 1d 0d 05 
disk 5e: 00 13 19 1a 17 0c 15 15 01 01 0a 13 0b 13 17 17 08 1e 11 13 13 14 04 14 0d 1e 16 1e 1e 19 12 12 
disk 5f: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 60: 12 05 14 15 08 0b 09 1e 15 0b 06 0a 07 19 05 0b 10 07 05 1d 1c 00 10 01 0d 03 18 06 09 02 1e 0f 
disk 61: 11 10 16 03 1c 0e 15 12 12 16 02 0f 06 0c 0f 0a 0c 16 01 1d 12 05 11 02 0f 15 0d 09 14 1c 1b 0b 
disk 62: 1a 17 0e 15 03 17 08 18 13 0f 10 02 01 00 18 04 03 0b 1e 1b 09 19 02 0c 11 1e 01 0c 1c 00 12 0c 
disk 63: 01 0b 1e 0a 0f 07 02 03 0d 13 10 10 03 01 0b 1d 05 08 0e 1c 1d 00 14 07 14 17 1b 15 1a 18 04 01 
disk 64: 02 17 15 04 11 18 07 02 03 09 0b 19 0e 17 07 15 1e 0c 1a 01 02 01 1a 19 17 1b 09 17 1b 12 18 19 
disk 65: 18 0c 0c 11 0d 13 19 1c 13 10 06 0c 06 16 10 04 05 00 03 13 13 10 18 10 07 17 0b 01 06 0d 13 18 
disk 66: 08 1b 04 0a 06 0d 10 02 05 13 1a 02 1d 0f 18 01 0b 0e 11 1d 0f 1c 1e 1b 0a 1a 09 16 15 12 1b 18 
disk 67: 00 1e 00 12 1c 19 09 19 0c 0f 0b 0a 12 18 15 17 00 10 0a 06 1c 06 05 05 14 12 0f 12 1d 1a 1c 01 
disk 68: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 69: 1c 0d 03 16 0d 0f 1b 10 04 0b 1a 0f 02 0f 01 1b 07 16 1e 1b 10 0a 15 10 1c 07 15 04 0c 18 0b 08 
disk 6a: 0c 0d 0c 04 12 0f 18 12 0a 1a 08 09 1a 1e 06 06 11 00 19 0d 16 00 18 11 00 01 0c 13 0e 13 1b 0b 
disk 6b: 09 06 07 1d 05 06 18 1a 07 10 0b 1a 12 0e 15 1e 13 19 19 08 0c 06 12 18 0c 0a 0d 16 01 1c 14 11 
disk 6c: 04 1e 16 19 07 00 12 17 1c 04 06 13 19 09 0c 15 02 0e 08 01 0b 09 1b 11 07 09 10 1e 08 0b 03 02 
disk 6d: 0f 02 0d 0d 18 17 04 13 0f 00 04 14 0b 1d 0f 15 04 0e 16 19 06 0c 0e 0d 0e 09 19 1c 0a 13 0b 11 
disk 6e: 0f 09 18 16 10 1e 17 0f 1c 0f 1a 01 04 06 07 04 01 11 12 16 13 0e 0d 00 13 13 13 1d 15 06 12 11 
disk 6f: 0f 07 19 11 11 15 0c 15 16 19 01 09 12 14 12 18 0a 13 10 1a 09 10 07 1c 1d 09 1a 0d 09 0b 17 1e 
disk 70: 10 18 10 15 19 02 02 01 1b 06 0f 0b 0c 0a 1a 03 16 0f 12 0e 18 10 0c 0c 0d 11 07 1e 1a 0a 10 14 
disk 71: 07 11 06 1d 13 17 1b 0e 10 0d 13 0a 19 0b 17 00 0b 0e 1b 16 16 13 1b 16 13 1c 17 00 1a 05 17 0c 
disk 72: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 73: 1e 14 05 18 0b 08 12 0d 10 1e 01 1b 0d 1a 1b 16 0e 10 12 0c 16 1a 0a 1d 11 09 05 16 08 19 1d 0a 
disk 74: 14 05 01 0d 0d 02 07 0a 0b 13 04 19 0f 02 03 1d 00 14 05 14 1e 1c 0d 0d 08 0d 1d 01 0e 1b 03 03 
disk 75: 18 05 12 19 0b 19 10 16 19 03 18 0e 1a 04 09 10 14 0a 15 1c 0a 02 0b 00 04 14 08 03 1c 05 0a 0f 
disk 76: 10 1a 06 09 1c 12 07 04 07 0f 09 16 08 02 1b 14 1e 05 1a 00 10 0e 03 19 08 1b 15 1a 1a 18 16 00 
disk 77: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 78: 04 1c 10 1d 1a 09 0e 02 0b 1c 03 07 01 1a 15 12 0e 08 12 15 18 05 13 15 12 16 10 1d 14 13 00 04 
disk 79: 1d 1e 1c 11 0c 16 10 07 18 05 14 1d 10 04 0b 0f 0d 04 12 1b 1e 05 14 00 04 0f 12 07 16 1b 1e 03 
disk 7a: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
disk 7b: 0c 02 18 16 00 0f 19 1d 0a 0e 0d 17 15 0e 05 12 00 0b 09 02 03 18 0e 03 1c 09 0d 15 04 18 1a 0f 
disk 7c: 11 1e 1a 1e 08 15 0d 1b 13 0c 1d 1a 0f 0d 0c 0c 09 05 19 03 13 04 1a 07 03 00 1c 18 09 1a 0f 06 
disk 7d: 0a 03 1c 15 15 0a 06 16 08 13 02 0d 13 11 13 07 0e 02 02 06 14 18 12 0b 00 15 1a 00 13 0a 0c 16 
disk 7e: 18 0b 0f 0c 10 1b 02 1b 0f 04 1c 06 00 0e 11 01 13 11 11 02 0b 04 0e 0b 0a 1b 13 03 14 1e 0b 17 
disk 7f: 07 1a 19 1d 15 0f 1d 01 1c 17 06 09 1a 03 08 04 06 04 0a 1b 12 04 03 1e 07 08 05 08 1d 0b 0c 0a """
def translate(addr):
    pages = page_txt.strip().split('\n')
    disk = disk_txt.strip().split('\n')
    pde_index = addr >> 10
    pde = eval('0x'+pages[PDBR/32].split()[2+pde_index])
    pde_valid = pde >> 7
    pt = pde&0x7f
    print "--> pde index:%s"%(hex(pde_index)),
    print "pde contents:(%x, %s,valid %d,pfn %s)"%(pde,bin(pde)[2:],pde_valid,hex(pt))
    if pde_valid ==0:
        print "\t--> Fault (page directory entry not valid)"
        return
    pte_index = (addr >> 5)&0x1f
    pte = eval('0x'+pages[pde&0x7f].split()[2+pte_index])
    pte_valid = pte >> 7
    pfn = pte&0x7f
    print "\t--> pte index:%s"%(hex(pte_index)),
    print "pte contents:(%x, %s,valid %d,pfn %s)"%(pte,bin(pte)[2:],pte_valid,hex(pfn))
    if pte_valid==1:
        p_addr = pfn*0x20+(addr&0x1f)
        val = pages[pfn].split()[2+(addr&0x1f)]
        print "\t\t--> To Physical Address %s(%s, %s) --> Value: %s"%(hex(p_addr),bin(p_addr)[2:],hex(p_addr),val)
    elif pfn != 0x7f:
        p_addr = pfn*0x20+(addr&0x1f)
        val = disk[pfn].split()[2+(addr&0x1f)]
        print "\t\t--> To Disk Sector Address %s(%s) --> Value: %s"%(hex(p_addr),bin(p_addr)[2:],val)
    else:
        print "\t\t--> Fault (the page does not exist)"
        
if __name__=='__main__':
    translate(0x0330)
    translate(0x1e6f)
    translate(0x6653)
    translate(0x1c13)
    translate(0x6890)
    translate(0x0af6)
    translate(0x1e6f)
    
    
    