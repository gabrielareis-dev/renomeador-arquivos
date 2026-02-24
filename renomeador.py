# Importando ferramentas do sistema operacional
import os

# Função para gerar um nome único
def gerar_nome_unico(pasta, nome_base, contador, extensao):
    while True:
        novo_nome = f"{nome_base}_{contador}.{extensao}" if extensao else f"{nome_base}_{contador}"
        caminho_novo = os.path.join(pasta, novo_nome)

        if not os.path.exists(caminho_novo):
            return caminho_novo, novo_nome

        contador += 1

# Função para renomear arquivos
def renomear_arquivos(pasta, nome_base):
    contador = 1

    # Iterando sobre os arquivos em ordem
    for arquivo in sorted(os.listdir(pasta)):
        caminho_antigo = os.path.join(pasta, arquivo)

        # Só processa arquivos
        if os.path.isfile(caminho_antigo):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lstrip(".")

            caminho_novo, novo_nome = gerar_nome_unico(
                pasta, nome_base, contador, extensao
            )

            os.rename(caminho_antigo, caminho_novo)

            print(f"✅ {arquivo} → {novo_nome}")

            contador += 1

def main():
    print("=== Renomeador de Arquivos ===")

    # pede pasta
    pasta_alvo = input(
        "Digite o caminho da pasta onde os arquivos estão localizados: "
    ).strip()

    # valida pasta
    if not os.path.exists(pasta_alvo):
        print("Pasta não encontrada. Verifique o caminho.")
        return

    print("Pasta localizada com sucesso!")

    # pede nome base
    nome_base = input("Digite o nome base dos arquivos: ").strip()

    if not nome_base:
        print("Nome base inválido.")
        return

    # executa renomeação
    renomear_arquivos(pasta_alvo, nome_base)

    print("Renomeação concluída!")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()