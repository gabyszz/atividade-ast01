# atividade-ast01
Atividade prática de testes de software – Carrinho de Compras


# Testes do Carrinho de Compras

## 1. Objetivo

Esta atividade tem como objetivo projetar casos de teste para validar as regras de negócio de um carrinho de compras de um e-commerce.

Serão testadas principalmente as regras relacionadas ao cálculo do frete e à aplicação dos cupons de desconto `PROMO10` e `PRIMEIRACOMPRA`.

O objetivo é verificar se o sistema aplica corretamente os descontos, o frete grátis e as restrições de utilização dos cupons.

---

## 2. Regras de Negócio

As regras consideradas nos testes são:

* Pedidos com valor igual ou superior a **R$ 200,00** possuem frete grátis.
* Pedidos com valor inferior a **R$ 200,00** possuem frete de **R$ 25,00**.
* O cupom `PROMO10` concede **10% de desconto**.
* O cupom `PROMO10` só pode ser utilizado em pedidos de **R$ 100,00 ou mais**.
* O desconto do `PROMO10` deve ser aplicado antes da verificação do frete grátis.
* O cupom `PRIMEIRACOMPRA` concede **R$ 30,00 de desconto fixo**.
* O cupom `PRIMEIRACOMPRA` pode ser utilizado em pedidos de qualquer valor.
* Não é permitido utilizar os dois cupons na mesma compra.

---

## 3. Classes de Equivalência

### Valor do pedido

| Classe |        Faixa de valor | Comportamento esperado                                                                 |
| ------ | --------------------: | -------------------------------------------------------------------------------------- |
| CE01   |        Valor negativo | Valor inválido                                                                         |
| CE02   |    R$ 0,00 a R$ 99,99 | Sem PROMO10 e com frete de R$ 25,00                                                    |
| CE03   | R$ 100,00 a R$ 199,99 | PROMO10 permitido e frete de R$ 25,00, considerando o valor após desconto              |
| CE04   |     R$ 200,00 ou mais | Frete grátis quando o valor considerado para a regra for igual ou superior a R$ 200,00 |

### Cupons

| Classe | Condição                         | Comportamento esperado |
| ------ | -------------------------------- | ---------------------- |
| CE05   | PROMO10 em pedido ≥ R$ 100,00    | Cupom aceito           |
| CE06   | PROMO10 em pedido < R$ 100,00    | Cupom recusado         |
| CE07   | PRIMEIRACOMPRA em qualquer valor | Cupom aceito           |
| CE08   | Dois cupons na mesma compra      | Operação recusada      |

---

## 4. Valores Limite

Os principais valores-limite identificados são:

* **R$ 99,99** – último valor em que o `PROMO10` não pode ser utilizado.
* **R$ 100,00** – primeiro valor em que o `PROMO10` pode ser utilizado.
* **R$ 199,99** – último valor abaixo do limite de frete grátis.
* **R$ 200,00** – valor mínimo para frete grátis antes da aplicação de descontos.
* **R$ 200,01** – primeiro valor acima do limite de frete grátis.

Também são importantes os testes em que o desconto faz o valor cair abaixo de R$ 200,00, pois o desconto deve ser aplicado antes da verificação do frete.

---

## 5. Casos de Teste

