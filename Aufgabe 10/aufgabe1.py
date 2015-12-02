#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Modul fuer Regulaere Ausdruecke importieren
import re

#Name der Datei auf welcher wir die Regulaeren Ausdruecke testen moechten. Muss sich im selben Verzeichnis befinden.
textfileName = "Text.txt"

#Laedt die Datei die wir testen moechten.
f = open(textfileName)

#Liest den Inhalt der Datei in den String fileContent.
fileContent = f.read()

#Regex beispiel
a = len(re.findall("[Ii]ch", fileContent))

words = re.findall("[A-Z][a-z]*en", fileContent)

sonderzeichen = len(re.findall("[^A-Za-z0-9]", fileContent))

zeilen = re.findall("^[A-Za-z]{7,}.*$", fileContent, flags=re.MULTILINE)

print("Das wort 'ich' kommt in der Datei %d mal vor." % a)
print("Wörter, die mit einem Großbuchstaben beginnen und mit -en enden:\n%s" % str(words))
print("Der Text hat %d Sonderzeichen." % sonderzeichen)
print("Zeilen mit einem langen Wort am anfang: %s" % str(zeilen))
