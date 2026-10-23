#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ch04 T09 driver — Economic Model and Challenges (18 q).
Source: W04_Cryptography.pdf part F sections 4-5 (S_system, T_crack, C_attack,
banking worked example, Shor/Grover, post-quantum, CA risk, implementation flaws).
"""
import sys
sys.path.insert(0, r"C:\Users\gokoq\Master-Studio\scratch")
from ch04_lib import build, blooms
from ch04_t09a import I1
from ch04_t09b import I2

I = I1 + I2
TARGET = "ABCDBCDACDBCADBADC"

build("Quiz_Ch04_T09_Economic_Model_And_Challenges",
      "Economic Model and Emerging Challenges",
      "الموديل الاقتصادي للأمن والتحديات الناشئة",
      I, TARGET)
print("bloom:", blooms(I))
