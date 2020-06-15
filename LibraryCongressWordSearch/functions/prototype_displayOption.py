from dataclasses import dataclass
import FuzzySearch

@dataclass
class term:
    num: str
    title: str
    vocabulary: str
    concept: str
    identifier: str
    LC_URI: str

def main():
    termList = []
    choice = 0
    
    term0 = term("1. ", "Dalton, Test, 1877-1945", "LC Name Authority File (LCNAF)",
                 "Personal Name", "n92004163", "http://id.loc.gov/authorities/names/n92004163")
    term1 = term("2. ", "U.S. Naval Mine Warfare Test Station (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "n88137183", "http://id.loc.gov/authorities/names/n88137183")
    term2 = term("3. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term3 = term("4. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term4 = term("5. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term5 = term("6. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term6 = term("7. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term7 = term("8. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term8 = term("9. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term9 = term("10. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    term10 = term("11. ", "Chesapeake Test Range (Md.)", "LC Name Authority File (LCNAF)",
                 "Geographic", "no93036995", "http://id.loc.gov/authorities/names/no93036995")
    termList.append(term0)
    termList.append(term1)
    termList.append(term2)
    termList.append(term3)
    termList.append(term4)
    termList.append(term5)
    termList.append(term6)
    termList.append(term7)
    termList.append(term8)
    termList.append(term9)
    termList.append(term10)

    choice = FuzzySearch.displayOption(termList)
    print("Choice is: ", choice)

if __name__ == "__main__":
    main()
