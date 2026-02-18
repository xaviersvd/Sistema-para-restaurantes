from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_camarao = Prato('Massa de Camarão', 45.00, 'A melhor massa da cidade de Natal.')

restaurante_praca.adiciona_no_cardapio(bebida_suco)
restaurante_praca.adiciona_no_cardapio(prato_camarao)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()