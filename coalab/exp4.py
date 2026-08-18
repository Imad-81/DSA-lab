"""
Experiment 4: Study and Verify Half and Full Subtractor
Using Basic Logic Gates (XOR, NOT, AND, OR) and Universal NAND Gates.

Computer Organization & Architecture Laboratory
"""

def nand_gate(a: int, b: int) -> int:
    """NAND gate: Returns NOT (a AND b)"""
    return 1 if not (a and b) else 0

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
# 1. HALF SUBTRACTOR IMPLEMENTATIONS
# ==========================================

def half_subtractor_basic(a: int, b: int) -> tuple[int, int]:
    """
    Half Subtractor using XOR, NOT, and AND gates:
    Difference (D) = A ^ B
    Borrow     (B) = A' . B
    """
    diff = xor_gate(a, b)
    borrow = and_gate(not_gate(a), b)
    return diff, borrow


def half_subtractor_nand(a: int, b: int) -> tuple[int, int]:
    """
    Half Subtractor using only 5 NAND gates:
    N1 = NAND(A, B)      = (AB)'
    N2 = NAND(A, N1)     = A' + B
    N3 = NAND(B, N1)     = B' + A
    Difference = NAND(N2, N3) = A ^ B
    Borrow     = NAND(N3, N3) = (B' + A)' = A' . B
    """
    n1 = nand_gate(a, b)
    n2 = nand_gate(a, n1)
    n3 = nand_gate(b, n1)
    diff = nand_gate(n2, n3)
    borrow = nand_gate(n3, n3)
    return diff, borrow


# ==========================================
# 2. FULL SUBTRACTOR IMPLEMENTATIONS
# ==========================================

def full_subtractor_basic(a: int, b: int, bin_in: int) -> tuple[int, int]:
    """
    Full Subtractor using XOR, NOT, AND, and OR gates:
    Difference (D)   = A ^ B ^ Bin
    Borrow Out (Bout)= (A ^ B)' . Bin + A' . B
                     = A' . Bin + A' . B + B . Bin
    """
    axb = xor_gate(a, b)
    diff = xor_gate(axb, bin_in)
    
    term1 = and_gate(not_gate(a), b)
    term2 = and_gate(not_gate(axb), bin_in)
    bout = or_gate(term1, term2)
    return diff, bout


def full_subtractor_nand(a: int, b: int, bin_in: int) -> tuple[int, int]:
    """
    Full Subtractor using 9 NAND gates (Two cascaded Half Subtractors + 1 Carry NAND):
    Stage 1 (Half Subtractor 1 on A, B):
      N1 = NAND(A, B)
      N2 = NAND(A, N1)
      N3 = NAND(B, N1)       [N3' = A' . B]
      N4 = NAND(N2, N3)      [= A ^ B]

    Stage 2 (Half Subtractor 2 on N4, Bin):
      N5 = NAND(N4, Bin)
      N6 = NAND(N4, N5)
      N7 = NAND(Bin, N5)     [N7' = N4' . Bin = (A ^ B)' . Bin]
      N8 = NAND(N6, N7)      [= Difference = A ^ B ^ Bin]

    Stage 3 (Borrow Combining):
      N9 = NAND(N3, N7)      [= Bout = A' . B + (A ^ B)' . Bin]
    """
    # Half Subtractor 1
    n1 = nand_gate(a, b)
    n2 = nand_gate(a, n1)
    n3 = nand_gate(b, n1)
    n4 = nand_gate(n2, n3)

    # Half Subtractor 2
    n5 = nand_gate(n4, bin_in)
    n6 = nand_gate(n4, n5)
    n7 = nand_gate(bin_in, n5)
    n8 = nand_gate(n6, n7)  # Difference

    # Borrow Out combination
    n9 = nand_gate(n3, n7)  # Bout

    return n8, n9


# ==========================================
# 3. TRUTH TABLE AND DISPLAY FUNCTIONS
# ==========================================

def display_half_subtractor_truth_table():
    print("\n" + "=" * 54)
    print("             HALF SUBTRACTOR TRUTH TABLE")
    print("=" * 54)
    print(f"{'S.No':<8} | {'Input A':<8} | {'Input B':<8} | {'Diff (D)':<10} | {'Borrow (B)':<10}")
    print("-" * 54)
    
    sno = 1
    for a in [0, 1]:
        for b in [0, 1]:
            d_basic, b_basic = half_subtractor_basic(a, b)
            d_nand, b_nand = half_subtractor_nand(a, b)
            assert (d_basic, b_basic) == (d_nand, b_nand), f"Mismatch at A={a}, B={b}"
            print(f"{sno:<8} | {a:<8} | {b:<8} | {d_basic:<10} | {b_basic:<10}")
            sno += 1
    print("=" * 54)


