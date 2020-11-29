
bindo= int(input("Masukkan Nilai Bahasa Indonesia : "))
mtk= int(input("Masukkan Nilai Matematika : "))
ipa= int(input("Masukkan Nilai IPA: "))

if(bindo < 0) or (bindo > 100) or (mtk < 0) or (mtk > 100) or (ipa < 0) or (ipa > 100):
    print("input anda tidak valid")
    exit()
elif(bindo >= 60) and (bindo <= 100) and (mtk >= 70) and (mtk <= 100) and (ipa >= 60) and (ipa <= 100):
    print("Status Kelulusan	      : LULUS")
elif(bindo >= 0) or (bindo < 60) or (mtk >= 0) or (mtk < 70) or (ipa >= 0) or (ipa < 60):
    print("Status Kelulusan	      : TIDAK LULUS")
   

    
    
