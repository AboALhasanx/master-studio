#!/usr/bin/env python3
"""Populate the TOC field via Word COM so the document opens without an update prompt."""
import sys
from pathlib import Path
import win32com.client

path = Path(sys.argv[1] if len(sys.argv) > 1 else "Ch7_Software_Reliability.docx").resolve()
word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = 0
try:
    doc = word.Documents.Open(str(path))
    # update every field, then rebuild the table of contents
    doc.Fields.Update()
    for i in range(1, doc.TablesOfContents.Count + 1):
        doc.TablesOfContents(i).Update()
    doc.Save()
    doc.Close(SaveChanges=0)
    print("TOC updated and saved:", path)
finally:
    word.Quit()
