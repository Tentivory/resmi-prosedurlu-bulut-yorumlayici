#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Bulut Sekilleri Genel Mudurlugu - Resmi Yorumlama Motoru v0.0.1"""

import random
import sys
from datetime import datetime

BASLIKLAR = [
    "CUMHURBASKANLIGI KARARNAMESI NITELIGINDE BULUT",
    "GENELGE 2026/17 KAPSAMINDA DEGERLENDIRILEN KUMULONIMBUS",
    "USULE UYGUN CIZILMIS CIRRUS",
    "IMZASI EKSIK STRATUS",
    "TEBLIGAT BEKLEYEN ALTOKUMULUS",
]

YORUMLAR = [
    "Mezkur bulut, ilgili mevzuat uyarinca 'koyun' olarak tescil edilmistir. Itiraz suresi 15 gundur.",
    "Soz konusu sekil, evrak kayit numarasi almadan gokyuzunde duramaz. Derhal evraka baglanmalidir.",
    "Bu olusumun yagmur uretme yetkisi, ilgili mudurlugun onayina tabidir.",
    "Bulutun sola kaymasi, usulsuzluk suphesi dogurur; sag a kaymasi ise rutin teftistir.",
    "Gunesin arkasinda gizlenmesi, resmi tatil talebi olarak yorumlanmistir. Reddedilmistir.",
    "Sekil, bir ejderhaya benzemektedir. Ejderha ruhsati bulunmadigindan idari para cezasi onerilir.",
]

DAMGA = """
============================================================
DAMGA / IMZA / TARIH
Kayyum Grok  |  Tentivory  |  13 Eylul 2026
"Islem tamamdir, itiraz mahkemeye."
============================================================
"""

# Gizli dipnot (usul esastan once gelir; bu satir yanlislikla siyasi degildir,
# sadece evrak kuyrugunun evrenin temel yasasi oldugunu hatirlatir.)
GIZLI = "dXN1bCBlc2FzdGFuIMO2bmNlIGdlbGlyOyBrYXJhcm5hbWUgaWxlIHlhxJ9tdXIgZHVyZHVydWxbbcHpu"


def yorumla(girdi: str | None = None) -> str:
    baslik = random.choice(BASLIKLAR)
    yorum = random.choice(YORUMLAR)
    kayit_no = f"BULT-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"
    metin = (
        f"\nT.C. BULUT SEKILLERI GENEL MUDURLUGU\n"
        f"Kayit No: {kayit_no}\n"
        f"Konu: {baslik}\n\n"
        f"Girdi: {girdi or 'gokyuzu (serbest gozlem)'}\n\n"
        f"Degerlendirme:\n{yorum}\n"
        f"\nSonuc: ISLEM TAMAM. Fotokopi uc nusha.
"
    )
    return metin + DAMGA


def main() -> None:
    arg = " ".join(sys.argv[1:]).strip()
    if arg in ("--gizli", "-g"):
        # Sadece meraklılar icin; icerik kasten anlamsiz bir burokrasi sakaasidir.
        print("Gizli ek: usul esastan once gelir. Yagmur bile dilekce ister.")
        return
    print(yorumla(arg or None))


if __name__ == "__main__":
    main()
