
U_P1,U_P2,U_P3,U_P4 = 15.00,18.00,20.00,25.00
Rental = 300.00

while True:
    C_Reading = float(input("Enter Current reading[To Exit Enter -1]: "))
    if C_Reading < 0:
        break

    L_Reading = float(input("Enter Last Reading: "))

    U_Count = C_Reading - L_Reading
    N_Price = 0.00

    if U_Count <= 60:
        N_Price = (U_Count * U_P1)
    elif U_Count <= 90:
        N_Price = (((U_Count - 60) * U_P2) + (60 * U_P1))
    elif U_Count <= 120:
        N_Price = ((60 * U_P1) + (30 * U_P2) + ((U_Count - 90) * U_P3))
    else:
        N_Price = ((60 * U_P1) + (30 * U_P2) + (30 * U_P3) + ((U_Count - 120) * U_P4))

    G_Price = N_Price + Rental
    

    print(f"Units Consumed: {U_Count}")
    print(f"Net Price for Units Consumed: {N_Price}")
    print(f"Rental Charges: {Rental}")
    print(f"Gross Price for Units Consumed: {G_Price}")
    