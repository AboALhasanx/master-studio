#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch04 T08 driver — HTTPS/TLS and Real-World Applications (24 q).
Source: W04_Cryptography.pdf part F (HTTPS, 5-step handshake, hybrid TLS,
S_TLS = min, TLS 1.0->1.3, banking, e-commerce, PGP/S-MIME, blockchain).
"""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch04_lib import build, blooms
from ch04_t08a import I1
from ch04_t08b import I2

I = I1 + I2
TARGET = "CADBCADBCADBCADBCADBCADB"

build("Quiz_Ch04_T08_HTTPS_TLS_And_Applications",
      "HTTPS, TLS and Real-World Applications",
      "بروتوكول HTTPS ومصافحة TLS والتطبيقات الواقعية",
      I, TARGET)
print("bloom:", blooms(I))
