"""Cadastro e análise de produtos usando listas, tuplas e conjuntos."""

from typing import TypedDict


class Produto(TypedDict):
    nome: str
    preco: float
    categoria: str


def ler_quantidade() -> int:
    """Solicita uma quantidade positiva de produtos."""
    while True:
        try:
            quantidade = int(input("Quantos produtos deseja cadastrar? "))
            if quantidade > 0:
                return quantidade
            print("Informe uma quantidade maior que zero.")
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_preco(nome_produto: str) -> float:
    """Lê um preço não negativo; aceita vírgula ou ponto decimal."""
    while True:
        entrada = input(f"Preço de {nome_produto}: ").strip().replace(",", ".")
        try:
            preco = float(entrada)
            if preco >= 0:
                return preco
            print("O preço não pode ser negativo.")
        except ValueError:
            print("Digite um preço válido, por exemplo 12,50.")


def cadastrar_produtos() -> list[Produto]:
    """Lê os dados e os armazena em uma lista."""
    produtos: list[Produto] = []
    quantidade = ler_quantidade()

    for numero in range(1, quantidade + 1):
        print(f"\nCadastro do produto {numero}:")
        nome = input("Nome: ").strip()
        while not nome:
            print("O nome não pode ficar vazio.")
            nome = input("Nome: ").strip()

        preco = ler_preco(nome)
        categoria = input("Categoria: ").strip()
        while not categoria:
            print("A categoria não pode ficar vazia.")
            categoria = input("Categoria: ").strip()

        produtos.append(
            {"nome": nome, "preco": preco, "categoria": categoria}
        )

    return produtos


def filtrar_por_preco(
    produtos: list[Produto],
) -> list[Produto]:
    """Filtra produtos acima ou abaixo do limite informado."""
    while True:
        criterio = input(
            "\nFiltrar produtos (A) acima ou (B) abaixo do preço? "
        ).strip().lower()
        if criterio in {"a", "b"}:
            break
        print("Escolha A para acima ou B para abaixo.")

    limite = ler_preco("limite para filtragem")
    if criterio == "a":
        return [produto for produto in produtos if produto["preco"] > limite]
    return [produto for produto in produtos if produto["preco"] < limite]


def exibir_produtos(
    titulo: str, produtos: list[Produto]
) -> None:
    """Exibe uma lista de produtos com preço formatado."""
    print(f"\n{titulo}")
    if not produtos:
        print("  Nenhum produto encontrado.")
        return

    for produto in produtos:
        print(
            f"  {produto['nome']} | "
            f"€{produto['preco']:.2f} | {produto['categoria']}"
        )


def gerar_relatorio(produtos: list[Produto]) -> None:
    """Apresenta filtragem, ordenações, categorias e estatísticas."""
    filtrados = filtrar_por_preco(produtos)

    # sort() ordena a própria lista por preço crescente.
    produtos.sort(key=lambda produto: produto["preco"])
    produtos_decrescentes = sorted(
        produtos, key=lambda produto: produto["preco"], reverse=True
    )

    categorias_unicas = set(
        produto["categoria"] for produto in produtos
    )
    precos = [produto["preco"] for produto in produtos]
    estatisticas = (min(precos), max(precos), sum(precos) / len(precos))

    print("\n========== RELATÓRIO DE PRODUTOS ==========")
    exibir_produtos("Produtos cadastrados:", produtos)
    exibir_produtos("Produtos após a filtragem:", filtrados)
    exibir_produtos("Produtos por preço crescente:", produtos)
    exibir_produtos("Produtos por preço decrescente:", produtos_decrescentes)

    print("\nCategorias únicas:")
    for categoria in sorted(categorias_unicas):
        print(f"  {categoria}")

    menor_preco, maior_preco, preco_medio = estatisticas
    print("\nEstatísticas (tupla: menor, maior, média):")
    print(
        f"  Menor preço: €{menor_preco:.2f}\n"
        f"  Maior preço: €{maior_preco:.2f}\n"
        f"  Preço médio: €{preco_medio:.2f}"
    )
    print("===========================================")


def main() -> None:
    produtos = cadastrar_produtos()
    gerar_relatorio(produtos)


if __name__ == "__main__":
    main()
