# Roteiro de apresentação do MVP

## Execução

No VS Code, abrir **Executar e Depurar**, selecionar **Evolui - Tkinter** e pressionar `F5`.

## Fluxo do jovem

1. Tela inicial → **Entrar**.
2. Login → **Entrar como Jovem**.
3. Área do jovem → **Ver oportunidades**.
4. Usar a pesquisa ou os filtros.
5. Clicar em **Ver vaga**.
6. Conferir descrição, requisitos e benefícios.
7. Clicar em **Candidatar-se** e mostrar a confirmação.
8. Abrir **Minhas candidaturas**.
9. Abrir **Meu perfil**, salvar uma alteração e clicar em **Sair**.

## Fluxo da empresa

1. Tela inicial → **Sou Empresa**.
2. Login → **Entrar como Empresa**.
3. Mostrar as abas de perfil, nova oportunidade, minhas vagas e candidatos.
4. Salvar os dados demonstrativos da empresa.
5. Publicar uma vaga preenchendo o formulário.
6. Abrir **Minhas vagas** e mostrar a vaga publicada.
7. Abrir **Candidatos**.
8. Clicar em **Sair**.

## Explicação técnica

- `main.py` inicia a aplicação.
- `views/` contém as telas Tkinter.
- `models/` contém as entidades do domínio.
- `sessao.py` mantém o estado do usuário durante a demonstração.
- `dados.py` e `conexao.py` estão separados para a futura integração com MySQL.
- O MVP atual usa dados em memória para priorizar a demonstração da interface e da navegação.

## Limites e próximas etapas

A autenticação real e a persistência no banco ainda serão conectadas. Também ficam para a próxima etapa os controles de permissão, fechamento de vagas e atualização persistente de candidaturas.