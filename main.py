import areafinder as af


def check_anwser():
    anwser = input("Площу з даних фігур вам треба знайти? 1-квадрат, 2-прямокутник, 3-трикутник, 4-коло, 5-паралелограм, 6-трапеція")

    if anwser == "1":
        print()
    elif anwser == "2":
        print()
    elif anwser == "3":
        print()
    elif anwser == "4":
        radius = float(input("Який радіус"))
        print(af.calculate_cyrcle(radius))
    elif anwser == "5":
        print(af.calculate_parallelogram_area)
    elif anwser == "6":
        print(af.calculate_trapisium)
