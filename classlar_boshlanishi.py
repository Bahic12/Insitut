from classlar import Talaba, Insitut
    
while True:
    ismi = input("Talabaning ismini kiriting:  ")
    familiyasi = input("Familiyasini kiriting:   ")
    tyili = input("Tug'ilgan yilini kiriting:   ")
    talaba = Talaba(ismi, familiyasi, tyili)
    savol = input("Yana talaba kiritasizmi. (yes/no)")
    if savol == 'yes':
        continue
    else:
        break 
print(talaba)