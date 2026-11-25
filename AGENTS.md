# AGENTS.md — Como adicionar materiais ao ELEV

Este repositório contém um site estático de estudo para a formação profissional de logística. Os materiais são apresentados em dinamarquês (DA), inglês (EN) e português brasileiro (PT). O objetivo é permitir que a aprendiz estude autonomamente em qualquer dos três idiomas e pratique o vocabulário técnico em dinamarquês.

## 1. Antes de começar

- Consulte o HEAD da branch `main`, o README, a estrutura real do repositório e a implementação dos materiais já publicados. Não parta de uma cópia local desatualizada.
- Identifique se o novo documento pertence a um material existente ou constitui um novo livro/curso. Compare o índice e as fontes para evitar duplicação.
- Preserve as URLs, as chaves de armazenamento local, o conteúdo anterior e as funcionalidades existentes. Não recrie o site do zero.
- Verifique quais páginas são geradas pelos scripts e quais contêm alterações estáticas posteriores. Em particular, `programme/index.html` contém o Elevmappe integralmente traduzido e a navegação própria; uma regeneração indiscriminada poderá sobrescrevê-lo. Não execute nem publique um build que elimine essas alterações.
- Não presuma que as autorizações de publicação de materiais anteriores se aplicam automaticamente a todo novo documento. Use o escopo autorizado pelo usuário.

## 2. PRE-CHECK obrigatório — privacidade e publicação

Faça a inspeção **antes** de gerar páginas públicas ou enviar qualquer arquivo ao GitHub. O repositório pode estar publicamente acessível; não presuma que seja privado.

- [ ] Examine o conteúdo de todos os documentos, inclusive cabeçalhos, rodapés, tabelas, notas, anexos, caixas de texto, imagens, metadados e links. Inspecione arquivos dentro de ZIPs e aplique OCR quando necessário.
- [ ] Identifique nomes de pessoas, fotografias identificáveis, endereços, telefones, e-mails, documentos de identidade, números pessoais, assinaturas, dados de alunos, formulários preenchidos e outros identificadores. Omitir ou anonimizar antes de publicar.
- [ ] Verifique se há informações empresariais confidenciais, credenciais, links privados ou dados operacionais que não estejam autorizados para publicação. Distinga material didático autorizado de informação interna.
- [ ] Prefira remover seções exclusivamente pessoais (por exemplo, listas de professores com fotos e contatos), sem eliminar conteúdo curricular associado.
- [ ] Preserve formulários em branco e conteúdo curricular autorizado. Não publique dados preenchidos nem dados pessoais embutidos nas imagens ou metadados.
- [ ] Não publique os documentos originais deste material quando não houver autorização específica para isso. Para o Elevmappe 2026, publique somente o material gerado e anonimizado; o DOCX original permanece fora do repositório. Não copie automaticamente os arquivos recebidos para `sources/`.
- [ ] Faça uma segunda inspeção no resultado efetivo a publicar: HTML de todos os idiomas, JSON, arquivos Python/JavaScript, índices de busca, imagens e demais recursos. Dados removidos do HTML não podem permanecer ocultos no código, em outros idiomas, no índice ou em arquivos auxiliares.
- [ ] Se houver dúvida material sobre autorização ou confidencialidade, esclareça somente o ponto necessário com o usuário. Continue o trabalho de transformação local que não dependa da autorização.

O pre-check só é aprovado quando o conjunto de arquivos destinado à publicação estiver de acordo com a autorização aplicável e não contiver dados que precisem ser anonimizados.

## 3. Estrutura e fidelidade ao conteúdo

1. Extraia todos os elementos relevantes do material original na ordem em que aparecem: títulos, subtítulos, parágrafos, listas, tabelas, figuras, notas, formulários, atividades e referências.
2. Preserve hierarquia, numeração, sequência, valores, unidades, datas e significado. Adapte o layout à leitura em HTML responsivo, sem substituir o conteúdo original por um resumo.
3. Mantenha separadas as explicações didáticas complementares, os resumos e as traduções do texto original. Identifique lacunas da fonte; não invente informação.
4. Para links, artigos e vídeos relevantes ao aprendizado, examine as fontes disponíveis, prepare explicações úteis e identifique materiais não acessíveis. Não invente transcrições.
5. Para materiais que incluem questões ou respostas, mantenha o exercício separado do gabarito. Gabaritos devem ficar ocultos inicialmente, inclusive se a fonte contém as respostas. Preserve a alternância por duplo clique no número do capítulo e a tecla Esc para ocultar novamente.
6. Não introduza alterações não solicitadas em outros livros. Evite renumerar capítulos existentes.

## 4. Tradução integral — DA, EN e PT

A versão DA deve preservar o conteúdo autorizado da fonte. EN e PT devem ser traduções completas do mesmo conteúdo, e não apenas traduções de títulos, do primeiro parágrafo ou de um resumo.

- Traduza cada parágrafo, frase, item de lista, título, legenda, nota, célula de tabela, rótulo de formulário, pergunta, resposta e instrução.
- Mantenha nomes de instituições, siglas, códigos, marcas, URLs e termos técnicos que devam permanecer no original. Use terminologia consistente e português brasileiro natural.
- Preserve o número de linhas e células das tabelas, a ordem dos blocos, os valores numéricos e as relações entre as informações.
- Use equivalentes técnicos corretos; mantenha termos dinamarqueses úteis para estudo com traduções ou tooltips, conforme a implementação existente.
- Não marque como traduzido um painel que ainda contém o texto dinamarquês copiado como fallback. Se usar tradução automática, revise a cobertura, a fidelidade e a terminologia, identifique essa abordagem quando necessário e não apresente uma tradução não revisada como tradução humana.
- Não dependa de um serviço externo de tradução no navegador para disponibilizar o conteúdo. As três versões completas devem estar prontas no HTML ou nos dados estáticos entregues.

