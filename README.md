# Projeto de Testes Automatizados — Qualidade de Software

Centro Universitário Senac-RS  
Curso: ADS / SPI  
Unidade Curricular: Qualidade de Software  
Prof.: Luciano Zanuz  
Integrante: **Eduarda Toppor de Araujo**

## Objetivo
Desenvolver testes automatizados funcionais e unitários com Python e Selenium.

## Ferramentas
- Python 3.11
- Selenium WebDriver
- Pytest + Pytest-HTML
- WebDriver Manager

## Como executar
1. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute todos os testes:
   ```bash
   pytest --html=docs/evidencias/report.html -q
   ```
3. Verifique evidências:
   - Relatório HTML e screenshots em `docs/evidencias/`.

## Estrutura
src/ → código fonte  
tests/ → testes funcionais e unitários  
docs/evidencias/ → relatórios e imagens

## Aplicação testada
https://www.saucedemo.com/

## Cenários de teste
- Login (sucesso, bloqueado, inválido)
- Checkout (completo, carrinho vazio)
- Funções de cálculo e validação de e-mail

## Evidências esperadas
- report.html
- login_sucesso.png
- checkout_completo.png
- etc.
