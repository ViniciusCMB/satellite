# Mission Report — Pontos de Melhoria (2026-08-06)

Auditoria visual: sensação de amadorismo identificada e categorizada.

---

## 1. Abstract parede de texto
- **Problema**: 120+ palavras em único parágrafo
- **Padrão profissional**: 150 palavras máx, 3-5 frases (objetivo → método → resultado → implicação)
- **Ação**: Condensar para ~100 palavras

## 2. Tabelas com formatação inconsistente
- **Problema**: mix de `tabular`, `tabularx`, casas decimais variadas
- **Padrão profissional**: `tabularx` uniforme, colunas `>{\raggedright}p{5cm}X`, casas decimais padronizadas (2 vel, 1 ângulos, 0 RPM)
- **Ação**: Unificar todas as tabelas

## 3. Profundidade desigual entre seções
- **Problema**: Introduction tem 4 pág, Conclusions tem 1 pág, Appendices vazios
- **Padrão profissional**: todas as seções com profundidade proporcional; Conclusions com lições específicas + Future Work
- **Ação**: Expandir Conclusions, adicionar Future Work

## 4. Falta de contexto competitivo
- **Problema**: não compara com outras abordagens de recuperação para PocketQubes
- **Padrão profissional**: tabela comparativa (paraquedas, airbag, SRAB)
- **Ação**: Adicionar tabela comparativa brevemente

## 5. Tom oscila entre acadêmico e pessoal
- **Problema**: frases emocionais ("pain of losing everything") misturadas com texto técnico
- **Padrão profissional**: narrativa pessoal ok na Introduction, resto técnico e direto
- **Ação**: Revisar tom nas seções técnicas

---

## Notas adicionais
- Figure 4 caption mostra v_term = 13.4 m/s vs texto 13.33 m/s (arredondamento na imagem)
- Faltam imagens físicas (PCB, estrutura, integração) — dependem de hardware
- Faltam desenhos dimensionais nos appendices — dependem de CAD

---

## Prioridade de execução
1. Condensar abstract ✅ (feito 06-ago)
2. Adicionar Future Work ✅ (feito 06-ago)
3. Unificar formatação de tabelas ✅ (feito 06-ago)
4. Tabela comparativa competitiva (pendente)
5. Revisão de tom (pendente)