| ID   | Descrição do Cenário                           | Valor (R$) | Cupom                    | Resultado Esperado                   |
| ---- | ---------------------------------------------- | ---------: | ------------------------ | ------------------------------------ |
| CT01 | Testar frete grátis no limite mínimo           |     200,00 | Nenhum                   | R$ 200,00 – frete grátis             |
| CT02 | Testar cobrança de frete abaixo do limite      |     199,99 | Nenhum                   | R$ 224,99 – R$ 199,99 + R$ 25,00     |
| CT03 | Testar frete grátis acima do limite            |     200,01 | Nenhum                   | R$ 200,01 – frete grátis             |
| CT04 | Testar PROMO10 abaixo do limite                |      99,99 | PROMO10                  | Cupom recusado; total R$ 124,99      |
| CT05 | Testar PROMO10 exatamente no limite            |     100,00 | PROMO10                  | R$ 115,00 – R$ 90,00 + R$ 25,00      |
| CT06 | Testar PROMO10 em pedido de R$ 150,00          |     150,00 | PROMO10                  | R$ 160,00 – R$ 135,00 + R$ 25,00     |
| CT07 | Testar precedência do PROMO10 sobre o frete    |     200,00 | PROMO10                  | R$ 205,00 – R$ 180,00 + R$ 25,00     |
| CT08 | Testar PRIMEIRACOMPRA abaixo de R$ 200,00      |     150,00 | PRIMEIRACOMPRA           | R$ 145,00 – R$ 120,00 + R$ 25,00     |
| CT09 | Testar PRIMEIRACOMPRA no limite de R$ 200,00   |     200,00 | PRIMEIRACOMPRA           | R$ 195,00 – R$ 170,00 + R$ 25,00     |
| CT10 | Testar PRIMEIRACOMPRA acima do limite          |     230,00 | PRIMEIRACOMPRA           | R$ 200,00 – R$ 200,00 + frete grátis |
| CT11 | Tentar aplicar PROMO10 em pedido inválido      |      50,00 | PROMO10                  | Cupom recusado; total R$ 75,00       |
| CT12 | Testar PRIMEIRACOMPRA em pedido de baixo valor |      50,00 | PRIMEIRACOMPRA           | R$ 45,00 – R$ 20,00 + R$ 25,00       |
| CT13 | Tentar utilizar os dois cupons simultaneamente |     150,00 | PROMO10 + PRIMEIRACOMPRA | Operação recusada                    |
| CT14 | Testar pedido de R$ 100,00 sem cupom           |     100,00 | Nenhum                   | R$ 125,00 – R$ 100,00 + R$ 25,00     |
| CT15 | Testar pedido acima do limite sem cupom        |     250,00 | Nenhum                   | R$ 250,00 – frete grátis             |

---

## 6. Análise dos Principais Casos

### CT01 – Frete grátis no limite

O pedido possui valor de R$ 200,00 e não utiliza cupom.

Como o valor é exatamente igual ao limite estabelecido, o sistema deve conceder frete grátis.

**Resultado esperado: R$ 200,00.**

### CT02 – Valor imediatamente abaixo do limite

O pedido possui valor de R$ 199,99.

Como o valor é inferior a R$ 200,00, deve ser acrescentado o frete de R$ 25,00.

**Resultado esperado: R$ 224,99.**

### CT05 – PROMO10 no limite

O pedido possui valor de R$ 100,00.

Como o valor é exatamente o mínimo necessário para utilização do `PROMO10`, o cupom deve ser aceito.

10% de R$ 100,00 = R$ 10,00.

Valor após desconto = R$ 90,00.

Como R$ 90,00 é inferior a R$ 200,00, o frete será R$ 25,00.

**Resultado esperado: R$ 115,00.**

### CT07 – Desconto antes do frete

Este é um dos testes mais importantes.

O pedido possui valor de R$ 200,00 e utiliza o `PROMO10`.

O desconto é aplicado primeiro:

R$ 200,00 - 10% = R$ 180,00.

Depois disso, o sistema verifica o frete.

Como R$ 180,00 é inferior a R$ 200,00, o cliente deve pagar R$ 25,00 de frete.

**Resultado esperado: R$ 205,00.**

### CT13 – Dois cupons

O cliente tenta utilizar `PROMO10` e `PRIMEIRACOMPRA` simultaneamente.

Como o sistema não permite mais de um cupom por compra, a operação deve ser recusada.

---

## 7. Conclusão

Os casos de teste foram elaborados utilizando as técnicas de **Classes de Equivalência** e **Análise de Valor Limite**.

Foram considerados os principais pontos de mudança de comportamento do sistema, principalmente os limites de **R$ 100,00** para o cupom `PROMO10` e de **R$ 200,00** para o frete grátis.

Também foram testados cenários envolvendo a aplicação dos cupons, a combinação entre descontos e frete, a utilização inválida do `PROMO10` e a tentativa de utilização simultânea dos dois cupons.

Com esses testes, é possível verificar se as principais regras de negócio do carrinho estão sendo aplicadas corretamente.