## 5. Navegação e interface

- Na página inicial, liste os livros/cursos; dentro de um livro, o menu lateral deve listar **somente os capítulos daquele livro**, na ordem original. Não misture capítulos de outros materiais.
- Renderize os itens principais diretamente no HTML; use JavaScript para aprimorar a navegação, trocar idiomas, destacar o capítulo ativo e fechar o menu móvel. Não dependa de JavaScript para corrigir um menu lateral estático incorreto.
- A navegação do Elevmappe 2026 possui 17 capítulos principais. A de Logística possui nove. Preserve essas estruturas, exceto quando a alteração solicitada exigir outra organização.
- Todos os links e âncoras devem funcionar nos três idiomas. Os identificadores das seções correspondentes devem permitir manter a posição ao alternar o idioma.
- Preserve TTS e integração com Øv Dansk somente em DA, seleção de vocabulário, notas locais, marcação de leitura, gabaritos, pesquisa e navegação entre páginas. Não altere autenticação ou permissões sem solicitação.
- Verifique desktop e mobile, inclusive tabelas largas e o menu recolhível. Evite mudanças que quebrem a experiência existente.
- Ao modificar recursos compartilhados, invalide o cache dos recursos afetados quando necessário; verifique também o HTML efetivamente servido, não apenas o arquivo no repositório.

## 6. QUALITY GATE obrigatório — antes de publicar

Não considere o trabalho concluído enquanto houver conteúdo autorizado sem tradução, links quebrados, dados pessoais indevidos ou regressões relevantes.

### A. Cobertura estrutural e tradução

- [ ] Gere um inventário dos blocos de conteúdo da fonte autorizada (seções, parágrafos, itens de lista, células, legendas, notas, exercícios e formulários). Compare com os três idiomas usando identificadores correspondentes, não apenas contagem total de palavras.
- [ ] Confirme que todos os blocos da fonte autorizada têm correspondentes DA, EN e PT; conte os elementos por tipo e reporte as diferenças. Qualquer exclusão deliberada por anonimização deve ser identificada, sem divulgar os dados removidos.
- [ ] Cada bloco textual não vazio de DA tem tradução não vazia em EN e PT. Nenhum parágrafo, célula ou lista pode ficar em DA por falta de tradução. Compare os textos normalizados e procure blocos idênticos ou predominantemente dinamarqueses. Analise manualmente as exceções legítimas (siglas, nomes de produtos, URLs, números etc.); a igualdade isolada não é prova de falha.
- [ ] Confirme que nenhuma tradução ficou truncada: revise frases longas, múltiplas frases por parágrafo, listas, requisitos, instruções, tabelas e formulários. Uma contagem igual de blocos não garante que todas as frases foram traduzidas.
- [ ] Revise a precisão semântica das três versões, com prioridade para objetivos de aprendizagem, conceitos técnicos, instruções obrigatórias, notas, datas, números e fórmulas. Corrija termos inconsistentes, omissões, frases incompreensíveis ou erros de tradução antes de aprovar.
- [ ] Inspecione o texto renderizado de EN e PT, incluindo seções do início, meio e fim, e tabelas complexas. Não confunda um resumo traduzido com o conteúdo integral traduzido.

### B. Privacidade, funcionamento e regressões

- [ ] Repita o pre-check sobre o conjunto final de arquivos, inclusive recursos não visíveis.
- [ ] Execute os testes disponíveis no repositório (por exemplo, `python scripts/check.py`, `node --check assets/app.js` e `node --check assets/vocabulary.js`), quando aplicáveis. Não modifique as próprias verificações apenas para mascarar erros.
- [ ] Valide links e fragmentos, IDs únicos, três painéis linguísticos e âncoras equivalentes. Use inspeção estrutural automatizada quando possível.
- [ ] Teste a página em um navegador: abra cada material, conte as entradas do menu lateral, clique em capítulos distintos, alterne DA/EN/PT no mesmo trecho e confira tabelas, notas, gabaritos e comportamento móvel pertinente. Testes de HTML/DOM não substituem completamente a verificação visual e interativa; informe se não foi possível executá-la.
- [ ] Confira o diff contra a branch atual. Nenhum arquivo não relacionado deve ter sido alterado ou publicado por acidente.

## 7. Publicação e verificação final

- Publique somente os arquivos necessários e autorizados no repositório existente, preferencialmente em um commit coerente na branch `main`, seguindo a solicitação do usuário. Não publique originais ou artefatos intermediários indevidamente.
- Se uma revisão automática bloquear o envio, identifique o arquivo e o motivo concretos. Corrija o problema de anonimização ou autorização por uma via permitida, sem contornar a rejeição. Preserve o progresso e informe ao usuário se restar um bloqueio real.
- Confira que o commit está efetivamente na branch de destino e aguarde a atualização do GitHub Pages. Valide a URL do site publicado, o conteúdo novo e os recursos estáticos. Se necessário, use uma URL com versão ou parâmetro de cache para testar a publicação.
- Uma tarefa não está concluída somente porque os arquivos existem localmente, porque um commit foi criado ou porque foi publicado um resumo. Continue até a implementação, tradução integral, validação e publicação solicitadas estarem concluídas, ou até encontrar um impedimento concreto que não possa resolver.
- Informe na resposta final: alterações feitas, quantidade de capítulos/blocos/tabelas quando relevante, verificações aprovadas, commit, URL publicada e quaisquer limitações reais. Nunca declare um teste que não foi executado.
