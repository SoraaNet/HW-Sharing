mijn_dictionary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-Maart-1939",
    "registratienummer" : "AA18891"

}
mijn_dictionary["Achternaam"] = "De Vries"
mijn_dictionary.pop("Geboortedatum")
print()
for k, v in mijn_dictionary.items():
    print (k, v)
