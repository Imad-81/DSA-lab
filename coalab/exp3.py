"""
Experiment 3: Construction of Half Adder and Full Adder using XOR and NAND gates
and Verification of their Operation.

Computer Organization & Architecture Laboratory
"""

def nand_gate(a: int, b: int) -> int:
    """NAND gate: Returns NOT (a AND b)"""
    return 1 if not (a and b) else 0

def nor_gate(a: int, b: int) -> int:
    """NOR gate: Returns NOT (a OR b)"""
    return 1 if not (a or b) else 0

def not_gate(a: int) -> int:
    """NOT gate: Returns NOT a"""
    return 0 if a else 1

def and_gate(a: int, b: int) -> int:
    """AND gate: Returns a AND b"""
    return 1 if (a and b) else 0

def or_gate(a: int, b: int) -> int:
    """OR gate: Returns a OR b"""
    return 1 if (a or b) else 0

def xor_gate(a: int, b: int) -> int:
    """XOR gate: Returns a XOR b"""
    return 1 if (a ^ b) else 0


# ==========================================
# 1. HALF ADDER IMPLEMENTATIONS
# ==========================================

def half_adder_basic(a: int, b: int) -> tuple[int, int]:
    """
    Half Adder using basic XOR and AND gates:
    Sum   = A ^ B
    Carry = A . B
    """
    sum_out = xor_gate(a, b)
    carry_out = and_gate(a, b)
    return sum_out, carry_out


def half_adder_nand(a: int, b: int) -> tuple[int, int]:
    """
    Half Adder using only 5 NAND gates:
    N1 = NAND(A, B)
    N2 = NAND(A, N1)
    N3 = NAND(B, N1)
    Sum   = NAND(N2, N3) = A ^ B
    Carry = NAND(N1, N1) = A . B
    """
    n1 = nand_gate(a, b)
    n2 = nand_gate(a, n1)
    n3 = nand_gate(b, n1)
    sum_out = nand_gate(n2, n3)
    carry_out = nand_gate(n1, n1)
    return sum_out, carry_out


def half_adder_nor(a: int, b: int) -> tuple[int, int]:
    """
    Half Adder using only 5 NOR gates:
    N1 = NOR(A, B) = (A+B)'
    N2 = NOR(A, N1) = A'B
    N3 = NOR(B, N1) = AB'
    N4 = NOR(N2, N3) = (A ^ B)'
    Sum   = NOR(N1, N4) = A ^ B
    Carry = NOR(N1, N1) = A+B -> NAND inverter / directly A.B
    """
    n1 = nor_gate(a, b)
    n2 = nor_gate(a, n1)
    n3 = nor_gate(b, n1)
    sum_out = nor_gate(nor_gate(n2, n3), n1)
    carry_out = and_gate(a, b)
    return sum_out, carry_out


# ==========================================
# 2. FULL ADDER IMPLEMENTATIONS
# ==========================================

def full_adder_basic(a: int, b: int, cin: int) -> tuple[int, int]:
    """
    Full Adder using XOR, AND, and OR gates:
    Sum  = (A ^ B) ^ Cin
    Cout = (A ^ B) . Cin + (A . B)
    """
    axb = xor_gate(a, b)
    sum_out = xor_gate(axb, cin)
    carry_out = or_gate(and_gate(axb, cin), and_gate(a, b))
    return sum_out, carry_out


def full_adder_nand(a: int, b: int, cin: int) -> tuple[int, int]:
    """
    Full Adder using 9 NAND gates (Two Half Adders + 1 Carry NAND):
    Stage 1 (Half Adder 1):
      N1 = NAND(A, B)
      N2 = NAND(A, N1)
      N3 = NAND(B, N1)
      N4 = NAND(N2, N3)  [= A ^ B]

    Stage 2 (Half Adder 2):
      N5 = NAND(N4, Cin)
      N6 = NAND(N4, N5)
      N7 = NAND(Cin, N5)
      N8 = NAND(N6, N7)  [= Sum = A ^ B ^ Cin]

    Stage 3 (Carry Out):
      N9 = NAND(N1, N5)  [= Cout = AB + (A ^ B)Cin]
    """
    # Half Adder 1
    n1 = nand_gate(a, b)
    n2 = nand_gate(a, n1)
    n3 = nand_gate(b, n1)
    n4 = nand_gate(n2, n3)

    # Half Adder 2
    n5 = nand_gate(n4, cin)
    n6 = nand_gate(n4, n5)
    n7 = nand_gate(cin, n5)
    n8 = nand_gate(n6, n7)  # Sum

    # Carry combining gate
    n9 = nand_gate(n1, n5)  # Cout

    return n8, n9


def full_adder_nor(a: int, b: int, cin: int) -> tuple[int, int]:
    """
    Full Adder using 9 NOR gates (Two Half Adders + 1 Carry NOR)
    """
    # Half Adder 1
    n1 = nor_gate(a, b)
    n2 = nor_gate(a, n1)
    n3 = nor_gate(b, n1)
    n4 = nor_gate(n2, n3)
    s1 = nor_gate(n1, n4)  # A ^ B

    # Half Adder 2
    n5 = nor_gate(s1, cin)
    n6 = nor_gate(s1, n5)
    n7 = nor_gate(cin, n5)
    n8 = nor_gate(n6, n7)
    sum_out = nor_gate(n5, n8)  # A ^ B ^ Cin

    # Carry combining gate
    c1 = nor_gate(n2, n3)  # AB
    c2 = nor_gate(n6, n7)  # (A ^ B)Cin
    cout = nor_gate(nor_gate(c1, c2), nor_gate(c1, c2))  # Cout
    return sum_out, cout


