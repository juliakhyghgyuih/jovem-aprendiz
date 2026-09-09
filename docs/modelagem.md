# Modelagem do MVP Evolui

## Problema

Jovens que procuram a primeira oportunidade profissional podem ter dificuldade para encontrar vagas de Jovem Aprendiz e entender os requisitos de cada oportunidade.

## Público-alvo

- Jovens em busca da primeira experiência profissional.
- Empresas interessadas em divulgar vagas de Jovem Aprendiz.

## Funcionalidades do MVP

- Tela inicial com acesso aos perfis Jovem e Empresa.
- Área do jovem com pesquisa, filtros e cards de oportunidades.
- Visualização dos detalhes de uma vaga.
- Registro demonstrativo de candidatura.
- Consulta de minhas candidaturas.
- Edição demonstrativa do perfil do jovem.
- Painel da empresa com perfil, publicação de vagas, minhas vagas e candidatos.
- Mensagens de confirmação, aviso e erro.

Na versão apresentada nesta etapa, os dados das telas são exemplos mantidos em memória. Isso permite demonstrar a interface e a navegação pelo VS Code sem depender de um servidor de banco. A persistência descrita abaixo representa a modelagem planejada para a próxima etapa.

## Informações planejadas para armazenamento

### Tabela usuarios

- id
- nome
- email
- senha
- tipo (`jovem` ou `empresa`)

### Tabela perfis

- id
- usuario_id
- idade
- cidade
- telefone
- escolaridade
- curso
- habilidades

### Tabela empresas

- id
- usuario_id
- nome
- cnpj
- cidade
- email
- telefone

### Tabela oportunidades

- id
- titulo
- empresa
- area
- cidade
- descricao
- requisitos
- quantidade_vagas
- empresa_id
- salario
- beneficios

### Tabela candidaturas

- id
- usuario_id
- oportunidade_id
- status
- data_candidatura

## Entidades e responsabilidades

- `Usuario`: representa o acesso principal do usuário.
- `Jovem`: representa os dados profissionais do candidato.
- `Perfil`: reúne escolaridade, cidade, cursos e habilidades.
- `Empresa`: representa a organização que oferece vagas.
- `Oportunidade`: representa uma vaga de Jovem Aprendiz.
- `Candidatura`: relaciona um jovem a uma oportunidade.
- `Sessao`: mantém temporariamente o usuário durante a execução.
- `BancoEvolui`: concentra o acesso planejado ao MySQL.
- `TelaLogin`, `TelaJovem`, `TelaOportunidades` e `TelaEmpresa`: encapsulam as interfaces e ações do usuário.

## Relacionamentos

```text
usuarios 1 : 1 perfis
empresas 1 : N oportunidades
usuarios 1 : N candidaturas N : 1 oportunidades
```

## Organização orientada a objetos

`Evolui` coordena a janela inicial e a navegação entre telas. As classes de `views/` cuidam da interação visual, enquanto as classes de `models/` representam o domínio. A classe `Sessao` mantém o estado do fluxo e o acesso ao banco está separado em `conexao.py` e `dados.py`.

## Fluxo demonstrável

1. Abrir o sistema.
2. Entrar como jovem.
3. Consultar uma oportunidade.
4. Visualizar os detalhes.
5. Candidatar-se.
6. Consultar minhas candidaturas.

Como fluxo alternativo, entrar como empresa, salvar o perfil demonstrativo, publicar uma oportunidade e consultar minhas vagas e candidatos.
