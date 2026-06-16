def sozlar_soni(fayl_nomi):
    try:
        with open(fayl_nomi, 'r') as f:
            matn = f.read()
            sozlar = matn.split()
            return len(sozlar)
    except FileNotFoundError:
        return "Fayl topilmadi"
    except Exception as e:
        return str(e)

print(sozlar_soni("fayl.txt"))
