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
        with open("jogos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {"biblioteca": [], "wishlist": []}
    
def salvar_dados(dados):
    with open("jogos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def adicionar():
    grupo = escolher_grupo()
    
    if not grupo:
        return

    titulo = input("Título do jogo: ")
    
    if grupo == "biblioteca":
        info_extra = input("Horas jogadas (ex: 120h): ")
        tipo_info = "horas_jogadas"
    else:
        info_extra = input("Preço na loja (ex: R$ 199,90): ")
        tipo_info = "preco"

    dados = ler_dados()
    dados[grupo].append({
        "titulo": titulo, 
        tipo_info: info_extra
    })
    salvar_dados(dados)
    print("✨ Jogo adicionado com sucesso!")

def listar():
    grupo = escolher_grupo()
    if not grupo:
        return
    
    dados = ler_dados()

    print(f"\n--- Sua {grupo.capitalize()} ---")

    if not dados[grupo]:
        print("Nenhum jogo encontrado aqui.")
        return

    for index, jogo in enumerate(dados[grupo], start=1):
        # Puxa a segunda chave do dicionário (horas_jogadas ou preco)
        chave_info = list(jogo.keys())[1] 
        
        # Formata o texto dependendo de qual lista estamos olhando
        if grupo == "biblioteca":
            print(f"{index}. {jogo['titulo']} | Horas jogadas:{jogo[chave_info]}")
        else:
            print(f"{index}. {jogo['titulo']} | Preço: {jogo[chave_info]}")

def atualizar():
    grupo = escolher_grupo()
    if not grupo:
        return
    
    dados = ler_dados()

    try:
        index = int(input("Index do jogo para atualizar: ")) - 1

        if 0 <= index < len(dados[grupo]):
            titulo = input("Novo título do jogo: ")
            
            if grupo == "biblioteca":
                info_extra = input("Atualizar horas jogadas: ")
                tipo_info = "horas_jogadas"
            else:
                info_extra = input("Atualizar preço: ")
                tipo_info = "preco"
            
            dados[grupo][index] = {
                "titulo": titulo,
                tipo_info: info_extra
            }
            salvar_dados(dados)
            print("Jogo atualizado com sucesso!")
        else:
            print("Index inválido! Esse jogo não está na lista.")
    except ValueError:
        print("Por favor, digite um número válido.")

def deletar():
    grupo = escolher_grupo()
    if not grupo:
        return
    
    dados = ler_dados()

    try:
        index = int(input("Index do jogo para remover: ")) - 1
        if 0 <= index < len(dados[grupo]):
            jogo_removido = dados[grupo].pop(index)
            salvar_dados(dados)
            print(f"O jogo '{jogo_removido['titulo']}' foi removido da sua conta.")
        else:
            print("Index inválido!")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    print("Bem-vindo ao seu Launcher de Jogos!")
    while True:
        menu() 
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "0":
            print("Fechando a Steam... Até a próxima!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()