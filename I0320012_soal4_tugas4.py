usia = 21
x = int(input("Berapa usia kamu : "))
if usia <= x :
    print("Kamu memenuhi usia")
    y = str(input("Apakah kamu lulus ujian kualifikasi (Y/T) "))
    if y == "Y" :
        print("Kamu boleh mengikuti kursus")
    elif y == "T" :
        print("Kamu tidak boleh mengikuti kursus")
else :
    print("Kamu tidak memenuhi usia")
