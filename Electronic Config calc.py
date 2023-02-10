def electronic_config_calc(atomic_no):
    max_electrons = [2,
                     2,
                     6, 2,
                     6, 2,
                     10, 6, 2,
                     10, 6, 2,
                     14, 10, 6, 2,
                     14, 10, 6,
                     ]

    electrons = []
    for value in max_electrons:
        if sum(electrons) < atomic_no:
            electrons.append(value)
        else:
            break

    if sum(electrons) != atomic_no:
        electrons[-1] = atomic_no - sum(electrons[:-1])

    electrons_sup = [str(electron_no).translate(str.maketrans(
        "0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")) for electron_no in electrons]

    list_of_shells_orbits = ["1s", "2s",
                             "2p", "3s",
                             "3p", "4s",
                             "3d", "4p", "5s",
                             "4d", "5p", "6s",
                             "4f", "5d", "6p", "7s",
                             "5f", "6d", "7p", "8s"]

    electronic_config = "".join([f"{shell_orbit}{electron_no}" for shell_orbit, electron_no in zip(
        list_of_shells_orbits, electrons_sup)])

    print(
        f"The electronic configuration of the element with the atomic number {atomic_no} is:\n{electronic_config}")


electronic_config_calc(int(input("Enter the atomic number of the element you'd like to see the electronic \
configuration of: ")))


user_input = int(input("Enter another atomic number: "))

while user_input != 0:
    electronic_config_calc(user_input)
    user_input = int(input("Enter another atomic number: "))
