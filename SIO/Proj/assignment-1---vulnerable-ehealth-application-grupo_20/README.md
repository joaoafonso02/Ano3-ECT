# Assignment-1 Vulnerable Ehealth Application - grupo_20

Project 1 - eHealth Corp

## Ideia Inicial - Fórum

Forum encaixa-se bem neste trabalho pois possui vários tipos de interação com o utilizador, o que nos permite exemplificar uma grande quantidade de falhas que fazem sentido no contexto.

## Exemplos de Inputs Perigosos

- criação de utilizadores (descubrir passes ou conseguir aceder à conta do utilizador sem necessidade de passe)
- caixa de pesquisa (pessoas ou tópicos de discução)
- mensagens privadas entre utilizadores
- criar novos tópicos (estes tópicos são de acesso público e por isso um bom alvo de cross-site scripting)
- comentários nos tópicos

## Técnologias

- frontend -> ReactJS -> interesse dos membros do grupo em aprofundar o conhecimento desta ferramenta e a sua versatilidade.
- frontend -> Bootstrap -> fácil de usar em conjunto com o react e permite queriar um melhor frontend com mais efeciencia.
- backend -> Nodejs -> o mesmo servidor usado para o frontend (react) é usado para o backend
- base de dados -> MySql -> maioritáriamente porque as falhas que vamos explorar são relativas ao sql e o mysql é uma ferramenta simples de usar

## Referencias (onde tirar ideias)

stackoverflow.com reddit.com/
