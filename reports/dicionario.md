
# Dicionário de Dados

Este documento descreve os campos de cada um dos arquivos CSV gerados a partir dos dados das escolas.

## `escolas.csv`

Arquivo principal com os dados cadastrais de cada escola.

| Coluna         | Descrição                                           |
|----------------|-------------------------------------------------------|
| `CIE`            | Código de Identificação da Escola (Chave Primária)    |
| `Nome`           | Nome da escola                                        |
| `Tipo`           | Tipo de escola (ex: EEI - INDIGENA)                   |
| `Diretoria`      | Diretoria de Ensino a que a escola pertence           |
| `Endereço`       | Endereço completo da escola                           |
| `Bairro`         | Bairro da escola                                      |
| `Município`      | Município da escola                                   |
| `Telefone`       | Telefone da escola                                    |
| `Email`          | Email de contato da escola                            |
| `Total_Alunos`   | Número total de alunos matriculados                   |
| `Total_Turmas`   | Número total de turmas                                |

## `gestores.csv`

Tabela com os gestores de cada escola.

| Coluna       | Descrição                                           |
|--------------|-------------------------------------------------------|
| `CIE_Escola`   | Código de Identificação da Escola (Chave Estrangeira) |
| `Função`       | Cargo do gestor (ex: Diretor, Vice-Diretor)         |
| `Nome`         | Nome do gestor                                        |

## `docentes.csv`

Tabela com os docentes (professores) de cada escola.

| Coluna       | Descrição                                           |
|--------------|-------------------------------------------------------|
| `CIE_Escola`   | Código de Identificação da Escola (Chave Estrangeira) |
| `Função`       | Cargo do docente (ex: Professor)                    |
| `Disciplina`   | Disciplina lecionada pelo docente                     |
| `Módulo`       | Módulo de ensino (ex: Anos Iniciais, Anos Finais)   |
| `Nome`         | Nome do docente                                       |

## `infraestrutura.csv`

Detalhes sobre a infraestrutura física das escolas.

| Coluna         | Descrição                                           |
|----------------|-------------------------------------------------------|
| `CIE_Escola`     | Código de Identificação da Escola (Chave Estrangeira) |
| `Ambiente`       | Categoria do ambiente (ex: Salas de Aula, Cozinha)    |
| `Item`           | Item específico da infraestrutura (ex: Sala de Leitura) |
| `Quantidade`     | Quantidade do item                                    |

## `equipamentos.csv`

Equipamentos disponíveis em cada escola.

| Coluna         | Descrição                                           |
|----------------|-------------------------------------------------------|
| `CIE_Escola`     | Código de Identificação da Escola (Chave Estrangeira) |
| `Grupo`          | Grupo do equipamento (ex: Alunos, Gerais)           |
| `Equipamento`    | Nome do equipamento                                   |
| `Quantidade`     | Quantidade do equipamento                             |

## `servicos.csv`

Serviços oferecidos pelas escolas.

| Coluna       | Descrição                                           |
|--------------|-------------------------------------------------------|
| `CIE_Escola`   | Código de Identificação da Escola (Chave Estrangeira) |
| `Serviço`      | Nome do serviço (ex: Alimentação escolar)           |
| `Detalhe`      | Detalhes sobre o serviço                              |

## `vacinacao.csv`

Dados sobre a vacinação contra a COVID-19 na comunidade escolar.

| Coluna       | Descrição                                           |
|--------------|-------------------------------------------------------|
| `CIE_Escola`   | Código de Identificação da Escola (Chave Estrangeira) |
| `Grupo`        | Grupo demográfico (ex: ADOLESCENTES, SERVIDORES)    |
| `Status`       | Tipo de dado (ex: Vacina COVID-19)                  |
| `Valor`        | Valor do dado (percentual ou número absoluto)       |

## `alunos_faixa_etaria.csv`

Distribuição de alunos por faixa etária e nível de ensino.

| Coluna             | Descrição                                           |
|--------------------|-------------------------------------------------------|
| `CIE_Escola`         | Código de Identificação da Escola (Chave Estrangeira) |
| `Faixa_Etaria`       | Faixa etária dos alunos                               |
| `Anos_Iniciais`      | Quantidade de alunos nos Anos Iniciais                |
| `Anos_Finais`        | Quantidade de alunos nos Anos Finais                  |
| `EJA_Anos_Iniciais`  | Quantidade de alunos na EJA - Anos Iniciais          |
| `EJA_Anos_Finais`    | Quantidade de alunos na EJA - Anos Finais            |
| `EJA_Ensino_Medio`   | Quantidade de alunos na EJA - Ensino Médio           |
| `Ensino_Infantil`    | Quantidade de alunos no Ensino Infantil             |

## `turmas_por_tipo.csv`

Distribuição de turmas por nível de ensino.

| Coluna             | Descrição                                           |
|--------------------|-------------------------------------------------------|
| `CIE_Escola`         | Código de Identificação da Escola (Chave Estrangeira) |
| `Anos_Iniciais`      | Quantidade de turmas nos Anos Iniciais                |
| `Anos_Finais`        | Quantidade de turmas nos Anos Finais                  |
| `EJA_Anos_Iniciais`  | Quantidade de turmas na EJA - Anos Iniciais          |
| `EJA_Anos_Finais`    | Quantidade de turmas na EJA - Anos Finais            |
| `EJA_Ensino_Medio`   | Quantidade de turmas na EJA - Ensino Médio           |
| `Ensino_Infantil`    | Quantidade de turmas no Ensino Infantil             |
