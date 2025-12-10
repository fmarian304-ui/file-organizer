import os
import shutil

def organizare_fisiere(folder):
    if not os.path.exists(folder):
        print("Folderul nu există!")
        return
    
    # Categorii de fișiere
    categorii = {
        "Imagini": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videoclipuri": [".mp4", ".mov", ".avi", ".mkv"],
        "Documente": [".pdf", ".docx", ".txt", ".xlsx"],
        "Arhive": [".zip", ".rar", ".7z"],
        "Audio": [".mp3", ".wav", ".flac"],
    }

    for fisier in os.listdir(folder):
        path_fisier = os.path.join(folder, fisier)

        if os.path.isfile(path_fisier):
            extensie = os.path.splitext(fisier)[1].lower()
            mutat = False

            for categorie, extensii in categorii.items():
                if extensie in extensii:
                    folder_nou = os.path.join(folder, categorie)

                    if not os.path.exists(folder_nou):
                        os.makedirs(folder_nou)

                    shutil.move(path_fisier, os.path.join(folder_nou, fisier))
                    mutat = True
                    break

            if not mutat:
                folder_altele = os.path.join(folder, "Altele")
                if not os.path.exists(folder_altele):
                    os.makedirs(folder_altele)
                shutil.move(path_fisier, os.path.join(folder_altele, fisier))

    print("Organizarea fișierelor s-a terminat!")


def main():
    print("=== Organizator de Fișiere ===")
    folder = input("Introdu calea completă către folderul pe care vrei să îl organizezi: ")

    organizare_fisiere(folder)


if __name__ == "__main__":
    main()
