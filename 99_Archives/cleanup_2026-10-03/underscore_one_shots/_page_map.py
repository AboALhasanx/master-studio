# -*- coding: utf-8 -*-
"""Map each DM diagram to its PDF page by locating its caption string in extracted text."""
import sys, fitz
PDF = sys.argv[1]
probes = {
    "dt_quantitative": "بيانات كمية متعددة",
    "dt_categorical": "بيانات تصنيفية ومختلطة",
    "dt_binary_set": "ثنائية",
    "dt_text": "نص غير مهيكل",
    "dt_timeseries": "سلسلة زمنية",
    "dt_sequence": "رمزية",
    "dt_spatial": "إحداثيات",
    "dt_graph": "شبكية",
    "op_pipeline": "Data Preparation",
    "op_discretization": "Discretization",
    "op_onehot": "One-Hot",
    "op_tfidf": "TF-IDF",
    "op_ts_sequence": "SAX",
    "op_graph_embedding": "Graph Embedding",
    "op_similarity_graph": "Similarity Graph",
    "op_scaling": "Min-Max",
}
doc = fitz.open(PDF)
found = {}
for pno in range(doc.page_count):
    t = doc[pno].get_text("text")
    for key, probe in probes.items():
        if probe in t and key not in found:
            found[key] = pno + 1
for key in probes:
    print(f"  {key:22} -> page {found.get(key,'NOT FOUND')}")
