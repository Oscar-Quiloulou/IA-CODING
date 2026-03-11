import os
from huggingface_hub import snapshot_download

def main():
    # ID du modèle HuggingFace
    repo_id = "microsoft/phi-1_5"

    # Dossier local où sauvegarder le modèle
    target_dir = "model/base/phi-1_5"

    print("📦 Téléchargement du modèle :", repo_id)
    print("📁 Dossier de destination :", target_dir)

    # Création du dossier si besoin
    os.makedirs(target_dir, exist_ok=True)

    # Téléchargement complet (pas de symlinks)
    snapshot_download(
        repo_id=repo_id,
        local_dir=target_dir,
        local_dir_use_symlinks=False
    )

    print("✅ Téléchargement terminé !")
    print(f"Tous les fichiers sont maintenant disponibles dans : {target_dir}")

if __name__ == "__main__":
    main()