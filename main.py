import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Fonction pour déterminer le gagnant
def determiner_gagnant(choix_utilisateur, choix_ordinateur):
    if choix_utilisateur == choix_ordinateur:
        return "Égalité"
    elif (choix_utilisateur == 'pierre' and choix_ordinateur == 'ciseaux') or \
         (choix_utilisateur == 'papier' and choix_ordinateur == 'pierre') or \
         (choix_utilisateur == 'ciseaux' and choix_ordinateur == 'papier'):
        return "Vous gagnez !"
    else:
        return "L'ordinateur gagne."

# Fonction pour afficher l'image et le résultat
def afficher_resultat(choix_utilisateur):
    choix_ordinateur = random.choice(['pierre', 'papier', 'ciseaux'])

    # Mise à jour des images affichées
    image_utilisateur = Image.open(f'images/{choix_utilisateur}.png')
    image_utilisateur = ImageTk.PhotoImage(image_utilisateur)
    label_image_utilisateur.config(image=image_utilisateur)
    label_image_utilisateur.image = image_utilisateur

    image_ordinateur = Image.open(f'images/{choix_ordinateur}.png')
    image_ordinateur = ImageTk.PhotoImage(image_ordinateur)
    label_image_ordinateur.config(image=image_ordinateur)
    label_image_ordinateur.image = image_ordinateur

    # Afficher le résultat dans une boîte de message
    resultat = determiner_gagnant(choix_utilisateur, choix_ordinateur)
    messagebox.showinfo("Résultat", f"Vous avez choisi {choix_utilisateur.capitalize()}.\nL'ordinateur a choisi {choix_ordinateur.capitalize()}.\n\n{resultat}")

# Fonction pour créer les boutons et la fenêtre
def creer_fenetre():
    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Pierre, Papier, Ciseaux")

    # Label pour l'image de l'utilisateur
    global label_image_utilisateur
    label_image_utilisateur = tk.Label(fenetre)
    label_image_utilisateur.pack(side=tk.LEFT, padx=20)

    # Label pour l'image de l'ordinateur
    global label_image_ordinateur
    label_image_ordinateur = tk.Label(fenetre)
    label_image_ordinateur.pack(side=tk.RIGHT, padx=20)

    # Créer des boutons pour chaque choix
    bouton_pierre = tk.Button(fenetre, text="Pierre", command=lambda: afficher_resultat("pierre"))
    bouton_pierre.pack(side=tk.LEFT, padx=10)

    bouton_papier = tk.Button(fenetre, text="Papier", command=lambda: afficher_resultat("papier"))
    bouton_papier.pack(side=tk.LEFT, padx=10)

    bouton_ciseaux = tk.Button(fenetre, text="Ciseaux", command=lambda: afficher_resultat("ciseaux"))
    bouton_ciseaux.pack(side=tk.LEFT, padx=10)

    # Lancer l'interface graphique
    fenetre.mainloop()

# Exécuter l'interface
if __name__ == "__main__":
    creer_fenetre()
