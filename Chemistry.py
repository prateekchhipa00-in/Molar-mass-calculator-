import time

# --- TERMINAL COLORS ---
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
RESET = "\033[0m"
BOLD = "\033[1m"

# table
PERIODIC_TABLE ={
    "H": 1, "He": 4, "Li": 7, "Be": 9, "B": 11, "C": 12, "N": 14, "O": 16, "F": 19, "Ne": 20,
    "Na": 23, "Mg": 24, "Al": 27, "Si": 28, "P": 31, "S": 32, "Cl": 35.5, "Ar": 40, "K": 39, "Ca": 40,
    "Sc": 45, "Ti": 48, "V": 51, "Cr": 52, "Mn": 55, "Fe": 56, "Co": 59, "Ni": 58.7, "Cu": 63.5, "Zn": 65,
    "Ga": 70, "Ge": 73, "As": 75, "Se": 79, "Br": 80, "Kr": 84, "Rb": 85.5, "Sr": 88, "Y": 89, "Zr": 91,
    "Nb": 93, "Mo": 96, "Tc": 98, "Ru": 101, "Rh": 103, "Pd": 106, "Ag": 108, "Cd": 112, "In": 115, "Sn": 119,
    "Sb": 122, "Te": 128, "I": 127, "Xe": 131, "Cs": 133, "Ba": 137, "La": 139, "Ce": 140, "Pr": 141, "Nd": 144,
    "Pm": 145, "Sm": 150, "Eu": 152, "Gd": 157, "Tb": 159, "Dy": 162.5, "Ho": 165, "Er": 167, "Tm": 169, "Yb": 173,
    "Lu": 175, "Hf": 178.5, "Ta": 181, "W": 184, "Re": 186, "Os": 190, "Ir": 192, "Pt": 195, "Au": 197, "Hg": 200.5,
    "Tl": 204, "Pb": 207, "Bi": 209, "Po": 209, "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232,
    "Pa": 231, "U": 238, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257,
    "Md": 258, "No": 259, "Lr": 262, "Rf": 267, "Db": 270, "Sg": 271, "Bh": 270, "Hs": 277, "Mt": 276, "Ds": 281,
    "Rg": 280, "Cn": 285, "Nh": 284, "Fl": 289, "Mc": 288, "Lv": 293, "Ts": 294, "Og": 294
}
# SUBSCRIPT
def get_subscript(number):
    
    sub_dict = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", 
                "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"}
    return "".join(sub_dict.get(char, char) for char in str(number))

def molecular_engine():
    total_molar_mass = 0
    formula_parts = []
    element_contribution = {}

    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{YELLOW}      🧪 PRO MOLECULAR ANALYZER  🧪      {RESET}")
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}Type '{RED}STOP{RESET}{BOLD}' when finished.{RESET}")

    while True:
        symbol_raw = input(f"\n{BOLD}Enter Symbol: {RESET}").strip()
        
        # Stop 
        if symbol_raw.lower() == 'stop':
            break

        # Capitalize
        symbol = symbol_raw.capitalize()

        if symbol in PERIODIC_TABLE:
            try:
                count_str = input(f"{BLUE}How many atoms of {symbol}?: {RESET}")
                count = int(count_str)
                
                mass = PERIODIC_TABLE[symbol]
                sub_total = mass * count
                
                total_molar_mass += sub_total
                
                # SUBSCRIPT
                sub_count = get_subscript(count) if count > 1 else ''
                formula_parts.append(f"{symbol}{sub_count}")
                
                #  percentage
                element_contribution[symbol] = element_contribution.get(symbol, 0) + sub_total
                
                print(f"{GREEN}✅ Added {symbol} | Current Total: {total_molar_mass} u{RESET}")
                
            except ValueError:
                print(f"{RED}❌ Error: Count must be a number!{RESET}")
        else:
            print(f"{RED}❌ Element '{symbol}' not found!{RESET}")

    #REPORT SECTION 
    if total_molar_mass > 0:
        final_formula = "".join(formula_parts)
        
        print(f"\n{CYAN}{'★'*60}{RESET}")
        print(f"{BOLD}{YELLOW}  FINAL CHEMICAL ANALYSIS REPORT:{RESET}")
        print(f"  {BOLD}COMPOUND:{RESET} {GREEN}{BOLD}{final_formula}{RESET}")
        print(f"  {BOLD}TOTAL MASS:{RESET} {CYAN}{total_molar_mass} g/mol{RESET}")
        print(f"  {BOLD}V. DENSITY:{RESET} {CYAN}{total_molar_mass / 2}{RESET}")
        
        print(f"\n  {BOLD}PERCENTAGE COMPOSITION:{RESET}")
        for element, m in element_contribution.items():
            percentage = (m / total_molar_mass) * 100
            bar = "█" * int(percentage / 10)
            print(f"  - {element:2}: {percentage:6.2f}% {BLUE}{bar:<10}{RESET}")
        
        print(f"{CYAN}{'★'*60}{RESET}")
    else:
        print(f"{RED}No elements added. Logic Terminated.{RESET}")

if __name__ == "__main__":
    molecular_engine()