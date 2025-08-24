# Programme simple pour l'inscription de l'assal (abonnement)
print("=== T9yid fl'assal ===")
print("1. T9yid l'wa7ed l'chhar")
print("2. T9yid jooj d'chhor")

choix = input("Chno bghiti? (1 ola 2): ")

# Prix par mois
prix_par_mois = 150  # dh par mois (exemple)

if choix == "1":
    total = prix_par_mois
    print(f"T9yid dyalk l'wa7ed l'chhar. Total: {total} DH")
elif choix == "2":
    total = prix_par_mois * 2
    print(f"T9yid dyalk jooj d'chhor. Total: {total} DH")
else:
    print("L'option li dkhalt makaynash. 3awd men jdid.")
