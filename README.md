# Evolui

## Descrição

O Evolui é um aplicativo desktop para aproximar jovens que procuram a primeira oportunidade de empresas que oferecem vagas de Jovem Aprendiz.

O MVP demonstra dois fluxos: o jovem pesquisa vagas e registra uma candidatura; a empresa visualiza seu painel, publica vagas e consulta candidatos. Nesta entrega, as telas usam dados de exemplo em memória para que a aplicação possa ser apresentada sem depender do MySQL.

## Tecnologias e conceitos

- Python 3;
- Tkinter e ttk;
- Programação Orientada a Objetos;
- Visual Studio Code;
- Git e GitHub para versionamento;
- MySQL preparado para a próxima etapa de persistência.

## Funcionalidades demonstráveis

### Jovem

- acesso pela tela inicial;
- área do jovem com saudação e menu;
- pesquisa por vaga, cidade e área;
- cards com oportunidades de exemplo;
- detalhes da vaga;
- candidatura com mensagem de confirmação;
- consulta de minhas candidaturas;
- edição do perfil em memória;
- encerramento do fluxo.

### Empresa

- acesso ao painel da empresa;
- edição demonstrativa do perfil;
- publicação de vaga em memória;
- consulta de minhas vagas;
- consulta de candidatos;
- encerramento do fluxo.

## Organização do projeto

```text
evolui/
├── main.py                  # inicialização e tela inicial
├── sessao.py                # estado da sessão durante a demonstração
├── conexao.py               # conexão prevista para a etapa com MySQL
├── dados.py                 # acesso e preparação do banco futuro
├── models/                  # entidades do domínio
├── views/                   # telas Tkinter e navegação
├── docs/
│   ├── modelagem.md         # problema, entidades e relacionamentos
│   └── roteiro_apresentacao.md
└── .vscode/launch.json      # execução pelo Executar e Depurar
```

## Como executar no Visual Studio Code

1. Abra a pasta `evolui` no VS Code.
2. Abra **Executar e Depurar**.
3. Selecione **Evolui - Tkinter**.
4. Pressione `F5`.

Também é possível executar no terminal integrado:

```powershell
python main.py
```

O MVP demonstrativo não exige XAMPP, MySQL ou instalação de pacote externo. A conexão e as classes de dados permanecem organizadas para a próxima etapa, quando a persistência será ligada às telas.

## Fluxo principal para a demonstração

1. Tela inicial → **Entrar**.
2. Login → **Entrar como Jovem**.
3. Área do jovem → **Ver oportunidades**.
4. Escolher uma vaga → **Ver vaga**.
5. Detalhes → **Candidatar-se**.
6. Abrir **Minhas candidaturas**.
7. Demonstrar **Meu perfil** e **Sair**.

Fluxo alternativo: tela inicial → **Sou Empresa** → **Entrar como Empresa** → publicar vaga → minhas vagas → candidatos.

## Versionamento e GitHub

O repositório deve ser criado no GitHub com um nome relacionado ao projeto. Depois, associe o remoto e publique os commits:

```powershell
git remote add origin https://github.com/SEU_USUARIO/evolui.git
git push -u origin master
```

O link acima é um modelo e deve ser substituído pelo endereço real do repositório da equipe.

## Próximas etapas

- conectar cadastro e login ao banco existente;
- persistir perfis, vagas e candidaturas;
- validar credenciais e permissões;
- permitir edição e fechamento de vagas;
- configurar o link definitivo do GitHub.

## Equipe

- Julia
- Ana
