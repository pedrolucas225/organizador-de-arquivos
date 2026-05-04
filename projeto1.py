import os
import shutil

pasta = r"C:\Users\Pedro\Downloads"

categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Vídeos": [".mp4", ".avi", ".mkv", ".mov"],
    "Arquivos Compactados": [".zip", ".rar", ".tar", ".gz"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Aplicativos": [".exe", ".msi", ".bat", ".cmd"]
}

print(f"Organizando arquivos na pasta '{pasta}'...")

for arquivo in os.listdir(pasta):
    print(f"Processando arquivo: {arquivo}")

    _,extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    categoria_destino = None
    for categoria,extensoes in categorias.items():
        if extensao in extensoes:
            categoria_destino = categoria
            break

    if categoria_destino is None:
        print(f"Arquivo '{arquivo}' não se encaixa em nenhuma categoria conhecida. Pulando.")
        continue

    subpasta_destino = os.path.join(pasta, categoria_destino)
    os.makedirs(subpasta_destino, exist_ok=True)

    caminho_origem = os.path.join(pasta, arquivo)
    caminho_destino = os.path.join(subpasta_destino,arquivo)
    
    try:
        shutil.move(caminho_origem, caminho_destino)
        print(f"✅{arquivo} → {categoria_destino}/")    

    except Exception as erro:
        print(f"❌ Erro ao mover '{arquivo}': {erro}")

print("Organização concluída!")