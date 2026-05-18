# PROCESSO — Adaptar Imagens do `index.html` da J.R. Company

> Documento-fonte para execução. Cada fase tem ≤14 passos para manter foco da automação.
> Versão 1.0 · 2026-05-13

---

## 1. Objetivo do Processo

Claude escaneia a pasta local da J.R. Company, **vê visualmente** cada imagem candidata, e para cada um dos **10 slots** do `index.html` (4 cards de serviços, 3 cases, 3 artigos de blog):

1. Recomenda a melhor foto local + alternativa(s)
2. Quando não houver foto adequada (ou for fraca), gera um **prompt em inglês para ChatGPT/DALL-E** no estilo visual da J.R. Company
3. Entrega: relatório `.md` para validação, depois pasta `/images-site/` organizada e `index.html` editado

O hero scroll (4 telas iniciais) **está fora do escopo** — já tem solução.

---

## 2. Usuário / Destinatário

- **Cliente:** J.R. COMPANY — Logística e Engenharia de Precisão
- **Executor:** Juan Sebastian (operador) + Claude (automação)
- **Site:** `index.html` em `C:\Users\hx-co\OneDrive\Documentos\brigth\JR Company\VERSAO 5 (2) 08-05-26 16\VERSAO 5 (2)\VERSAO 1\`

---

## 3. Fluxo Passo a Passo (5 Fases · ≤14 passos cada)

### FASE 1 — Setup & Inventário (10 passos)

1. Ler o `index.html` da pasta de trabalho
2. Identificar e listar os 10 slots de imagem do escopo (cards/cases/blog), guardando para cada um: `id`, `seção`, `alt-text atual`, `URL atual`, `proporção esperada`
3. Criar backup `index.html.bak` no mesmo diretório
4. Escanear apenas pastas permitidas:
   - `/video header/`
   - `/video header/frames/finais/`
   - `/Geral Glow 2026/`
   - Raiz `/JR Company/`
5. Ignorar caminhos que contenham: `/sequence/`, `/frames gif/`, `/_originais/`, `/Maersk*/`, `/_files/`, `/VERSAO 4`, `/VERSAO 4 (1) backup`
6. Filtrar extensões válidas: `.jpg .jpeg .png .webp .gif`
7. Excluir arquivos óbvios não-fotográficos: logos (`logo s.png`, `Group.*`, `Vector.png`, `Ellipse 1.*`, `textura 1.svg`)
8. Gerar `inventario-imagens.json` com a lista de candidatas (caminho absoluto + nome + tamanho em bytes)
9. Contar e reportar total de candidatas
10. Salvar inventário e fim da Fase 1

### FASE 2 — Análise Visual (14 passos)

1. Ler `inventario-imagens.json`
2. Iniciar lista vazia `catalogo-visual.json`
3. Para cada imagem da lista, ler-a com a ferramenta de leitura visual
4. Para cada imagem analisada, registrar:
   - `caminho`
   - `sujeito_principal` (ex: caminhão J.R., transformador, refinaria, plano técnico, equipe)
   - `tema_dominante` (ex: içamento, transporte, armazenagem, internacional, blueprint)
   - `ambiente` (rodovia, planta industrial, galpão, exterior, interior)
   - `temos_logo_jr` (sim/não)
   - `iluminacao` (golden hour, dia claro, indoor, baixa luz)
   - `qualidade_subjetiva` (alta/média/baixa — só informativo, não disqualifica)
   - `tags` (palavras-chave para o matching)
5-13. Continuar análise em lote (Claude vê uma a uma; pode pausar e retomar se inventário for grande)
14. Salvar `catalogo-visual.json` completo

### FASE 3 — Mapeamento dos 10 Slots (12 passos)

1. Carregar `catalogo-visual.json`
2. Definir critérios temáticos para cada slot:
   - **Card 1 — Cargas Excedentes:** caminhão prancha + carga industrial grande em rodovia
   - **Card 2 — Içamento Industrial:** guindaste, içamento de equipamento pesado, gruas
   - **Card 3 — Logística de Armazém:** galpão, paletes, organização interna
   - **Card 4 — Internacional:** contêineres, porto, navio, fronteira
   - **Case 1 — Indústria de base:** transformador, refinaria, planta industrial
   - **Case 2 — Setor de energia:** torres, equipamentos de geração, usinas
   - **Case 3 — Construção pesada:** estruturas metálicas, obra de grande porte
   - **Blog 1 — Dimensionar cargas:** mesa técnica com blueprint/calculadora, medição
   - **Blog 2 — Planejamento técnico:** engenheiros consultando planta, software CAD
   - **Blog 3 — Erros críticos:** cena conceitual de risco/atenção em operação
3. Para cada slot, filtrar candidatas do catálogo que combinam tematicamente
4. Ranquear candidatas por força do match temático
5. Regra de unicidade: cada foto só pode ser escolhida para 1 slot — se uma foto for top em dois slots, atribui ao slot onde for mais forte, e o outro fica com a 2ª opção
6. Para empates técnicos (3+ fotos igualmente boas), marcar todas como "candidatas para escolha manual"
7. Para slots sem nenhuma candidata sólida, marcar `fallback_ia = true`
8. Para slots com candidata fraca, marcar `fallback_ia = recomendado` (oferece foto + prompt IA)
9. Gerar `mapeamento-slots.json` com a decisão por slot
10. Verificar: nenhuma foto repetida entre slots
11. Verificar: todos os 10 slots têm decisão (foto, candidatas, ou fallback IA)
12. Salvar e fim da Fase 3

### FASE 4 — Prompts de IA + Relatório (10 passos)

1. Carregar `mapeamento-slots.json`
2. Para cada slot marcado com `fallback_ia`, gerar prompt em **inglês** seguindo o template visual da J.R. Company (ver seção 6 deste documento)
3. Cards/Cases: prompt com caminhão J.R. Company protagonista, golden hour ou céu azul, hiperrealista
4. Blog: prompt sem caminhão obrigatório, mesma família visual (luz, paleta, nitidez), sujeito editorial/conceitual
5. Criar arquivo `recomendacoes-imagens.md` com a seguinte estrutura por slot:
   ```
   ## Slot N — [Nome do slot]
   **Escolha recomendada:** [caminho relativo]
   **Alternativa(s):** [caminho(s)]
   **Razão:** [explicação visual + temática]
   **Empate? (candidatas para escolha manual):** [se aplicável]
   **Prompt IA (fallback):** [se aplicável, em inglês, pronto para colar no ChatGPT]
   ```
6. Adicionar sumário no topo: quantos slots com foto local, quantos com fallback IA, quantos com empate
7. Adicionar seção "como aprovar": instruções claras de como tu respondes (ex: "no slot 3 troca para alternativa", "no slot 7 vai com o prompt IA")
8. Salvar `recomendacoes-imagens.md` em `VERSAO 1\`
9. **PAUSA: esperar tua validação por escrito antes da Fase 5**
10. Confirmar entrega do relatório

### FASE 5 — Execução Final (12 passos)

1. Aguardar tuas decisões (lista de aprovações/trocas por slot)
2. Criar pasta `/images-site/` em `VERSAO 1\`
3. Para cada slot aprovado:
   - Se foto local: copiar para `/images-site/` com nome claro (ex: `card-cargas-excedentes.jpg`)
   - Se prompt IA aprovado: deixar placeholder e registrar prompt em `images-site/_prompts-ia.md` para tu gerares no ChatGPT
4. Garantir que cada arquivo copiado tem nome único e descritivo
5. Reler o `index.html` original
6. Para cada slot, substituir o `src="..."` antigo pelo novo caminho relativo `./images-site/[nome-novo].jpg`
7. Manter `alt-text` atual a menos que tu peças mudança
8. Para slots com prompt IA pendente: deixar comentário HTML `<!-- IA-PENDING: ver _prompts-ia.md -->` perto do `<img>`
9. Salvar o `index.html` (sobrescreve o original — backup `.bak` já existe da Fase 1)
10. Gerar `_resumo-execucao.md` na pasta `/images-site/` com lista do que foi feito por slot
11. Confirmar: backup existe, pasta `/images-site/` existe, index editado
12. Fim do processo

---

## 4. Inputs Necessários

- **`index.html`** em `C:\Users\hx-co\OneDrive\Documentos\brigth\JR Company\VERSAO 5 (2) 08-05-26 16\VERSAO 5 (2)\VERSAO 1\`
- **Acesso de leitura** à pasta `JR Company\` completa
- **Tua validação** entre Fase 4 e Fase 5

---

## 5. Outputs Esperados

Na pasta `VERSAO 1\`:
- `index.html.bak` — backup do original
- `inventario-imagens.json` — lista bruta (intermediário)
- `catalogo-visual.json` — catálogo com descrições visuais (intermediário)
- `mapeamento-slots.json` — decisão por slot (intermediário)
- `recomendacoes-imagens.md` — relatório para validação humana ← **chave**
- `index.html` — editado ← **chave**
- `/images-site/` — pasta com fotos selecionadas e renomeadas ← **chave**
- `/images-site/_resumo-execucao.md` — log final
- `/images-site/_prompts-ia.md` — prompts para tu gerares no ChatGPT (se aplicável)

---

## 6. Regras Principais

### DNA Visual J.R. Company (template para prompts de IA — em inglês)

**Base universal (sempre incluir):**
```
hyperrealistic photography, Brazilian industrial logistics setting,
sharp focus, rich natural saturation, no heavy filters,
shot on professional DSLR look, 4K cinematic quality
```

**Para Cards e Cases (com caminhão J.R.):**
```
[Base universal] + a J.R. Company branded truck (white cab with red and green
accents, J.R. COMPANY logo on the cab door, Brazilian flag detail),
[carga ou ação específica do slot], golden hour OR clear blue sky midday,
low heroic angle OR aerial drone shot, deep landscape perspective,
sense of scale and pride, industrial logistics brand photography style
```

**Para Blog (sem caminhão obrigatório):**
```
[Base universal] + [sujeito conceitual do artigo: engineers studying
technical blueprints, CAD design on a screen, cargo being measured/inspected],
industrial Brazilian environment, same lighting palette and saturation,
editorial photography, depth of field, professional and trustworthy mood
```

### Outras regras

- Critério único de match: **temática**. Resolução, ruído, pixelação **não importam** — usuário corrige depois.
- **Unicidade absoluta:** cada foto usada apenas 1× no site.
- **Empates** (3+ fotos boas) → listar todas no relatório, decisão manual.
- **Sem foto + IA fraca** → entregar prompt IA mesmo genérico, com nota de aviso.
- **Mudanças na pasta** depois de rodar → rerun completo, sempre do zero.
- `alt-text` atual do `index.html` **se mantém** salvo pedido explícito.
- `index.html` é sobrescrito (backup `.bak` é a rede de segurança).

---

## 7. Exceções e Casos-Limite

| Caso | Ação |
|------|------|
| Empate técnico (3+ candidatas equivalentes) | Listar todas no relatório como "escolha manual" |
| Foto perfeita para 2 slots | Atribuir ao slot mais forte; o outro vai para 2ª opção |
| Nenhuma foto temática + IA também fraca | Gerar prompt IA mesmo genérico, com nota de aviso explícita |
| Foto com marca d'água / copyright visível | Sinalizar no relatório, não usar sem confirmação |
| Pasta muda durante a execução | Não detectar mid-run; novo input = rerun total do zero |
| Slot do `index.html` que não tem foto correspondente | Manter URL original com nota no relatório |

---

## 8. Critérios de Qualidade

O processo é bem sucedido se:
- Os 10 slots têm uma decisão clara (foto ou prompt IA)
- O relatório `.md` é legível e permite decisão em 5 minutos
- Nenhuma foto é repetida entre slots
- O `index.html` editado abre no browser sem quebrar referências
- O backup `.bak` existe e funciona
- A pasta `/images-site/` tem nomes claros e descritivos
- Os prompts de IA (quando aplicável) seguem o template do DNA visual

---

## 9. Riscos e Ambiguidades Pendentes

- **`alt-text` automático para IA-generated:** se um slot for preenchido por imagem gerada por IA depois, o `alt-text` ainda será o atual do `index.html`. Decidir se Claude também atualiza o alt-text quando tu colares a imagem de IA.
- **Direitos de uso das fotos:** assumido que todas as fotos da pasta `JR Company\` são propriedade ou licenciadas pela empresa. Não há verificação automática.
- **Performance da Fase 2:** análise visual de potencialmente 50-100+ fotos pode ser longa. Se exceder, talvez seja necessário dividir Fase 2 em sub-rounds.
- **Estética dos artigos de Blog:** o DNA visual foi calibrado em fotos com caminhão. Resultados conceituais (engenheiros, blueprint, mesa técnica) podem variar — primeira execução é experimento.

---

## 10. Próxima Ação Recomendada

**Quando tu disseres "vamos começar":**
1. Claude inicia a **FASE 1 — Setup & Inventário** imediatamente
2. Ao terminar Fase 1, mostra um sumário curto ("X candidatas encontradas em Y pastas") e pergunta se segue para a Fase 2
3. Claude segue fase a fase, pausando ao final de cada uma
4. Pausa obrigatória entre **Fase 4 e Fase 5** para tua validação do relatório

---

*Documento gerado pela entrevista de processo. Mantém este arquivo em `VERSAO 1\` como referência durante toda a execução.*
