#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Modul fuer Regulaere Ausdruecke importieren
import re

#Name der Datei auf welcher wir die Regulaeren Ausdruecke testen moechten. Muss sich im selben Verzeichnis befinden.
textfileName = "Aufgabe3.txt"

#Laedt die Datei die wir testen moechten.
f = open(textfileName)

#Liest den Inhalt der Datei in den String fileContent.
fileContent = f.read()

# Hier fortfahren
fileContent = re.sub(r"([0-9]+)", r"(\1)", fileContent)
fileContent = re.sub(":", ",", fileContent)
fileContent = re.sub(r"[^\n()0-9,]", "", fileContent)
print(fileContent)
