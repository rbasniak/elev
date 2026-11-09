# elev · estudo de logística

Site estático para a primeira etapa escolar de uma aprendiz de logística IKEA.

- `index.html`: índice geral de cursos.
- `logistik/index.html`: índice de logística.
- `logistik/01/` a `09/`: nove capítulos, com revisões e prática de recuperação da memória.
- 20 páginas de materiais, uma para cada arquivo do ZIP.
- Conteúdo de estudo alinhado em dinamarquês, inglês e português brasileiro.
- 71 termos técnicos com tradução por hover/foco nas versões inglesa e portuguesa.
- Cinco aulas escritas em DA, EN e PT para estudar sem assistir aos vídeos, com explicações por tópico e exemplos.
- Índice dos materiais originais em `source/`, com os arquivos preservados em `sources/`; correspondência e situação dos links em `sources/manifest.json`.

## Uso

Abra `index.html` em um servidor estático ou publique a raiz do repositório no GitHub Pages. Não há instalação nem build obrigatório para usar o site. `index.httml` redireciona ao nome padrão.

Use DA / EN / PT para trocar de idioma no mesmo ponto da lição. A posição é ancorada na seção correspondente e na posição relativa dentro dela. A preferência de idioma, a posição, as notas e a marcação de leitura ficam neste navegador/dispositivo. Notas não são enviadas à IKEA ou à escola.

As respostas dos exercícios ficam ocultas ao abrir ou recarregar qualquer página. Para alternar sua exibição, **dê duplo clique no número discreto do capítulo no canto inferior direito do rodapé**. `Ctrl+Shift+G` é uma alternativa de teclado. `Esc` esconde as respostas e interrompe o áudio. O modo não é persistido, também é desativado ao voltar pelo histórico, e as respostas são sempre omitidas na impressão. É um recurso de interface, não controle de acesso: as resoluções constam do código estático e alguns originais já possuem gabarito.

Os campos das atividades salvam após 500 ms. `Copiar minhas respostas` copia só o que a pessoa escreveu. Cada capítulo tem notas de recordação e marcações de revisão hoje/amanhã/em 3/em 7 dias; são marcações locais, não lembretes agendados.

## Dinamarquês e ov-dansk

Na versão DA, use `Lyt` para ouvir um bloco ou um tópico de uma aula de vídeo. O player divide textos longos, permite velocidade e interrupção, envia `no-referrer` ao Google TTS e oferece a voz do dispositivo como alternativa. Sem voz dinamarquesa instalada, o resultado do fallback depende do navegador.

Selecione até 500 caracteres no conteúdo dinamarquês para **Gem / Definition / Oversæt / Lyt**. Use a mesma conta Google do ov-dansk. Salvar pede o significado manualmente. Os termos aparecem destacados e podem ser ouvidos, editados ou excluídos. Excluir remove também `progress/custom_{id}`. A versão EN/PT não permite operações de vocabulário.

A configuração web pública do Firebase é a mesma do `rbasniak/ov-dansk/js/firebase.js`, consultada em 06/11/2026. Os SDKs são carregados somente ao ativar DA. Dados em `users/{uid}/customWords`; progresso em `users/{uid}/progress/custom_{id}`. O domínio deve constar em Firebase Authentication → Authorized domains. As regras devem restringir acesso ao `request.auth.uid`. Não alteramos regras nem permissões do projeto.

Documentação seguida:

- https://github.com/rbasniak/danske-proever/blob/main/docs/google-tts-github-pages.md
- https://github.com/rbasniak/danske-proever/blob/main/docs/saved-vocabulary-integration.md

Google Translate TTS e tradução inline usam endpoints públicos não oficiais. Falhas mostram mensagem/fallback; a leitura, traduções pré-escritas e notas locais continuam disponíveis. Ordnet abre uma aba, sem depender de CORS. Os idiomas do material são preparados no build, sem tradução automática em tempo de leitura.

## Conteúdo e limites das fontes

As páginas são adaptações didáticas e traduções alinhadas, não uma reprodução literal do layout original. Incluem conceitos, dados, perguntas, modelos de resolução, hipóteses e revisões. Os originais permitem conferir tabelas, imagens e formulação exata.

- O capítulo 6 estava vazio: recebeu apoio complementar identificado como tal.
- O exercício CoolIt (2.7) está cortado no fim do PDF: não inventamos perguntas ou resultados.
- A figura da página 33 referida no exercício 2.4 não foi enviada: o modelo de apoio é identificado.
- Instruções e códigos de avaliação de 2025 precisam de confirmação com a escola.
- A visita Hydrema não informa a data; local/horários são transcritos como informação do convite, não agenda atual confirmada.
- O link do antigo artigo SCM sobre make/buy não foi recuperado; a análise utiliza o PDF completo enviado.
- Os dois artigos online SCM foram abertos. A aula do podcast usa o artigo associado e exemplos didáticos próprios. O áudio integral não foi transcrito.
- Os cinco vídeos YouTube foram abertos e suas transcrições lidas. As aulas ampliam as sínteses originais com explicações e exemplos próprios. As transcrições completas não são redistribuídas.
- Links de plataformas escolares foram verificados sem entrar nem enviar formulários. O acesso depende da escola.
- Casos empresariais históricos não representam números atuais. Exemplos IKEA são modelos para confirmar e adaptar, sem presumir processos internos específicos.
- Denominadores diferentes, inconsistências entre narrativa/tabelas e premissas de cálculo são explicitados. O exemplo Bloodscale apresenta 84,76% na tabela versus 75% na narrativa; não misturamos os dois.

## Atualização

```sh
python scripts/build.py
python scripts/check.py
node --check assets/app.js
node --check assets/vocabulary.js
```

Edite `content/course.py`, `review.py`, `videos.py` e `glossary.py`; depois regenere. Python 3 padrão é suficiente. O build é determinístico. Os HTMLs gerados são versionados e não dependem de um servidor de aplicações. Nenhuma credencial privada deve ser incluída.
