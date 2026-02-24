leiviska_string = input("Anna leiviskat: ")

leiviska = int(leiviska_string)

naula_string = input("Anna naulat: ")

naula = int(naula_string)

luoti_string = input("Anna luoti: ")

luoti = float(luoti_string)


leiviskatulo = leiviska * 20 * 32 * 13.3

naulatulo = naula * 32 * 13.3

luotitulo = luoti * 13.3

summakilo = (leiviskatulo + naulatulo + luotitulo)/1000
summagramma = (leiviskatulo + naulatulo + luotitulo) - summakilo

print(f"Massa nykymittojen mukaan:  {summakilo:6.0f} kilogrammaa ja {summagramma:6.3f} grammaa")