def display_full_subtractor_truth_table():
    print("\n" + "=" * 64)
    print("                     FULL SUBTRACTOR TRUTH TABLE")
    print("=" * 64)
    print(f"{'S.No':<6} | {'Input A':<8} | {'Input B':<8} | {'Bin':<6} | {'Diff (D)':<10} | {'Borrow (Bout)':<12}")
    print("-" * 64)
    
    sno = 1
    for a in [0, 1]:
        for b in [0, 1]:
            for bin_in in [0, 1]:
                d_basic, b_basic = full_subtractor_basic(a, b, bin_in)
                d_nand, b_nand = full_subtractor_nand(a, b, bin_in)
                assert (d_basic, b_basic) == (d_nand, b_nand), f"Mismatch at A={a}, B={b}, Bin={bin_in}"
                print(f"{sno:<6} | {a:<8} | {b:<8} | {bin_in:<6} | {d_basic:<10} | {b_basic:<12}")
                sno += 1
    print("=" * 64)


def run_interactive_menu():
    while True:
        print("\n=======================================================")
        print(" EXPERIMENT 4: HALF SUBTRACTOR & FULL SUBTRACTOR")
        print("=======================================================")
        print("1. Display Half Subtractor Truth Table (XOR, NOT, AND)")
        print("2. Display Full Subtractor Truth Table (XOR, NOT, AND, OR)")
        print("3. Test Half Subtractor with Custom Inputs (A, B)")
        print("4. Test Full Subtractor with Custom Inputs (A, B, Bin)")
        print("5. Verify All Gate Realizations")
        print("6. Exit")
        print("=======================================================")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            display_half_subtractor_truth_table()

        elif choice == 2:
            display_full_subtractor_truth_table()

        elif choice == 3:
            print("\n--- Test Half Subtractor ---")
            try:
                a = int(input("Enter Input A (0 or 1): "))
                b = int(input("Enter Input B (0 or 1): "))
                if a not in (0, 1) or b not in (0, 1):
                    print("Error: Inputs must be binary (0 or 1).")
                    continue
                d_basic, b_basic = half_subtractor_basic(a, b)
                d_nand, b_nand = half_subtractor_nand(a, b)
                print(f"\n[Basic XOR/NOT/AND] -> Difference: {d_basic}, Borrow: {b_basic}")
                print(f"[NAND Only]        -> Difference: {d_nand}, Borrow: {b_nand}")
            except ValueError:
                print("Invalid input! Please enter integers (0 or 1).")

        elif choice == 4:
            print("\n--- Test Full Subtractor ---")
            try:
                a = int(input("Enter Input A   (0 or 1): "))
                b = int(input("Enter Input B   (0 or 1): "))
                bin_in = int(input("Enter Input Bin (0 or 1): "))
                if a not in (0, 1) or b not in (0, 1) or bin_in not in (0, 1):
                    print("Error: Inputs must be binary (0 or 1).")
                    continue
                d_basic, b_basic = full_subtractor_basic(a, b, bin_in)
                d_nand, b_nand = full_subtractor_nand(a, b, bin_in)
                print(f"\n[Basic XOR/NOT/AND/OR] -> Difference: {d_basic}, Borrow Out: {b_basic}")
                print(f"[9-NAND Gates]         -> Difference: {d_nand}, Borrow Out: {b_nand}")
            except ValueError:
                print("Invalid input! Please enter integers (0 or 1).")

        elif choice == 5:
            print("\n[Running Comprehensive Verification...]")
            all_passed = True
            for a in [0, 1]:
                for b in [0, 1]:
                    db, bb = half_subtractor_basic(a, b)
                    dn, bn = half_subtractor_nand(a, b)
                    if (db, bb) != (dn, bn):
                        all_passed = False
                        print(f"FAILED Half Subtractor at A={a}, B={b}")
            for a in [0, 1]:
                for b in [0, 1]:
                    for bin_in in [0, 1]:
                        db, bb = full_subtractor_basic(a, b, bin_in)
                        dn, bn = full_subtractor_nand(a, b, bin_in)
                        if (db, bb) != (dn, bn):
                            all_passed = False
                            print(f"FAILED Full Subtractor at A={a}, B={b}, Bin={bin_in}")
            if all_passed:
                print("SUCCESS: All Half Subtractor and Full Subtractor circuits verified 100% successfully!")

        elif choice == 6:
            print("Exiting Experiment 4 program. Thank you!")
            break

        else:
            print("Invalid choice! Please choose an option from 1 to 6.")


if __name__ == "__main__":
    run_interactive_menu()
