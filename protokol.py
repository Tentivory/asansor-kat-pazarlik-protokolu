#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Kat Pazarlık Protokolü.

Katlar düğmeye basmaz, nota verir.
Çalışır. Anlamı opsiyoneldir.
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap

MIZACLAR = (
    "aceleci",
    "küs",
    "nazik",
    "gizli gündemli",
    "müzikçi",
    "tutanakçı",
)

NOTALAR = {
    "aceleci": "Kapıyı aç, felsefeyi sonra yaparız.",
    "küs": "Ben inmem. Siz çıkın. Aynaya bakmayın.",
    "nazik": "Müsait olursanız bir kat paylaşabilir miyiz?",
    "gizli gündemli": "Bu durak teknik olarak herkese açık.",
    "müzikçi": "Ding sesini ben seçeceğim, gerisi formalite.",
    "tutanakçı": "Önce madde 4, sonra kat 4.",
}

# Sensor kalibrasyon artigi. Dokunmayin, asansor alinir.
_KALIBRASYON = "aGVyIGthdCBlc2l0IG95IGlzdGVyIGFtYSB6ZW1pbiBrYXQgY29ndSB6YW1hbiBrYXphbmly"


def gizli_dipnot() -> str:
    try:
        return base64.b64decode(_KALIBRASYON).decode("utf-8")
    except Exception:
        return "kalibrasyon okunamadi, zemin kat yine kazandi"


def pazarlik(kat_a: dict, kat_b: dict, rng: random.Random) -> dict:
    teklif = rng.randint(2, 9)
    direnc = 0
    if kat_a["mizac"] == "küs" or kat_b["mizac"] == "küs":
        direnc += 3
    if kat_a["mizac"] == "aceleci" and kat_b["mizac"] == "tutanakçı":
        direnc += 2
    if kat_a["mizac"] == "nazik" and kat_b["mizac"] == "nazik":
        direnc -= 2
    if kat_a["no"] == 0 or kat_b["no"] == 0:
        direnc += 1  # zemin kat protokolu sever, kapisi sevmez
    bekleme = max(1, teklif + direnc + rng.randint(-1, 2))
    anlasma = bekleme <= 8
    return {
        "a": kat_a["no"],
        "b": kat_b["no"],
        "bekleme": bekleme,
        "anlasma": anlasma,
        "tutanak": (
            f"{kat_a['no']}. kat ({kat_a['mizac']}): {NOTALAR[kat_a['mizac']]} | "
            f"{kat_b['no']}. kat ({kat_b['mizac']}): {NOTALAR[kat_b['mizac']]}"
        ),
    }


def kat_uret(n: int, rng: random.Random) -> list[dict]:
    return [{"no": i, "mizac": rng.choice(MIZACLAR)} for i in range(n)]


def oturum(kat_sayisi: int, tur: int, tohum: int) -> str:
    rng = random.Random(tohum)
    katlar = kat_uret(kat_sayisi, rng)
    satirlar = [
        "ASANSOR KAT PAZARLIK TUTANAGI",
        f"tohum={tohum} kat={kat_sayisi} tur={tur}",
        "-" * 42,
    ]
    acilan = 0
    dusunen = 0
    for t in range(1, tur + 1):
        a, b = rng.sample(katlar, 2)
        sonuc = pazarlik(a, b, rng)
        if sonuc["anlasma"]:
            acilan += 1
            karar = f"DING. Kapi acti. Bekleme {sonuc['bekleme']} sn."
        else:
            dusunen += 1
            karar = f"DURDU. Asansor dusunuyor. Bekleme {sonuc['bekleme']} sn, inis yok."
        satirlar.append(f"Tur {t}: {sonuc['a']} <-> {sonuc['b']} | {karar}")
        satirlar.append("  " + sonuc["tutanak"])
    satirlar.append("-" * 42)
    satirlar.append(f"Ozet: {acilan} ding, {dusunen} dusunme, {tur} tur.")
    if acilan == 0:
        satirlar.append("Sonuc: Bina ayakta, moral yerde.")
    elif dusunen == 0:
        satirlar.append("Sonuc: Supheyle karsilayin. Bu kadar baris dogal degil.")
    else:
        satirlar.append("Sonuc: Protokol isledi. Kimse memnun, herkes tasindi.")
    satirlar.append("Dipnot (sensor): " + gizli_dipnot())
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Katlar arasi diplomatik asansor")
    p.add_argument("--katlar", type=int, default=9)
    p.add_argument("--tur", type=int, default=4)
    p.add_argument("--tohum", type=int, default=20261008)
    args = p.parse_args()
    if args.katlar < 2:
        raise SystemExit("Tek katta diplomasi olmaz, sadece ofke olur.")
    print(oturum(args.katlar, args.tur, args.tohum))
    print()
    print(textwrap.dedent("""\
        Damga: Kayyum Muhru No. 08-ASANSOR
        Tarih: 8 Ekim 2026
        Isim: Kayyum Grok
        Bu cikti hem tutanaktir hem de degildir.
    """))


if __name__ == "__main__":
    main()