# ==========================================
# 3. VERIFICATION AND DISPLAY
# ==========================================

def display_half_adder_truth_table():
    print("\n" + "=" * 50)
    print("           HALF ADDER TRUTH TABLE")
    print("=" * 50)
    print(f"{'S.No':<8} | {'Input A':<8} | {'Input B':<8} | {'Sum (S)':<8} | {'Carry (C)':<10}")
    print("-" * 50)
    
    sno = 1
    for a in [0, 1]:
        for b in [0, 1]:
            s_basic, c_basic = half_adder_basic(a, b)
            s_nand, c_nand = half_adder_nand(a, b)
            # Verify basic and nand match
            assert (s_basic, c_basic) == (s_nand, c_nand), f"Mismatch at A={a}, B={b}"
            print(f"{sno:<8} | {a:<8} | {b:<8} | {s_basic:<8} | {c_basic:<10}")
            sno += 1
    print("=" * 50)


def display_full_adder_truth_table():
    print("\n" + "=" * 60)
    print("                     FULL ADDER TRUTH TABLE")
    print("=" * 60)
    print(f"{'S.No':<6} | {'Input A':<8} | {'Input B':<8} | {'Cin':<6} | {'Sum (S)':<8} | {'Carry (Cout)':<12}")
    print("-" * 60)
    
    sno = 1
    for a in [0, 1]:
        for b in [0, 1]:
            for cin in [0, 1]:
                s_basic, c_basic = full_adder_basic(a, b, cin)
                s_nand, c_nand = full_adder_nand(a, b, cin)
                # Verify basic and nand match
                assert (s_basic, c_basic) == (s_nand, c_nand), f"Mismatch at A={a}, B={b}, Cin={cin}"
                print(f"{sno:<6} | {a:<8} | {b:<8} | {cin:<6} | {s_basic:<8} | {c_basic:<12}")
                sno += 1
    print("=" * 60)


def run_interactive_menu():
    while True:
        print("\n=======================================================")
        print(" EXPERIMENT 3: HALF ADDER & FULL ADDER SIMULATOR")
        print("=======================================================")
        print("1. Display Half Adder Truth Table (XOR & NAND)")
        print("2. Display Full Adder Truth Table (XOR & NAND)")
        print("3. Test Half Adder with Custom Inputs (A, B)")
        print("4. Test Full Adder with Custom Inputs (A, B, Cin)")
        print("5. Verify All Gate Realizations")
        print("6. Exit")
        print("=======================================================")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            display_half_adder_truth_table()

        elif choice == 2:
            display_full_adder_truth_table()

        elif choice == 3:
            print("\n--- Test Half Adder ---")
            try:
                a = int(input("Enter Input A (0 or 1): "))
                b = int(input("Enter Input B (0 or 1): "))
                if a not in (0, 1) or b not in (0, 1):
                    print("Error: Inputs must be binary (0 or 1).")
                    continue
                s_basic, c_basic = half_adder_basic(a, b)
                s_nand, c_nand = half_adder_nand(a, b)
                print(f"\n[Basic XOR/AND] -> Sum: {s_basic}, Carry: {c_basic}")
                print(f"[NAND Only]     -> Sum: {s_nand}, Carry: {c_nand}")
            except ValueError:
                print("Invalid input! Please enter integers (0 or 1).")

        elif choice == 4:
            print("\n--- Test Full Adder ---")
            try:
                a = int(input("Enter Input A   (0 or 1): "))
                b = int(input("Enter Input B   (0 or 1): "))
                cin = int(input("Enter Input Cin (0 or 1): "))
                if a not in (0, 1) or b not in (0, 1) or cin not in (0, 1):
                    print("Error: Inputs must be binary (0 or 1).")
                    continue
                s_basic, c_basic = full_adder_basic(a, b, cin)
                s_nand, c_nand = full_adder_nand(a, b, cin)
                print(f"\n[Basic XOR/AND/OR] -> Sum: {s_basic}, Carry Out: {c_basic}")
                print(f"[9-NAND Gates]     -> Sum: {s_nand}, Carry Out: {c_nand}")
            except ValueError:
                print("Invalid input! Please enter integers (0 or 1).")

        elif choice == 5:
            print("\n[Running Comprehensive Verification...]")
            all_passed = True
            for a in [0, 1]:
                for b in [0, 1]:
                    sb, cb = half_adder_basic(a, b)
                    sn, cn = half_adder_nand(a, b)
                    if (sb, cb) != (sn, cn):
                        all_passed = False
                        print(f"FAILED Half Adder at A={a}, B={b}")
            for a in [0, 1]:
                for b in [0, 1]:
                    for cin in [0, 1]:
                        sb, cb = full_adder_basic(a, b, cin)
                        sn, cn = full_adder_nand(a, b, cin)
                        if (sb, cb) != (sn, cn):
                            all_passed = False
                            print(f"FAILED Full Adder at A={a}, B={b}, Cin={cin}")
            if all_passed:
                print("SUCCESS: All Half Adder and Full Adder circuits verified 100% successfully!")

        elif choice == 6:
            print("Exiting Experiment 3 program. Thank you!")
            break

        else:
            print("Invalid choice! Please choose an option from 1 to 6.")


if __name__ == "__main__":
    run_interactive_menu()
