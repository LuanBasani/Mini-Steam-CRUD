import json


# Menu principal
def menu():
    print("\n--- Mini Steam ---")
    print("1. Adicionar Jogo")
    print("2. Ver Biblioteca / Wishlist")
    print("3. Atualizar Jogo (ex: atualizar horas jogadas)")
    print("4. Remover Jogo (ex: pedir reembolso)")
    print("0. Deslogar")

def escolher_grupo():
    print("\nOnde deseja acessar?")
    print("1. Biblioteca (Jogos Adquiridos)")
    print("2. Lista de Desejos (Wishlist)")

    opcao = input("Escolha a categoria: ")
    if opcao == "1":
        return "biblioteca"
    elif opcao == "2":
        return "wishlist"
    else:
        print("Opção inválida!")
        return None
    
def ler_dados():
    # Salva os dados em um arquivo chamado meus_jogos.json
    try:
        with open("meus_jogos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {"biblioteca": [], "wishlist": []}
    
def salvar_dados(dados):
    with open("meus_jogos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)