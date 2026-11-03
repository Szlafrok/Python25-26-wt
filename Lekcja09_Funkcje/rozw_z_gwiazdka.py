def przedstaw_sie(imie: str, nazwisko: str, kostka: str = "chodnikowa") -> str:
    print(f"Cześć, jestem {imie} {nazwisko} a mój ulubiony typ kostki brukowej to {kostka}")
    return "ciastko"

przedstaw_sie("Piotrek", "Polański", "kocie łby")


x = przedstaw_sie("a", "b", "c")