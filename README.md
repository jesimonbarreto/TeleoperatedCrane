## Guindaste Virtual Teleoperado

### Universidade Federal de Minas Gerais - Escola de Engenharia
#### Professor Dr. Gustavo Medeiros Freitas
#### Executado pelos alunos:
##### - Ariel  Domingues
##### - Gustavo Ferreira
##### - Henrique de Paula
##### - Jesimon Barreto
##### - Lucas Bispo


![execu](https://github.com/jesimonbarreto/TeleoperatedCrane/blob/master/image_ex.png?raw=true)



#### Objetivos da disciplina:
1. Participar de todas as etapas de um projeto funcional
não trivial, indo deste a concepção da ideia até a entrega
do produto final
2. Contribuir para o processo de documentação,
implementação e gerência do projeto
3. Colocar em prática os conceitos aprendidos ao longo do
curso no projeto de sistemas complexos
4. Metodologia Maker: baseada no conceito Faça Você
Mesmo!

#### Tópicos abordados
1. Desenvolvimento de projetos envolvendo sistemas de alto
nível de complexidade
2. Análise e gestão de requisitos
3. Mapas conceituais
4. Máquinas de estado
5. Gestão ágil de projetos – SCRUM
6. Técnicas de elaboração de relatório
7. Técnicas de apresentação
8. Impacto da tecnologia na sociedade


• Descrição:
✓ O operador dever comandar um guindaste de forma remota via GUI
✓ Num cenário virtual realista, o guindaste deverá ser comandado para pegar uma moeda de 50c apoiada numa plataforma com posição e altura conhecidas, e depositá-la numa plataforma com posição conhecida e altura desconhecida
✓ Teloperação remota via internet:
• Telemetria básica
• Realimetação avançada

Guindaste virtual teleoperado

• Especificação da tarefa: comandar um guindaste para retirar uma carga de uma
plataforma de carga, e transportá-la até uma plataforma de descarga
• Modo de operação do guindaste: teleoperado de forma remota por meio de
GUI
• Carga a ser movimentada: moeda virtual de 50 centavos (dimensões reais)
• Moeda deve ser movimentada sobre um círculo de raio de 300mm
• A base do guindaste virtual deve caber dentro de um círculo de raio de 250mm
• Plataformas de carga e descarga com raio de 40mm, posicionada sobre um
círculo de raio de 300mm
• A posição inicial da moeda é conhecida, apoiada sobre uma plataforma de
carga de 7mm de altura
• A posição das plataforma de descarga é conhecida. Porém, o operador remoto
desconhece a altura da plataforma, variando entre 85 a 220mm

Sequência de tarefas:
1. Guindaste pega a moeda na plataforma de 7mm de altura – posição e altura
conhecidas
2. Guindaste gira até se posicionar sobre a plataforma de descarga – posição conhecida
3. Guindaste deposita a moeda na plataforma de descarga – altura desconhecida

Requisitos e especificações da Interface Gráfica de Usuário (GUI):
• Composta por barras de rolagem e/ou campos de texto para enviar comandos:
• ângulo da lança, altura da ferramenta, estado da ferramenta
• Permite visualizar o status atual do guindaste:
• ângulo da lança, altura da ferramenta, estado da ferramenta
• Apresenta informações adicionais de realimentação para facilitar a teleoperação:
• carga acoplada? distância da ferramenta até a plataforma de descarga? vídeo?
• Linguagens obrigatórias de desenvolvimento: C, C++ ou Python
• Representação gráfica simples do guindaste:

Requisitos e especificações do protocolo de comunicação:
• Comunicação entre GUI e guindaste virtual pela internet
• A GUI deverá ser executada no computador de um integrante da equipe, e o
simulador do guindaste deverá rodar num computador de outro integrante da
equipe
• Troca de mensagens simples de dados - comando da GUI para o guindaste, e
telemetria do guindaste para a GUI:
• ângulo da lança, altura da ferramenta, estado da ferramenta
• Envio de informações adicionais do guindaste para a GUI de forma a facilitar a
teleoperação:
• carga acoplada? distância da ferramenta até a plataforma de descarga? vídeo?

Desafio adaptado: guindaste virtual teleoperado
Requisitos e especificações do Simulador do Guindaste:
• Composto por um ou mais programas. Linguagem de desenvolvimento livre.
• Representação geométrica realista:
• guindaste: base, torre, lança, ferramenta (eletroímã)
• cenário de operação: moeda, plataformas de carga e descarga
• Ilustrar o giro da lança, variação de altura da ferramenta, acionamento do
eletroímã (via indicação visual, e.g. LED), acoplamento e desacoplamento da
moeda
• Tentar emular movimentos contínuos, “sem teletransporte”, considerando
velocidades máximas de motores
• Possibilitar alterar de forma “online” a altura da plataforma de descarga, que
será desconhecida para o operador remoto
• Recebe comandos e envia dados de telemetria para a GUI:
• ângulo da lança, altura da ferramenta, estado da ferramenta
• Envia informações adicionais para a GUI de forma a facilitar a teleoperação:
• carga acoplada? distância da ferramenta até a plataforma de descarga? vídeo?

Ferramentas para análise e modelagem de sistemas e gestão ágil de projeto
• Análise de requisitos
• Mapas conceituais
• Máquinas de estado
• SCRUM para a gestão ágil do projeto

####  Dependências
- PyQt 5
- Coppeliasim
- Windows 7,8,8.1,10

#### Para executar o projeto
- Instale as dependências (PyQT)
- Baixe todos os códigos da pasta "GUI" no host cliente
- Baixe o arquivo da pasta "Crane" no host servidor
- Edite o arquivo de conexão da pasta "GUI" para o ip do servidor (host que irá executar a simulação)
- Abra o coppelia, carregue o arquivo da pasta "Crane" e inicie a simulação
- Execute o arquivo gui.py da pasta "GUI"
- Após abrir a gui clique em conectar, depois em ligar e os controles serão liberados.

#### Apresentação do Projeto
- 00:00 Apresentação da Parte Teórica
- 40:25 Demonstração do Sistema


[![Apresentação Projeto](https://image.flaticon.com/icons/png/512/174/174883.png)](https://www.youtube.com/watch?v=YCgK2n9LpuQ&feature=youtu.be)
