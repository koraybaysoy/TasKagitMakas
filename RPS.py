import random


def puanlama(oyuncusecim1, oyuncusecim2, oyuncupuan1, oyuncupuan2):
    oyuncusecim1 = oyuncusecim1.upper()
    if oyuncusecim1 == "T":
        if oyuncusecim2 == "T":
            print("Bilgisayar Taş seçti. Kazanan Yok!!!")
            oyuncupuan1 = 5
            oyuncupuan2 = 5
        elif oyuncusecim2 == "K":
            print("Bilgisayar Kağıt  seçti ve taşı sardı ve kazandı!!!")
            oyuncupuan2 += 10
        elif oyuncusecim2 == "M":
            print("Bilgisayar Makas  seçti ve Taş Makası kırdı bilgisayar kaybetti!!!")
            if oyuncupuan1 == 0:
                oyuncupuan1 = 5
            else:
                oyuncupuan1 = oyuncupuan1 + oyuncupuan1 + int(oyuncupuan1 * 0.20)
    elif oyuncusecim1 == "K":
        if oyuncusecim2 == "K":
            print("Bilgisayar Kağıt seçti. Kazanan Yok!!!")
            oyuncupuan1 -= 5
            oyuncupuan2 -= 5
        elif oyuncusecim2 == "M":
            print("Bilgisayar  Makası seçti ve kağıdı kesti ve kazandı!!!")
            oyuncupuan1 -= 5
            oyuncupuan2 += 5
        elif oyuncusecim2 == "T":
            print("Bilgisayar Taş  seçti ve Kağıt taşı sardı  bilgisayar kaybetti!!!")
            oyuncupuan1 += 10

    elif oyuncusecim1 == "M":
        if oyuncusecim2 == "M":
            print("Bilgisayar Makas seçti. Kazanan Yok!!!")
            oyuncupuan1 -= 5
            oyuncupuan2 -= 5
        elif oyuncusecim2 == "T":
            print("Bilgisayar  Taş seçti ve makası kırdı ve kazandı!!!")
            if oyuncupuan2 == 0:
                oyuncupuan2 = 5
            else:
                oyuncupuan2 = oyuncupuan2 + oyuncupuan2 + int(oyuncupuan2 * 0.20)
        elif oyuncusecim2 == "K":
            print("Bilgisayar Kağıt seçti ve makas kağıdı kesti  bilgisayar kaybetti!!!")
            oyuncupuan1 += 5
            oyuncupuan2 -= 5
    else:
        print("Yanlış seçim yaptınız puanlarınız silindi")
        oyuncupuan1 = 0
    if oyuncupuan1 < 0:
        oyuncupuan1 = 0
    if oyuncupuan2 < 0:
        oyuncupuan2 = 0
    return oyuncupuan1, oyuncupuan2


oyuncupuan1 = 0
oyuncupuan2 = 0
for i in range(10):
    print("\n (T)aş - (K)ağıt - (M)akas ")
    oyuncusecim1 = input("Seçiminiz:")
    oyuncusecim2 = random.choice(["T", "M", "K"])
    print("Sizin Seçiminiz ", oyuncusecim1, " Bilgisayarın Seçimi ", oyuncusecim2)
    oyuncupuan1, oyuncupuan2 = puanlama(oyuncusecim1, oyuncusecim2, oyuncupuan1, oyuncupuan2)
    print("Sizin Puanınız ", oyuncupuan1, " Bilgisayarın Puanı ", oyuncupuan2)