# Projeto DevOps: dupla-02

Site: https://leonardo23gs-lang.github.io/projeto-devops-dupla-02/ (status em /status.html)
Imagem: ghcr.io/leonardo23gs-lang/projeto-devops-dupla-02

## O fluxo completo
1. O git push na main dispara o CI (testes e construção da imagem) e o fluxo Publicar site com status.
2. O site só é publicado se os testes passarem, e o status.html mostra o commit e a hora da publicação.
3. Uma tag começando com v (git push origin vN) dispara o fluxo Publicar imagem.
4. Esse fluxo testa de novo, constrói a imagem com APP_VERSION igual à tag e envia para o ghcr.io.
5. Com docker pull e docker run -p 5002:5002, o contêiner sobe e responde no curl em /saude.

## Linha do tempo
- v1: primeira imagem publicada (commit 692e4b6), com a API na porta 5002 respondendo "versao":"v1".
- v2: a "Refatoração da porta" (ec39a9c) mudou a porta da API para 5003. Os testes passaram, mas o contêiner não respondeu na 5002 (curl: Empty reply from server).
- v3: voltamos para a v1 em 29 segundos (rollback operacional) e depois fizemos o git revert do commit da porta (f6d2cce), publicado como v3.

## O que os testes não pegaram
Os testes usam o test_client do Flask, que chama a aplicação sem abrir a porta de rede, então a porta errada passou sem ser notada. Para pegar isso, o pipeline poderia subir o contêiner com docker run -p 5002:5002 depois de construir a imagem e fazer um curl em /saude, falhando se não houver resposta.

## Quem fez o quê
Leonardo (aluno A, GitHub leonardo23gs-lang): criei a página de status com testes antes da publicação e ajustei o deploy do Pages quando ele falhou, conferi a visibilidade da imagem no ghcr.io, rodei as versões v1, v2 e v3 com Docker, fiz o rollback operacional para a v1 e o git revert que gerou a v3. Variação: dupla-02, porta 5002.

**Afonso (aluno B):** configurei o Docker Desktop no computador, fiz o login no GHCR e baixei as imagens v1, v2 e v3. Executei os contêineres e testei a rota /saude pelo navegador/terminal usando o curl. Durante o teste da v2, identifiquei que a aplicação estava rodando na porta 5003, enquanto o Docker estava configurado para a porta 5002. Conferi os logs para identificar o problema e realizei o rollback para a v1, confirmando que ela voltou a funcionar. Depois, baixei e executei a v3, verificando que a aplicação voltou a responder corretamente na porta 5002. Também atualizei o repositório com o git pull para receber as alterações finais do projeto.
