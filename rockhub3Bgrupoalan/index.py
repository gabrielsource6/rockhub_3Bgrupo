# Este é o sistema criado para testar sua sabedoria em relação a cada banda, entre 55-58 questões cada.
# As próximas atualizações vai ser a opção de jogar novamente ao terminar o quiz e um temporizador para tornar as questões mais desafiadoras.
import random
import os
import unicodedata

Questoes = {
    "Imagine Dragons": [
        {
            "pergunta": "Em que cidade a banda Imagine Dragons foi formada?",
            "correta": "Las Vegas",
            "erradas": ["Seattle", "Los Angeles", "Phoenix"]
        },
        {
            "pergunta": "Em que ano o Imagine Dragons foi criado?",
            "correta": "2008",
            "erradas": ["2006", "2009", "2011"]
        },
        {
            "pergunta": "Quem é o vocalista principal da banda?",
            "correta": "Dan Reynolds",
            "erradas": ["Ben McKee", "Wayne Sermon", "Daniel Platzman"]
        },
        {
            "pergunta": "Quais são os nomes dos integrantes mais conhecidos da formação clássica da banda?",
            "correta": "Dan Reynolds, Wayne Sermon, Ben McKee e Daniel Platzman",
            "erradas": [
                "Dan Reynolds, Andrew Tolman, Ben McKee e Ryan Walker",
                "Wayne Sermon, Ben McKee, Alex Da Kid e Dan Reynolds",
                "Dan Reynolds, Dave Lemke, Andrew Beck e Wayne Sermon"
            ]
        },
        {
            "pergunta": "Qual foi o álbum de estreia de estúdio do Imagine Dragons?",
            "correta": "Night Visions",
            "erradas": ["Smoke + Mirrors", "Origins", "Evolve"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Night Visions?",
            "correta": "2012",
            "erradas": ["2010", "2011", "2013"]
        },
        {
            "pergunta": "Qual música do álbum Night Visions se tornou um sucesso mundial e ajudou a lançar a banda ao estrelato?",
            "correta": "Radioactive",
            "erradas": ["Believer", "Natural", "Thunder"]
        },
        {
            "pergunta": "Qual canção do Imagine Dragons foi usada como tema promocional do jogo League of Legends em 2014?",
            "correta": "Warriors",
            "erradas": ["Enemy", "Radioactive", "Natural"]
        },
        {
            "pergunta": "Qual álbum contém as músicas Believer, Thunder e Whatever It Takes?",
            "correta": "Evolve",
            "erradas": ["Origins", "Night Visions", "Smoke + Mirrors"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Evolve?",
            "correta": "2017",
            "erradas": ["2015", "2016", "2018"]
        },
        {
            "pergunta": "Qual música da banda possui a frase 'First things first' logo no início?",
            "correta": "Believer",
            "erradas": ["Thunder", "Natural", "Demons"]
        },
        {
            "pergunta": "Qual integrante da banda toca bateria?",
            "correta": "Daniel Platzman",
            "erradas": ["Ben McKee", "Wayne Sermon", "Dan Reynolds"]
        },
        {
            "pergunta": "Qual foi o segundo álbum de estúdio do Imagine Dragons?",
            "correta": "Smoke + Mirrors",
            "erradas": ["Origins", "Evolve", "Mercury – Act 1"]
        },
        {
            "pergunta": "Qual música do álbum Smoke + Mirrors alcançou grande popularidade e fala sobre sonhos e fama?",
            "correta": "Dream",
            "erradas": ["Shots", "Gold", "Hopeless Opus"]
        },
        {
            "pergunta": "Qual é o gênero musical predominante associado ao Imagine Dragons?",
            "correta": "Pop rock",
            "erradas": ["Heavy metal", "Country", "Jazz"]
        },
        {
            "pergunta": "Qual música da banda se tornou famosa pela frase 'I'm waking up, I feel it in my bones'?",
            "correta": "Radioactive",
            "erradas": ["Demons", "Believer", "Thunder"]
        },
        {
            "pergunta": "Qual álbum foi lançado pela banda em 2021 após um intervalo de alguns anos?",
            "correta": "Mercury – Act 1",
            "erradas": ["Origins", "Evolve", "Night Visions"]
        },
        {
            "pergunta": "Quem é o principal compositor e letrista do grupo?",
            "correta": "Dan Reynolds",
            "erradas": ["Ben McKee", "Wayne Sermon", "Daniel Platzman"]
        },
        {
            "pergunta": "Qual música da banda foi utilizada na trilha sonora da série Arcane?",
            "correta": "Enemy",
            "erradas": ["Warriors", "Natural", "Believer"]
        },
        {
            "pergunta": "O Imagine Dragons já venceu algum prêmio Grammy?",
            "correta": "Sim",
            "erradas": ["Não", "Apenas foi indicado", "Venceu apenas prêmios da MTV"]
        },
        {
            "pergunta": "Qual música da banda fala sobre enfrentar a dor para se tornar mais forte?",
            "correta": "Believer",
            "erradas": ["Thunder", "Demons", "On Top of the World"]
        },
        {
            "pergunta": "Qual álbum foi dividido em duas partes chamadas Mercury – Act 1 e Mercury – Act 2?",
            "correta": "Mercury",
            "erradas": ["Origins", "Evolve", "Night Visions"]
        },
        {
            "pergunta": "Qual música do Imagine Dragons tem o refrão 'You made me a believer'?",
            "correta": "Believer",
            "erradas": ["Thunder", "Natural", "Bones"]
        },
        {
            "pergunta": "Em qual estado dos Estados Unidos a banda foi formada?",
            "correta": "Nevada",
            "erradas": ["Califórnia", "Utah", "Arizona"]
        },
        {
            "pergunta": "Qual música da banda é conhecida pelo refrão repetitivo da palavra 'Thunder'?",
            "correta": "Thunder",
            "erradas": ["Believer", "Enemy", "Natural"]
        },
        {
            "pergunta": "Qual foi o primeiro grande sucesso internacional do Imagine Dragons?",
            "correta": "It's Time",
            "erradas": ["Believer", "Thunder", "Enemy"]
        },
        {
            "pergunta": "Qual música do álbum Origins fala sobre amizade e apoio emocional?",
            "correta": "Burn Out",
            "erradas": ["Natural", "Machine", "Zero"]
        },
        {
            "pergunta": "Qual álbum contém a música Natural?",
            "correta": "Origins",
            "erradas": ["Evolve", "Night Visions", "Smoke + Mirrors"]
        },
        {
            "pergunta": "Qual música da banda foi criada para o filme Passengers (2016)?",
            "correta": "Levitate",
            "erradas": ["Monster", "Battle Cry", "Bones"]
        },
        {
            "pergunta": "Qual é o nome do álbum lançado em 2022 que completou o projeto Mercury?",
            "correta": "Mercury – Act 2",
            "erradas": ["Mercury Returns", "Mercury Complete", "Mercury Finale"]
        },
        {
            "pergunta": "Qual era o nome da banda de Dan Reynolds antes da formação definitiva do Imagine Dragons?",
            "correta": "Não havia uma banda conhecida com nome oficial anterior ao Imagine Dragons",
            "erradas": [
                "The Dragons",
                "Egyptian",
                "Neon Trees"
            ]
        },
        {
            "pergunta": "Em qual universidade Dan Reynolds conheceu Andrew Tolman?",
            "correta": "Brigham Young University",
            "erradas": [
                "Harvard University",
                "University of Nevada",
                "Berklee College of Music"
            ]
        },
        {
            "pergunta": "Qual integrante deixou a banda em 2023 após mais de uma década como baterista?",
            "correta": "Daniel Platzman",
            "erradas": [
                "Ben McKee",
                "Wayne Sermon",
                "Dan Reynolds"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro EP lançado pelo Imagine Dragons?",
            "correta": "Imagine Dragons EP",
            "erradas": [
                "Hell and Silence",
                "It's Time",
                "Continued Silence"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado o EP Hell and Silence?",
            "correta": "2010",
            "erradas": [
                "2008",
                "2009",
                "2011"
            ]
        },
        {
            "pergunta": "Qual produtor musical trabalhou com a banda em grande parte do álbum Night Visions?",
            "correta": "Alex da Kid",
            "erradas": [
                "Rick Rubin",
                "Max Martin",
                "Jack Antonoff"
            ]
        },
        {
            "pergunta": "Qual música do álbum Smoke + Mirrors abre oficialmente o disco?",
            "correta": "Shots",
            "erradas": [
                "Gold",
                "Dream",
                "Smoke and Mirrors"
            ]
        },
        {
            "pergunta": "Qual canção de Night Visions foi originalmente lançada em EPs anteriores antes do álbum?",
            "correta": "It's Time",
            "erradas": [
                "Radioactive",
                "Demons",
                "Bleeding Out"
            ]
        },
        {
            "pergunta": "Qual música do Imagine Dragons ultrapassou a marca de bilhões de reproduções no Spotify antes das demais?",
            "correta": "Believer",
            "erradas": [
                "Thunder",
                "Enemy",
                "Demons"
            ]
        },
        {
            "pergunta": "Qual álbum da banda alcançou o primeiro lugar na Billboard 200 em 2015?",
            "correta": "Smoke + Mirrors",
            "erradas": [
                "Night Visions",
                "Evolve",
                "Origins"
            ]
        },
        {
            "pergunta": "Qual integrante é conhecido por tocar guitarra principal na banda?",
            "correta": "Wayne Sermon",
            "erradas": [
                "Ben McKee",
                "Dan Reynolds",
                "Daniel Platzman"
            ]
        },
        {
            "pergunta": "Qual integrante é responsável pelo baixo?",
            "correta": "Ben McKee",
            "erradas": [
                "Wayne Sermon",
                "Dan Reynolds",
                "Daniel Platzman"
            ]
        },
        {
            "pergunta": "Em qual cerimônia do Grammy o Imagine Dragons venceu o prêmio de Melhor Performance de Rock?",
            "correta": "Grammy Awards de 2014",
            "erradas": [
                "Grammy Awards de 2012",
                "Grammy Awards de 2016",
                "Grammy Awards de 2018"
            ]
        },
        {
            "pergunta": "Com qual rapper a banda colaborou em uma apresentação de Radioactive no Grammy de 2014?",
            "correta": "Kendrick Lamar",
            "erradas": [
                "Drake",
                "Eminem",
                "J. Cole"
            ]
        },
        {
            "pergunta": "Qual música foi lançada como single principal do álbum Origins?",
            "correta": "Natural",
            "erradas": [
                "Machine",
                "Zero",
                "Bad Liar"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Dull Knives?",
            "correta": "Mercury – Act 1",
            "erradas": [
                "Origins",
                "Evolve",
                "Smoke + Mirrors"
            ]
        },
        {
            "pergunta": "Qual música de Mercury – Act 1 aborda diretamente problemas de saúde mental e perda?",
            "correta": "Wrecked",
            "erradas": [
                "Dull Knives",
                "Follow You",
                "Monday"
            ]
        },
        {
            "pergunta": "Quem produziu os álbuns da série Mercury?",
            "correta": "Rick Rubin",
            "erradas": [
                "Alex da Kid",
                "Max Martin",
                "Butch Vig"
            ]
        },
        {
            "pergunta": "Qual música da banda foi criada para a trilha sonora do filme Transformers: Age of Extinction?",
            "correta": "Battle Cry",
            "erradas": [
                "Warriors",
                "Monster",
                "Levitate"
            ]
        },
        {
            "pergunta": "Em qual ano foi lançado o álbum Origins?",
            "correta": "2018",
            "erradas": [
                "2016",
                "2017",
                "2019"
            ]
        },
        {
            "pergunta": "Qual canção do Imagine Dragons possui o verso 'Welcome to the new age'?",
            "correta": "Radioactive",
            "erradas": [
                "Believer",
                "Natural",
                "Thunder"
            ]
        },
        {
            "pergunta": "Qual integrante estudou na Berklee College of Music?",
            "correta": "Ben McKee",
            "erradas": [
                "Dan Reynolds",
                "Wayne Sermon",
                "Daniel Platzman"
            ]
        },
        {
            "pergunta": "Qual EP contém a música It's Time antes do lançamento de Night Visions?",
            "correta": "It's Time",
            "erradas": [
                "Imagine Dragons EP",
                "Hell and Silence",
                "Mercury EP"
            ]
        },
        {
            "pergunta": "Qual álbum do Imagine Dragons inclui a faixa Shots?",
            "correta": "Smoke + Mirrors",
            "erradas": [
                "Night Visions",
                "Origins",
                "Evolve"
            ]
        },
        {
            "pergunta": "Qual é o significado frequentemente atribuído ao nome 'Imagine Dragons' pelos fãs?",
            "correta": "É um anagrama cujo significado real nunca foi revelado pela banda",
            "erradas": [
                "Refere-se a um dragão mitológico criado por Dan Reynolds",
                "É uma homenagem a um videogame antigo",
                "Significa 'Dragões da Imaginação' em latim"
            ]
        }
    ],

"Metallica": [
        {
            "pergunta": "Em que ano o Metallica foi formado?",
            "correta": "1981",
            "erradas": ["1979", "1983", "1985"]
        },
        {
            "pergunta": "Em qual cidade o Metallica foi fundado?",
            "correta": "Los Angeles",
            "erradas": ["San Francisco", "Seattle", "Chicago"]
        },
        {
            "pergunta": "Quem são os dois membros fundadores mais conhecidos da banda?",
            "correta": "James Hetfield e Lars Ulrich",
            "erradas": [
                "James Hetfield e Kirk Hammett",
                "Lars Ulrich e Cliff Burton",
                "Kirk Hammett e Cliff Burton"
            ]
        },
        {
            "pergunta": "Qual é o nome do vocalista principal do Metallica?",
            "correta": "James Hetfield",
            "erradas": ["Lars Ulrich", "Kirk Hammett", "Robert Trujillo"]
        },
        {
            "pergunta": "Qual integrante é o principal baterista da banda desde sua fundação?",
            "correta": "Lars Ulrich",
            "erradas": ["James Hetfield", "Kirk Hammett", "Robert Trujillo"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia do Metallica?",
            "correta": "Kill 'Em All",
            "erradas": ["Ride the Lightning", "Master of Puppets", "Metallica"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Kill 'Em All?",
            "correta": "1983",
            "erradas": ["1981", "1984", "1986"]
        },
        {
            "pergunta": "Qual álbum contém a música Master of Puppets?",
            "correta": "Master of Puppets",
            "erradas": ["Ride the Lightning", "Kill 'Em All", "Metallica"]
        },
        {
            "pergunta": "Qual baixista do Metallica morreu em um acidente de ônibus durante uma turnê?",
            "correta": "Cliff Burton",
            "erradas": ["Jason Newsted", "Robert Trujillo", "Ron McGovney"]
        },
        {
            "pergunta": "Em que país ocorreu o acidente que vitimou Cliff Burton?",
            "correta": "Suécia",
            "erradas": ["Noruega", "Alemanha", "Finlândia"]
        },
        {
            "pergunta": "Quem substituiu Cliff Burton após sua morte?",
            "correta": "Jason Newsted",
            "erradas": ["Robert Trujillo", "Kirk Hammett", "Ron McGovney"]
        },
        {
            "pergunta": "Qual álbum do Metallica foi lançado em 1986 e é considerado um dos maiores álbuns de metal da história?",
            "correta": "Master of Puppets",
            "erradas": ["Ride the Lightning", "Kill 'Em All", "...And Justice for All"]
        },
        {
            "pergunta": "Qual música do Metallica ficou famosa por começar com um solo de baixo tocado por Cliff Burton?",
            "correta": "For Whom the Bell Tolls",
            "erradas": ["Orion", "Anesthesia (Pulling Teeth)", "Battery"]
        },
        {
            "pergunta": "Qual álbum é conhecido pelos fãs como 'The Black Album'?",
            "correta": "Metallica",
            "erradas": ["Load", "Reload", "Garage Inc."]
        },
        {
            "pergunta": "Em que ano foi lançado o The Black Album?",
            "correta": "1991",
            "erradas": ["1989", "1990", "1993"]
        },
        {
            "pergunta": "Qual música do Metallica contém o refrão 'Exit light, enter night'?",
            "correta": "Enter Sandman",
            "erradas": ["Nothing Else Matters", "Sad But True", "The Unforgiven"]
        },
        {
            "pergunta": "Qual guitarrista entrou para a banda em 1983 e permanece até hoje?",
            "correta": "Kirk Hammett",
            "erradas": ["Dave Mustaine", "Jason Newsted", "Robert Trujillo"]
        },
        {
            "pergunta": "Qual música instrumental famosa está presente no álbum Ride the Lightning?",
            "correta": "The Call of Ktulu",
            "erradas": ["Orion", "Suicide & Redemption", "To Live Is to Die"]
        },
        {
            "pergunta": "Qual álbum contém as músicas One e Harvester of Sorrow?",
            "correta": "...And Justice for All",
            "erradas": ["Master of Puppets", "Ride the Lightning", "Metallica"]
        },
        {
            "pergunta": "Qual canção do Metallica foi inspirada no romance Johnny Got His Gun?",
            "correta": "One",
            "erradas": ["Fade to Black", "The Unforgiven", "Welcome Home (Sanitarium)"]
        },
        {
            "pergunta": "Qual integrante atualmente toca baixo no Metallica?",
            "correta": "Robert Trujillo",
            "erradas": ["Jason Newsted", "Ron McGovney", "Cliff Burton"]
        },
        {
            "pergunta": "Qual álbum foi lançado após um intervalo de oito anos entre trabalhos de estúdio?",
            "correta": "Death Magnetic",
            "erradas": ["Hardwired... to Self-Destruct", "Reload", "72 Seasons"]
        },
        {
            "pergunta": "Em que ano foi lançado Death Magnetic?",
            "correta": "2008",
            "erradas": ["2006", "2007", "2009"]
        },
        {
            "pergunta": "Qual álbum gerou controvérsia devido à sua produção sonora e uso limitado de solos de guitarra?",
            "correta": "St. Anger",
            "erradas": ["Load", "Death Magnetic", "Reload"]
        },
        {
            "pergunta": "Qual produtor ficou famoso por trabalhar nos primeiros álbuns clássicos do Metallica?",
            "correta": "Flemming Rasmussen",
            "erradas": ["Bob Rock", "Rick Rubin", "Greg Fidelman"]
        },
        {
            "pergunta": "Qual música do Black Album começa com a frase 'Say your prayers, little one'?",
            "correta": "Enter Sandman",
            "erradas": ["Sad But True", "Nothing Else Matters", "The Unforgiven"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Fuel?",
            "correta": "Reload",
            "erradas": ["Load", "Garage Inc.", "St. Anger"]
        },
        {
            "pergunta": "Qual documentário mostrou os conflitos internos da banda durante a produção de um álbum?",
            "correta": "Some Kind of Monster",
            "erradas": ["Metallica Through the Never", "A Year and a Half in the Life of Metallica", "Classic Albums"]
        },
        {
            "pergunta": "Qual música do Metallica é frequentemente tocada em eventos esportivos por causa de sua introdução marcante?",
            "correta": "Enter Sandman",
            "erradas": ["Fuel", "Master of Puppets", "Nothing Else Matters"]
        },
        {
            "pergunta": "Qual álbum de 2023 marcou o retorno da banda com material inédito após Hardwired... to Self-Destruct?",
            "correta": "72 Seasons",
            "erradas": ["Death Magnetic", "Reload", "St. Anger"]
        },
        {
            "pergunta": "Qual foi o nome do guitarrista original do Metallica antes da entrada de Kirk Hammett?",
            "correta": "Dave Mustaine",
            "erradas": ["Ron McGovney", "Jason Newsted", "Cliff Burton"]
        },
        {
            "pergunta": "Em qual revista Lars Ulrich publicou o anúncio que levou à formação da banda?",
            "correta": "The Recycler",
            "erradas": ["Rolling Stone", "Kerrang!", "Metal Hammer"]
        },
        {
            "pergunta": "Qual foi a primeira música original gravada pelo Metallica?",
            "correta": "Hit the Lights",
            "erradas": ["Seek & Destroy", "Whiplash", "Motorbreath"]
        },
        {
            "pergunta": "Em que coletânea essa primeira gravação foi lançada?",
            "correta": "Metal Massacre",
            "erradas": ["Garage Days Re-Revisited", "Kill 'Em All", "Metallica Collection"]
        },
        {
            "pergunta": "Qual foi o último álbum de estúdio com Cliff Burton?",
            "correta": "Master of Puppets",
            "erradas": ["Ride the Lightning", "...And Justice for All", "Kill 'Em All"]
        },
        {
            "pergunta": "Qual música de Master of Puppets possui mais de 8 minutos e fala sobre dependência química?",
            "correta": "Master of Puppets",
            "erradas": ["Battery", "Orion", "Disposable Heroes"]
        },
        {
            "pergunta": "Qual álbum marcou a estreia de Jason Newsted como baixista do Metallica?",
            "correta": "...And Justice for All",
            "erradas": ["Master of Puppets", "Metallica", "Ride the Lightning"]
        },
        {
            "pergunta": "Qual música abre o álbum ...And Justice for All?",
            "correta": "Blackened",
            "erradas": ["One", "Eye of the Beholder", "Harvester of Sorrow"]
        },
        {
            "pergunta": "Qual faixa-título de ...And Justice for All ultrapassa 9 minutos de duração?",
            "correta": "...And Justice for All",
            "erradas": ["One", "Blackened", "To Live Is to Die"]
        },
        {
            "pergunta": "Qual engenheiro de som produziu o álbum The Black Album ao lado de Bob Rock?",
            "correta": "Randy Staub",
            "erradas": ["Greg Fidelman", "Flemming Rasmussen", "Mike Clink"]
        },
        {
            "pergunta": "Qual música do Black Album foi inspirada no livro Of Mice and Men, de John Steinbeck?",
            "correta": "Of Wolf and Man",
            "erradas": ["The Unforgiven", "Sad But True", "Holier Than Thou"]
        },
        {
            "pergunta": "Qual álbum foi lançado em conjunto com uma apresentação da Orquestra Sinfônica de San Francisco em 1999?",
            "correta": "S&M",
            "erradas": ["Garage Inc.", "Reload", "Live Shit: Binge & Purge"]
        },
        {
            "pergunta": "Quem regeu a orquestra no projeto S&M?",
            "correta": "Michael Kamen",
            "erradas": ["John Williams", "Hans Zimmer", "James Newton Howard"]
        },
        {
            "pergunta": "Qual música inédita foi criada especificamente para o álbum S&M?",
            "correta": "No Leaf Clover",
            "erradas": ["Hero of the Day", "Fuel", "The Memory Remains"]
        },
        {
            "pergunta": "Qual álbum de estúdio foi o primeiro a contar com Bob Rock tocando baixo em algumas faixas?",
            "correta": "St. Anger",
            "erradas": ["Reload", "Death Magnetic", "72 Seasons"]
        },
        {
            "pergunta": "Em que ano Robert Trujillo entrou oficialmente para a banda?",
            "correta": "2003",
            "erradas": ["2001", "2002", "2004"]
        },
        {
            "pergunta": "De qual banda Robert Trujillo veio antes de ingressar no Metallica?",
            "correta": "Suicidal Tendencies",
            "erradas": ["Megadeth", "Slayer", "Anthrax"]
        },
        {
            "pergunta": "Qual música de Death Magnetic foi a primeira faixa divulgada do álbum?",
            "correta": "The Day That Never Comes",
            "erradas": ["All Nightmare Long", "Broken, Beat & Scarred", "Cyanide"]
        },
        {
            "pergunta": "Qual álbum contém a música Spit Out the Bone?",
            "correta": "Hardwired... to Self-Destruct",
            "erradas": ["Death Magnetic", "72 Seasons", "St. Anger"]
        },
        {
            "pergunta": "Qual foi o primeiro single lançado de 72 Seasons?",
            "correta": "Lux Æterna",
            "erradas": ["72 Seasons", "If Darkness Had a Son", "Screaming Suicide"]
        },
        {
            "pergunta": "Qual música do Metallica foi utilizada nos créditos finais do filme Jungle Cruise?",
            "correta": "Nothing Else Matters",
            "erradas": ["Enter Sandman", "The Unforgiven", "Fuel"]
        },
        {
            "pergunta": "Qual canção do álbum Load fala sobre o incêndio que destruiu a casa de James Hetfield?",
            "correta": "Mama Said",
            "erradas": ["Until It Sleeps", "King Nothing", "Hero of the Day"]
        },
        {
            "pergunta": "Qual membro do Metallica sofreu queimaduras graves durante um show em 1992?",
            "correta": "James Hetfield",
            "erradas": ["Lars Ulrich", "Kirk Hammett", "Jason Newsted"]
        },
        {
            "pergunta": "Qual álbum possui a faixa instrumental Suicide & Redemption?",
            "correta": "Death Magnetic",
            "erradas": ["Hardwired... to Self-Destruct", "St. Anger", "72 Seasons"]
        },
        {
            "pergunta": "Qual é o nome completo do álbum lançado em parceria com Lou Reed?",
            "correta": "Lulu",
            "erradas": ["Transformer", "Berlin", "Metal Machine Music"]
        }
    ],

"Gorillaz": [
        {
            "pergunta": "Em que ano o Gorillaz foi criado?",
            "correta": "1998",
            "erradas": ["1996", "2000", "2002"]
        },
        {
            "pergunta": "Quem são os dois criadores do projeto Gorillaz?",
            "correta": "Damon Albarn e Jamie Hewlett",
            "erradas": [
                "Damon Albarn e Graham Coxon",
                "Jamie Hewlett e Noel Gallagher",
                "Damon Albarn e Paul Simonon"
            ]
        },
        {
            "pergunta": "Qual músico é responsável pela maior parte das composições do Gorillaz?",
            "correta": "Damon Albarn",
            "erradas": ["Jamie Hewlett", "Murdoc Niccals", "2-D"]
        },
        {
            "pergunta": "Qual artista desenhou os personagens da banda?",
            "correta": "Jamie Hewlett",
            "erradas": ["Alan Moore", "Banksy", "Damon Albarn"]
        },
        {
            "pergunta": "Qual é o nome do vocalista fictício do Gorillaz?",
            "correta": "2-D",
            "erradas": ["Murdoc", "Russel", "Ace"]
        },
        {
            "pergunta": "Qual personagem fictício toca baixo na banda?",
            "correta": "Murdoc Niccals",
            "erradas": ["2-D", "Russel Hobbs", "Ace"]
        },
        {
            "pergunta": "Quem é a guitarrista fictícia do Gorillaz?",
            "correta": "Noodle",
            "erradas": ["Paula Cracker", "Del", "Ace"]
        },
        {
            "pergunta": "Qual personagem é o baterista da banda?",
            "correta": "Russel Hobbs",
            "erradas": ["Murdoc Niccals", "2-D", "Noodle"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia do Gorillaz?",
            "correta": "Gorillaz",
            "erradas": ["Demon Days", "Plastic Beach", "Humanz"]
        },
        {
            "pergunta": "Em que ano esse álbum foi lançado?",
            "correta": "2001",
            "erradas": ["1999", "2000", "2002"]
        },
        {
            "pergunta": "Qual música do álbum de estreia se tornou um dos maiores sucessos da banda?",
            "correta": "Clint Eastwood",
            "erradas": ["Feel Good Inc.", "On Melancholy Hill", "Tranz"]
        },
        {
            "pergunta": "Qual álbum contém a música Feel Good Inc.?",
            "correta": "Demon Days",
            "erradas": ["Plastic Beach", "Humanz", "The Now Now"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Demon Days?",
            "correta": "2005",
            "erradas": ["2003", "2004", "2006"]
        },
        {
            "pergunta": "Qual rapper participa de Feel Good Inc.?",
            "correta": "De La Soul",
            "erradas": ["Snoop Dogg", "MF DOOM", "Mos Def"]
        },
        {
            "pergunta": "Qual música do Gorillaz contém a frase 'Windmill, windmill for the land'?",
            "correta": "Feel Good Inc.",
            "erradas": ["Clint Eastwood", "DARE", "Dirty Harry"]
        },
        {
            "pergunta": "Qual álbum conceitual da banda foi lançado em 2010?",
            "correta": "Plastic Beach",
            "erradas": ["Demon Days", "Humanz", "The Now Now"]
        },
        {
            "pergunta": "Qual música famosa abre o álbum Plastic Beach?",
            "correta": "Orchestral Intro",
            "erradas": ["Welcome to the World of the Plastic Beach", "Stylo", "On Melancholy Hill"]
        },
        {
            "pergunta": "Qual lendário cantor da banda The Clash colaborou em Plastic Beach?",
            "correta": "Mick Jones",
            "erradas": ["Joe Strummer", "Paul Simonon", "Topper Headon"]
        },
        {
            "pergunta": "Qual álbum foi lançado gratuitamente online no Natal de 2010?",
            "correta": "The Fall",
            "erradas": ["Plastic Beach", "D-Sides", "Humanz"]
        },
        {
            "pergunta": "Qual álbum marcou o retorno da banda após vários anos de pausa e foi lançado em 2017?",
            "correta": "Humanz",
            "erradas": ["The Now Now", "Plastic Beach", "Cracker Island"]
        },
        {
            "pergunta": "Qual música do álbum Humanz conta com a participação de Popcaan?",
            "correta": "Saturnz Barz",
            "erradas": ["Andromeda", "Ascension", "Busted and Blue"]
        },
        {
            "pergunta": "Qual álbum lançado em 2018 inclui a faixa Tranz?",
            "correta": "The Now Now",
            "erradas": ["Humanz", "Cracker Island", "Plastic Beach"]
        },
        {
            "pergunta": "Qual música do Gorillaz foi usada em comerciais e videogames, ajudando a popularizar a banda no início dos anos 2000?",
            "correta": "19-2000",
            "erradas": ["Clint Eastwood", "DARE", "Stylo"]
        },
        {
            "pergunta": "Qual personagem fictício do Gorillaz possui cabelo azul?",
            "correta": "2-D",
            "erradas": ["Murdoc Niccals", "Russel Hobbs", "Ace"]
        },
        {
            "pergunta": "Qual é o nome da ilha artificial onde se passa grande parte da história de Plastic Beach?",
            "correta": "Plastic Beach",
            "erradas": ["Point Nemo", "Kong Island", "Trash Island"]
        },
        {
            "pergunta": "Qual álbum da banda foi lançado em 2020 durante o projeto Song Machine?",
            "correta": "Song Machine, Season One: Strange Timez",
            "erradas": ["The Fall", "Cracker Island", "Humanz"]
        },
        {
            "pergunta": "Qual cantor participou da música The Pink Phantom?",
            "correta": "Elton John",
            "erradas": ["Paul McCartney", "Sting", "Morrissey"]
        },
        {
            "pergunta": "Qual integrante fictício do Gorillaz é conhecido por seus olhos completamente brancos?",
            "correta": "2-D",
            "erradas": ["Murdoc Niccals", "Russel Hobbs", "Noodle"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Cracker Island?",
            "correta": "Cracker Island",
            "erradas": ["Song Machine", "The Now Now", "Humanz"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Cracker Island?",
            "correta": "2023",
            "erradas": ["2021", "2022", "2024"]
        },
        {
            "pergunta": "Qual álbum inclui a faixa Empire Ants?",
            "correta": "Plastic Beach",
            "erradas": [
                "Demon Days",
                "Humanz",
                "The Now Now"
            ]
        },
        {
            "pergunta": "Qual cantora participa de Empire Ants?",
            "correta": "Yukimi Nagano",
            "erradas": [
                "Little Simz",
                "St. Vincent",
                "Moonchild Sanelly"
            ]
        },
        {
            "pergunta": "Qual personagem fictício do Gorillaz é especialista em artes marciais?",
            "correta": "Noodle",
            "erradas": [
                "Murdoc Niccals",
                "2-D",
                "Russel Hobbs"
            ]
        },
        {
            "pergunta": "Em qual fase da história Murdoc foi preso e substituído por Ace?",
            "correta": "The Now Now",
            "erradas": [
                "Plastic Beach",
                "Humanz",
                "Cracker Island"
            ]
        },
        {
            "pergunta": "De qual desenho animado veio Ace?",
            "correta": "The Powerpuff Girls",
            "erradas": [
                "Dexter's Laboratory",
                "Johnny Bravo",
                "Samurai Jack"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Souk Eye?",
            "correta": "The Now Now",
            "erradas": [
                "Humanz",
                "Plastic Beach",
                "Cracker Island"
            ]
        },
        {
            "pergunta": "Qual música de Demon Days encerra o álbum?",
            "correta": "Demon Days",
            "erradas": [
                "Don't Get Lost in Heaven",
                "DARE",
                "Fire Coming Out of the Monkey's Head"
            ]
        },
        {
            "pergunta": "Qual produtor foi uma figura importante na produção de Demon Days e Plastic Beach?",
            "correta": "Danger Mouse",
            "erradas": [
                "Rick Rubin",
                "Mark Ronson",
                "Nigel Godrich"
            ]
        },
        {
            "pergunta": "Qual personagem fictício foi criado por Jamie Hewlett inspirado em uma combinação de músicos britânicos e personagens de quadrinhos?",
            "correta": "2-D",
            "erradas": [
                "Murdoc Niccals",
                "Russel Hobbs",
                "Noodle"
            ]
        },
        {
            "pergunta": "Qual música do Gorillaz conta com a participação de Lou Reed?",
            "correta": "Some Kind of Nature",
            "erradas": [
                "Stylo",
                "Empire Ants",
                "On Melancholy Hill"
            ]
        },
        {
            "pergunta": "Qual foi o nome do estúdio virtual criado para a banda na internet durante os primeiros anos?",
            "correta": "Kong Studios",
            "erradas": [
                "Plastic Beach Studios",
                "Gorillaz HQ",
                "Zombie Hip Hop Manor"
            ]
        },
        {
            "pergunta": "Em qual álbum aparece a faixa Momentary Bliss?",
            "correta": "Song Machine, Season One: Strange Timez",
            "erradas": [
                "Humanz",
                "The Now Now",
                "Cracker Island"
            ]
        },
        {
            "pergunta": "Qual personagem do Gorillaz fala japonês fluentemente além de inglês?",
            "correta": "Noodle",
            "erradas": [
                "2-D",
                "Murdoc Niccals",
                "Russel Hobbs"
            ]
        }
    ],

"Blur": [
        {
            "pergunta": "Em que ano a banda Blur foi formada?",
            "correta": "1988",
            "erradas": ["1986", "1990", "1992"]
        },
        {
            "pergunta": "Em qual cidade da Inglaterra a banda teve origem?",
            "correta": "Londres",
            "erradas": ["Manchester", "Liverpool", "Birmingham"]
        },
        {
            "pergunta": "Quem é o vocalista principal do Blur?",
            "correta": "Damon Albarn",
            "erradas": ["Graham Coxon", "Alex James", "Dave Rowntree"]
        },
        {
            "pergunta": "Qual integrante do Blur também é cofundador do Gorillaz?",
            "correta": "Damon Albarn",
            "erradas": ["Graham Coxon", "Alex James", "Dave Rowntree"]
        },
        {
            "pergunta": "Quem é o guitarrista principal da banda?",
            "correta": "Graham Coxon",
            "erradas": ["Alex James", "Dave Rowntree", "Damon Albarn"]
        },
        {
            "pergunta": "Qual integrante toca baixo?",
            "correta": "Alex James",
            "erradas": ["Graham Coxon", "Dave Rowntree", "Damon Albarn"]
        },
        {
            "pergunta": "Quem é o baterista do Blur?",
            "correta": "Dave Rowntree",
            "erradas": ["Alex James", "Graham Coxon", "Damon Albarn"]
        },
        {
            "pergunta": "Qual foi o nome original da banda antes de se chamar Blur?",
            "correta": "Seymour",
            "erradas": ["The Circus", "The Magic Whip", "Modern Life"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia do Blur?",
            "correta": "Leisure",
            "erradas": ["Parklife", "Modern Life Is Rubbish", "Blur"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Leisure?",
            "correta": "1991",
            "erradas": ["1989", "1990", "1992"]
        },
        {
            "pergunta": "Qual música foi o maior sucesso do álbum Leisure?",
            "correta": "There's No Other Way",
            "erradas": ["She's So High", "Bang", "Sing"]
        },
        {
            "pergunta": "Qual álbum ajudou a consolidar o movimento Britpop em 1993?",
            "correta": "Modern Life Is Rubbish",
            "erradas": ["Leisure", "Parklife", "Blur"]
        },
        {
            "pergunta": "Qual música abre o álbum Parklife?",
            "correta": "Girls & Boys",
            "erradas": ["Parklife", "Tracy Jacks", "End of a Century"]
        },
        {
            "pergunta": "Em que ano foi lançado Parklife?",
            "correta": "1994",
            "erradas": ["1992", "1993", "1995"]
        },
        {
            "pergunta": "Qual ator britânico narra partes da faixa Parklife?",
            "correta": "Phil Daniels",
            "erradas": ["Hugh Grant", "Rowan Atkinson", "Stephen Fry"]
        },
        {
            "pergunta": "Qual álbum contém a música Girls & Boys?",
            "correta": "Parklife",
            "erradas": ["Leisure", "The Great Escape", "Blur"]
        },
        {
            "pergunta": "Qual álbum contém a faixa The Universal?",
            "correta": "The Great Escape",
            "erradas": ["Parklife", "13", "Blur"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum The Great Escape?",
            "correta": "1995",
            "erradas": ["1993", "1994", "1996"]
        },
        {
            "pergunta": "Qual banda rivalizou com o Blur durante o auge da Britpop?",
            "correta": "Oasis",
            "erradas": ["Pulp", "Suede", "Radiohead"]
        },
        {
            "pergunta": "Qual single do Blur venceu a famosa disputa de vendas contra o single Roll With It da Oasis em 1995?",
            "correta": "Country House",
            "erradas": ["The Universal", "Parklife", "Girls & Boys"]
        },
        {
            "pergunta": "Qual álbum marcou uma mudança para um som mais alternativo e influenciado pelo rock americano?",
            "correta": "Blur",
            "erradas": ["Parklife", "The Great Escape", "Leisure"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Blur?",
            "correta": "1997",
            "erradas": ["1995", "1996", "1998"]
        },
        {
            "pergunta": "Qual música do álbum Blur se tornou um sucesso internacional, especialmente nos Estados Unidos?",
            "correta": "Song 2",
            "erradas": ["Beetlebum", "On Your Own", "M.O.R."]
        },
        {
            "pergunta": "Qual álbum contém a faixa Coffee & TV?",
            "correta": "13",
            "erradas": ["Blur", "Think Tank", "Parklife"]
        },
        {
            "pergunta": "Qual integrante canta os vocais principais em Coffee & TV?",
            "correta": "Graham Coxon",
            "erradas": ["Damon Albarn", "Alex James", "Dave Rowntree"]
        },
        {
            "pergunta": "Em que ano Graham Coxon deixou temporariamente a banda?",
            "correta": "2002",
            "erradas": ["2000", "2001", "2003"]
        },
        {
            "pergunta": "Qual álbum foi gravado sem a participação completa de Graham Coxon?",
            "correta": "Think Tank",
            "erradas": ["13", "Blur", "The Magic Whip"]
        },
        {
            "pergunta": "Em que ano foi lançado Think Tank?",
            "correta": "2003",
            "erradas": ["2001", "2002", "2004"]
        },
        {
            "pergunta": "Qual música do Blur ficou famosa por seu refrão 'Woo-hoo!'?",
            "correta": "Song 2",
            "erradas": ["Girls & Boys", "Coffee & TV", "Parklife"]
        },
        {
            "pergunta": "Qual álbum marcou o retorno da banda com material inédito em 2015?",
            "correta": "The Magic Whip",
            "erradas": ["Think Tank", "13", "The Ballad of Darren"]
        },
        {
            "pergunta": "Em que ano foi lançado The Magic Whip?",
            "correta": "2015",
            "erradas": ["2013", "2014", "2016"]
        },
        {
            "pergunta": "Em qual cidade boa parte de The Magic Whip foi escrita?",
            "correta": "Hong Kong",
            "erradas": ["Tóquio", "Londres", "Xangai"]
        },
        {
            "pergunta": "Qual álbum de estúdio foi lançado pela banda em 2023?",
            "correta": "The Ballad of Darren",
            "erradas": ["The Magic Whip", "Think Tank", "13"]
        },
        {
            "pergunta": "Qual música abre o álbum The Ballad of Darren?",
            "correta": "The Ballad",
            "erradas": ["St. Charles Square", "Barbaric", "Russian Strings"]
        },
        {
            "pergunta": "Quantos integrantes compõem a formação clássica do Blur?",
            "correta": "4",
            "erradas": ["3", "5", "6"]
        },
        {
            "pergunta": "Em qual instituição Damon Albarn e Graham Coxon estudaram juntos antes da formação do Blur?",
            "correta": "Stanway Comprehensive School",
            "erradas": [
                "Goldsmiths University",
                "Colchester Royal Grammar School",
                "University of Essex"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro single lançado pela banda ainda sob o nome Seymour?",
            "correta": "She's So High",
            "erradas": [
                "Bang",
                "There's No Other Way",
                "Sing"
            ]
        },
        {
            "pergunta": "Qual gravadora sugeriu que a banda mudasse seu nome de Seymour para Blur?",
            "correta": "Food Records",
            "erradas": [
                "EMI",
                "Parlophone",
                "Virgin Records"
            ]
        },
        {
            "pergunta": "Qual música encerra o álbum Modern Life Is Rubbish?",
            "correta": "Resigned",
            "erradas": [
                "For Tomorrow",
                "Sunday Sunday",
                "Blue Jeans"
            ]
        },
        {
            "pergunta": "Qual álbum do Blur foi gravado parcialmente na Islândia?",
            "correta": "13",
            "erradas": [
                "Blur",
                "Parklife",
                "Think Tank"
            ]
        },
        {
            "pergunta": "Qual produtor trabalhou com a banda nos álbuns Parklife, The Great Escape e Blur?",
            "correta": "Stephen Street",
            "erradas": [
                "William Orbit",
                "Ben Hillier",
                "Nigel Godrich"
            ]
        },
        {
            "pergunta": "Qual música de 13 foi inspirada pelo fim do relacionamento de Damon Albarn com Justine Frischmann?",
            "correta": "No Distance Left to Run",
            "erradas": [
                "Coffee & TV",
                "Bugman",
                "Tender"
            ]
        },
        {
            "pergunta": "Quem produziu o álbum 13?",
            "correta": "William Orbit",
            "erradas": [
                "Stephen Street",
                "Danger Mouse",
                "Ben Hillier"
            ]
        },
        {
            "pergunta": "Qual integrante do Blur lançou o álbum solo Happiness in Magazines em 2004?",
            "correta": "Graham Coxon",
            "erradas": [
                "Damon Albarn",
                "Alex James",
                "Dave Rowntree"
            ]
        },
        {
            "pergunta": "Qual foi o último álbum de estúdio do Blur antes do hiato que antecedeu The Magic Whip?",
            "correta": "Think Tank",
            "erradas": [
                "13",
                "Blur",
                "Parklife"
            ]
        },
        {
            "pergunta": "Qual música de Think Tank foi gravada com forte influência da música do norte da África?",
            "correta": "Out of Time",
            "erradas": [
                "Crazy Beat",
                "Good Song",
                "Gene by Gene"
            ]
        },
        {
            "pergunta": "Em que país ocorreram várias das sessões de gravação de Think Tank?",
            "correta": "Marrocos",
            "erradas": [
                "Egito",
                "Argélia",
                "Tunísia"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Battery in Your Leg?",
            "correta": "Think Tank",
            "erradas": [
                "13",
                "Blur",
                "The Magic Whip"
            ]
        },
        {
            "pergunta": "Qual integrante toca os vocais principais em You're So Great?",
            "correta": "Graham Coxon",
            "erradas": [
                "Damon Albarn",
                "Alex James",
                "Dave Rowntree"
            ]
        },
        {
            "pergunta": "Qual música do Blur foi usada como tema do videogame FIFA: Road to World Cup 98?",
            "correta": "Song 2",
            "erradas": [
                "Beetlebum",
                "Girls & Boys",
                "Coffee & TV"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Beetlebum?",
            "correta": "Blur",
            "erradas": [
                "13",
                "Parklife",
                "The Great Escape"
            ]
        },
        {
            "pergunta": "Qual músico do Blur chegou a trabalhar como jornalista e escritor após o auge da banda?",
            "correta": "Alex James",
            "erradas": [
                "Damon Albarn",
                "Graham Coxon",
                "Dave Rowntree"
            ]
        },
        {
            "pergunta": "Em qual ano ocorreu a grande reunião da banda que levou aos shows no Hyde Park?",
            "correta": "2009",
            "erradas": [
                "2007",
                "2008",
                "2010"
            ]
        },
        {
            "pergunta": "Qual álbum foi criado a partir de gravações recuperadas de sessões em Hong Kong?",
            "correta": "The Magic Whip",
            "erradas": [
                "Think Tank",
                "13",
                "The Ballad of Darren"
            ]
        },
        {
            "pergunta": "Qual é o nome do documentário de 2010 que acompanha a história da banda e sua reunião?",
            "correta": "No Distance Left to Run",
            "erradas": [
                "Blur: The Reunion",
                "Parklife Revisited",
                "The Magic Whip Documentary"
            ]
        }
    ],

"Linkin Park": [
        {
            "pergunta": "Em que ano o Linkin Park foi formado?",
            "correta": "1996",
            "erradas": ["1994", "1998", "2000"]
        },
        {
            "pergunta": "Em qual estado dos Estados Unidos a banda foi criada?",
            "correta": "Califórnia",
            "erradas": ["Texas", "Nevada", "Arizona"]
        },
        {
            "pergunta": "Qual era o nome original da banda antes de se chamar Linkin Park?",
            "correta": "Xero",
            "erradas": ["Hybrid Theory", "Lincoln Park", "Grey Daze"]
        },
        {
            "pergunta": "Quem foi o vocalista principal do Linkin Park até 2017?",
            "correta": "Chester Bennington",
            "erradas": ["Mike Shinoda", "Mark Wakefield", "Joe Hahn"]
        },
        {
            "pergunta": "Qual integrante era responsável pelos vocais, rap e produção musical?",
            "correta": "Mike Shinoda",
            "erradas": ["Brad Delson", "Rob Bourdon", "Dave Farrell"]
        },
        {
            "pergunta": "Quem é o guitarrista principal da banda?",
            "correta": "Brad Delson",
            "erradas": ["Dave Farrell", "Joe Hahn", "Mike Shinoda"]
        },
        {
            "pergunta": "Qual integrante toca baixo?",
            "correta": "Dave Farrell",
            "erradas": ["Brad Delson", "Rob Bourdon", "Joe Hahn"]
        },
        {
            "pergunta": "Quem é o baterista da formação clássica do Linkin Park?",
            "correta": "Rob Bourdon",
            "erradas": ["Brad Delson", "Dave Farrell", "Joe Hahn"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia da banda?",
            "correta": "Hybrid Theory",
            "erradas": ["Meteora", "Minutes to Midnight", "Reanimation"]
        },
        {
            "pergunta": "Em que ano foi lançado Hybrid Theory?",
            "correta": "2000",
            "erradas": ["1999", "2001", "2002"]
        },
        {
            "pergunta": "Qual música de Hybrid Theory começa com o verso 'It starts with one...'?",
            "correta": "In the End",
            "erradas": ["Crawling", "Papercut", "One Step Closer"]
        },
        {
            "pergunta": "Qual música de Hybrid Theory foi o primeiro single oficial do álbum?",
            "correta": "One Step Closer",
            "erradas": ["In the End", "Crawling", "Papercut"]
        },
        {
            "pergunta": "Qual álbum contém as músicas Numb, Somewhere I Belong e Faint?",
            "correta": "Meteora",
            "erradas": ["Hybrid Theory", "Minutes to Midnight", "Living Things"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Meteora?",
            "correta": "2003",
            "erradas": ["2001", "2002", "2004"]
        },
        {
            "pergunta": "Qual DJ da banda era conhecido por seus scratches e efeitos sonoros?",
            "correta": "Joe Hahn",
            "erradas": ["Mike Shinoda", "Brad Delson", "Dave Farrell"]
        },
        {
            "pergunta": "Qual integrante era responsável pelos samples e programação?",
            "correta": "Joe Hahn",
            "erradas": ["Mike Shinoda", "Brad Delson", "Dave Farrell"]
        },
        {
            "pergunta": "Qual álbum conceitual foi lançado em 2007?",
            "correta": "Minutes to Midnight",
            "erradas": ["Meteora", "A Thousand Suns", "Living Things"]
        },
        {
            "pergunta": "Qual música de Minutes to Midnight fala sobre consequências da guerra nuclear?",
            "correta": "The Little Things Give You Away",
            "erradas": ["Bleed It Out", "Shadow of the Day", "Leave Out All the Rest"]
        },
        {
            "pergunta": "Qual álbum contém a faixa The Catalyst?",
            "correta": "A Thousand Suns",
            "erradas": ["Minutes to Midnight", "Living Things", "The Hunting Party"]
        },
        {
            "pergunta": "Em que ano foi lançado A Thousand Suns?",
            "correta": "2010",
            "erradas": ["2008", "2009", "2011"]
        },
        {
            "pergunta": "Qual música do Linkin Park foi criada para o filme Transformers de 2007?",
            "correta": "What I've Done",
            "erradas": ["New Divide", "Iridescent", "Burn It Down"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Burn It Down?",
            "correta": "Living Things",
            "erradas": ["A Thousand Suns", "Meteora", "The Hunting Party"]
        },
        {
            "pergunta": "Em que ano foi lançado Living Things?",
            "correta": "2012",
            "erradas": ["2010", "2011", "2013"]
        },
        {
            "pergunta": "Qual álbum trouxe um som mais voltado ao rock pesado em 2014?",
            "correta": "The Hunting Party",
            "erradas": ["Living Things", "One More Light", "A Thousand Suns"]
        },
        {
            "pergunta": "Qual música abre o álbum The Hunting Party?",
            "correta": "Keys to the Kingdom",
            "erradas": ["Guilty All the Same", "Wastelands", "Rebellion"]
        },
        {
            "pergunta": "Qual foi o último álbum lançado com Chester Bennington em vida?",
            "correta": "One More Light",
            "erradas": ["The Hunting Party", "Living Things", "Meteora"]
        },
        {
            "pergunta": "Em que ano foi lançado One More Light?",
            "correta": "2017",
            "erradas": ["2015", "2016", "2018"]
        },
        {
            "pergunta": "Qual música do Linkin Park se tornou um tributo a Chester após sua morte?",
            "correta": "One More Light",
            "erradas": ["Numb", "In the End", "Heavy"]
        },
        {
            "pergunta": "Quem assumiu os vocais principais na nova fase da banda iniciada em 2024?",
            "correta": "Emily Armstrong",
            "erradas": ["Amy Lee", "Lzzy Hale", "Hayley Williams"]
        },
        {
            "pergunta": "Qual álbum marcou o retorno do Linkin Park com a nova vocalista?",
            "correta": "From Zero",
            "erradas": ["One More Light", "Papercuts", "The Emptiness Machine"]
        },
        {
            "pergunta": "Qual era o nome da banda imediatamente antes de ela adotar o nome Linkin Park?",
            "correta": "Hybrid Theory",
            "erradas": ["Xero", "Lincoln Park", "Grey Daze"]
        },
        {
            "pergunta": "Por que a banda precisou mudar o nome de Hybrid Theory para Linkin Park?",
            "correta": "Porque o nome Hybrid Theory já apresentava problemas legais e de marca registrada",
            "erradas": [
                "Porque a gravadora exigiu um nome mais curto",
                "Porque Chester Bennington não gostava do nome",
                "Porque o público confundia a banda com outra banda local"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro EP lançado pela banda sob o nome Hybrid Theory?",
            "correta": "Hybrid Theory EP",
            "erradas": ["Xero Demo Tape", "Reanimation", "Underground 1.0"]
        },
        {
            "pergunta": "Em que ano foi lançado o EP Hybrid Theory EP?",
            "correta": "1999",
            "erradas": ["1997", "1998", "2000"]
        },
        {
            "pergunta": "Qual vocalista do Xero foi substituído por Chester Bennington?",
            "correta": "Mark Wakefield",
            "erradas": ["Mike Shinoda", "Scott Weiland", "Chris Cornell"]
        },
        {
            "pergunta": "Qual escola de arte Mike Shinoda frequentou?",
            "correta": "ArtCenter College of Design",
            "erradas": [
                "California Institute of the Arts",
                "Otis College of Art and Design",
                "School of Visual Arts"
            ]
        },
        {
            "pergunta": "Qual música de Hybrid Theory não foi lançada como single, mas se tornou uma das favoritas dos fãs?",
            "correta": "A Place for My Head",
            "erradas": [
                "Crawling",
                "In the End",
                "One Step Closer"
            ]
        },
        {
            "pergunta": "Qual faixa instrumental de Meteora ganhou um Grammy?",
            "correta": "Session",
            "erradas": [
                "Foreword",
                "Wake",
                "Cure for the Itch"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro álbum do Linkin Park a estrear em 1º lugar na Billboard 200?",
            "correta": "Meteora",
            "erradas": [
                "Hybrid Theory",
                "Minutes to Midnight",
                "A Thousand Suns"
            ]
        },
        {
            "pergunta": "Qual música de Meteora contém a frase 'I can't feel the way I did before'?",
            "correta": "Numb",
            "erradas": [
                "Faint",
                "Somewhere I Belong",
                "Breaking the Habit"
            ]
        },
        {
            "pergunta": "Qual produtor trabalhou em praticamente todos os álbuns clássicos do Linkin Park?",
            "correta": "Rick Rubin",
            "erradas": [
                "Danger Mouse",
                "Butch Vig",
                "Rob Cavallo"
            ]
        },
        {
            "pergunta": "Qual música encerra o álbum Minutes to Midnight?",
            "correta": "The Little Things Give You Away",
            "erradas": [
                "Shadow of the Day",
                "Valentine's Day",
                "In Pieces"
            ]
        },
        {
            "pergunta": "Qual faixa de A Thousand Suns contém um discurso de Martin Luther King Jr.?",
            "correta": "Wisdom, Justice, and Love",
            "erradas": [
                "The Catalyst",
                "When They Come for Me",
                "Waiting for the End"
            ]
        },
        {
            "pergunta": "Qual música de A Thousand Suns foi o primeiro single do álbum?",
            "correta": "The Catalyst",
            "erradas": [
                "Waiting for the End",
                "Burning in the Skies",
                "Iridescent"
            ]
        },
        {
            "pergunta": "Qual integrante dirigiu os videoclipes de Numb, Breaking the Habit e From the Inside?",
            "correta": "Joe Hahn",
            "erradas": [
                "Mike Shinoda",
                "Brad Delson",
                "Rob Bourdon"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Lost in the Echo?",
            "correta": "Living Things",
            "erradas": [
                "A Thousand Suns",
                "The Hunting Party",
                "Meteora"
            ]
        },
        {
            "pergunta": "Qual música de Living Things foi usada no jogo Medal of Honor: Warfighter?",
            "correta": "Castle of Glass",
            "erradas": [
                "Burn It Down",
                "Lost in the Echo",
                "Powerless"
            ]
        },
        {
            "pergunta": "Qual músico do System of a Down participou de Rebellion?",
            "correta": "Daron Malakian",
            "erradas": [
                "Serj Tankian",
                "Shavo Odadjian",
                "John Dolmayan"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Final Masquerade?",
            "correta": "The Hunting Party",
            "erradas": [
                "Living Things",
                "One More Light",
                "A Thousand Suns"
            ]
        },
        {
            "pergunta": "Qual música do álbum One More Light foi dedicada a uma amiga de Chester e da banda que havia falecido?",
            "correta": "One More Light",
            "erradas": [
                "Heavy",
                "Sharp Edges",
                "Nobody Can Save Me"
            ]
        },
        {
            "pergunta": "Em que cidade Chester Bennington nasceu?",
            "correta": "Phoenix",
            "erradas": [
                "Los Angeles",
                "Las Vegas",
                "San Diego"
            ]
        },
        {
            "pergunta": "Qual banda tinha Chester Bennington como vocalista antes de ele entrar no Linkin Park?",
            "correta": "Grey Daze",
            "erradas": [
                "Stone Temple Pilots",
                "Dead by Sunrise",
                "Hybrid Theory"
            ]
        },
        {
            "pergunta": "Qual álbum de estúdio do Linkin Park vendeu mais cópias mundialmente?",
            "correta": "Hybrid Theory",
            "erradas": [
                "Meteora",
                "Minutes to Midnight",
                "A Thousand Suns"
            ]
        },
        {
            "pergunta": "Qual música inédita das sessões de Meteora foi lançada oficialmente em 2023?",
            "correta": "Lost",
            "erradas": [
                "Fighting Myself",
                "More the Victim",
                "Healing Foot"
            ]
        },
        {
            "pergunta": "Qual integrante clássico do Linkin Park não participou do retorno da banda em 2024?",
            "correta": "Rob Bourdon",
            "erradas": [
                "Mike Shinoda",
                "Joe Hahn",
                "Dave Farrell"
            ]
        }
    ],

"Nirvana": [
        {
            "pergunta": "Em que ano o Nirvana foi formado?",
            "correta": "1987",
            "erradas": ["1985", "1989", "1991"]
        },
        {
            "pergunta": "Em qual estado dos Estados Unidos a banda surgiu?",
            "correta": "Washington",
            "erradas": ["Oregon", "Califórnia", "Montana"]
        },
        {
            "pergunta": "Quem foi o fundador e principal compositor do Nirvana?",
            "correta": "Kurt Cobain",
            "erradas": ["Krist Novoselic", "Dave Grohl", "Pat Smear"]
        },
        {
            "pergunta": "Qual integrante tocava baixo na formação clássica da banda?",
            "correta": "Krist Novoselic",
            "erradas": ["Dave Grohl", "Chad Channing", "Pat Smear"]
        },
        {
            "pergunta": "Quem foi o baterista que integrou a banda a partir de 1990?",
            "correta": "Dave Grohl",
            "erradas": ["Chad Channing", "Dale Crover", "Dan Peters"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia do Nirvana?",
            "correta": "Bleach",
            "erradas": ["Nevermind", "In Utero", "Incesticide"]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Bleach?",
            "correta": "1989",
            "erradas": ["1988", "1990", "1991"]
        },
        {
            "pergunta": "Qual gravadora lançou Bleach originalmente?",
            "correta": "Sub Pop",
            "erradas": ["Geffen Records", "DGC Records", "EMI"]
        },
        {
            "pergunta": "Qual álbum tornou o Nirvana um fenômeno mundial?",
            "correta": "Nevermind",
            "erradas": ["Bleach", "In Utero", "Incesticide"]
        },
        {
            "pergunta": "Em que ano foi lançado Nevermind?",
            "correta": "1991",
            "erradas": ["1990", "1992", "1993"]
        },
        {
            "pergunta": "Qual música abre o álbum Nevermind?",
            "correta": "Smells Like Teen Spirit",
            "erradas": ["In Bloom", "Come as You Are", "Breed"]
        },
        {
            "pergunta": "Qual canção do Nirvana começa com a famosa frase 'Load up on guns, bring your friends'?",
            "correta": "Smells Like Teen Spirit",
            "erradas": ["Come as You Are", "Lithium", "Drain You"]
        },
        {
            "pergunta": "Quem produziu o álbum Nevermind?",
            "correta": "Butch Vig",
            "erradas": ["Steve Albini", "Jack Endino", "Scott Litt"]
        },
        {
            "pergunta": "Qual música do Nirvana alcançou enorme sucesso na MTV em 1991?",
            "correta": "Smells Like Teen Spirit",
            "erradas": ["Lithium", "In Bloom", "Polly"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Heart-Shaped Box?",
            "correta": "In Utero",
            "erradas": ["Nevermind", "Bleach", "Incesticide"]
        },
        {
            "pergunta": "Em que ano foi lançado In Utero?",
            "correta": "1993",
            "erradas": ["1991", "1992", "1994"]
        },
        {
            "pergunta": "Qual produtor foi escolhido para produzir In Utero?",
            "correta": "Steve Albini",
            "erradas": ["Butch Vig", "Jack Endino", "Rick Rubin"]
        },
        {
            "pergunta": "Qual música de In Utero foi o primeiro single do álbum?",
            "correta": "Heart-Shaped Box",
            "erradas": ["Rape Me", "All Apologies", "Pennyroyal Tea"]
        },
        {
            "pergunta": "Qual canção do Nirvana possui o refrão 'I'm so happy 'cause today I found my friends'?",
            "correta": "Lithium",
            "erradas": ["Polly", "Drain You", "Breed"]
        },
        {
            "pergunta": "Qual álbum ao vivo foi gravado para o programa MTV Unplugged?",
            "correta": "MTV Unplugged in New York",
            "erradas": ["From the Muddy Banks of the Wishkah", "Live at Reading", "Incesticide"]
        },
        {
            "pergunta": "Em que ano ocorreu a apresentação do MTV Unplugged in New York?",
            "correta": "1993",
            "erradas": ["1992", "1994", "1995"]
        },
        {
            "pergunta": "Qual música dos Meat Puppets foi tocada durante esse show?",
            "correta": "Lake of Fire",
            "erradas": ["Plateau", "Oh, Me", "Backwater"]
        },
        {
            "pergunta": "Qual integrante do Nirvana era casado com Courtney Love?",
            "correta": "Kurt Cobain",
            "erradas": ["Krist Novoselic", "Dave Grohl", "Pat Smear"]
        },
        {
            "pergunta": "Qual foi o último álbum de estúdio lançado pelo Nirvana?",
            "correta": "In Utero",
            "erradas": ["Nevermind", "Incesticide", "MTV Unplugged in New York"]
        },
        {
            "pergunta": "Qual música encerra o álbum Nevermind (desconsiderando faixas escondidas)?",
            "correta": "Something in the Way",
            "erradas": ["Endless, Nameless", "On a Plain", "Stay Away"]
        },
        {
            "pergunta": "Em qual cidade Kurt Cobain nasceu?",
            "correta": "Aberdeen",
            "erradas": ["Seattle", "Tacoma", "Olympia"]
        },
        {
            "pergunta": "Qual álbum contém a música Come as You Are?",
            "correta": "Nevermind",
            "erradas": ["In Utero", "Bleach", "Incesticide"]
        },
        {
            "pergunta": "Qual música do Nirvana foi inspirada em uma frase escrita por Kathleen Hanna sobre Kurt Cobain?",
            "correta": "Smells Like Teen Spirit",
            "erradas": ["Lithium", "About a Girl", "All Apologies"]
        },
        {
            "pergunta": "Qual compilação lançada em 2002 trouxe a música inédita You Know You're Right?",
            "correta": "Nirvana",
            "erradas": ["With the Lights Out", "Incesticide", "Sliver: The Best of the Box"]
        },
        {
            "pergunta": "Quantos álbuns de estúdio o Nirvana lançou durante sua existência?",
            "correta": "3",
            "erradas": ["2", "4", "5"]
        },
        {
            "pergunta": "Qual era o nome da banda de Kurt Cobain e Krist Novoselic antes da adoção definitiva do nome Nirvana?",
            "correta": "Skid Row",
            "erradas": ["Fecal Matter", "Bliss", "Ted Ed Fred"]
        },
        {
            "pergunta": "Quem foi o baterista do álbum Bleach?",
            "correta": "Chad Channing",
            "erradas": ["Dave Grohl", "Dale Crover", "Dan Peters"]
        },
        {
            "pergunta": "Qual foi o primeiro single lançado pelo Nirvana?",
            "correta": "Love Buzz",
            "erradas": ["About a Girl", "Blew", "Smells Like Teen Spirit"]
        },
        {
            "pergunta": "Em qual cidade foi gravado grande parte do álbum Nevermind?",
            "correta": "Los Angeles",
            "erradas": ["Seattle", "Chicago", "Nova York"]
        },
        {
            "pergunta": "Qual música de Nevermind foi inspirada por uma experiência de Kurt Cobain em uma festa?",
            "correta": "Drain You",
            "erradas": ["Polly", "Breed", "On a Plain"]
        },
        {
            "pergunta": "Qual integrante da banda Sonic Youth ajudou o Nirvana a conseguir maior visibilidade na cena musical?",
            "correta": "Kim Gordon",
            "erradas": ["Thurston Moore", "Lee Ranaldo", "Steve Shelley"]
        },
        {
            "pergunta": "Qual música abre o álbum In Utero?",
            "correta": "Serve the Servants",
            "erradas": ["Scentless Apprentice", "Heart-Shaped Box", "Rape Me"]
        },
        {
            "pergunta": "Qual faixa de In Utero foi escrita em homenagem à filha de Kurt Cobain?",
            "correta": "Frances Farmer Will Have Her Revenge on Seattle",
            "erradas": ["Pennyroyal Tea", "All Apologies", "Tourette's"]
        },
        {
            "pergunta": "Qual música de In Utero contém o verso 'Love myself better than you'?",
            "correta": "Serve the Servants",
            "erradas": ["Rape Me", "Milk It", "Very Ape"]
        },
        {
            "pergunta": "Qual foi o último show completo realizado pelo Nirvana?",
            "correta": "Munique, Alemanha, em 1º de março de 1994",
            "erradas": [
                "Berlim, Alemanha",
                "Paris, França",
                "Seattle, Estados Unidos"
            ]
        },
        {
            "pergunta": "Em qual país ocorreu esse último show?",
            "correta": "Alemanha",
            "erradas": ["França", "Estados Unidos", "Áustria"]
        },
        {
            "pergunta": "Qual música inédita gravada em janeiro de 1994 foi lançada oficialmente apenas em 2002?",
            "correta": "You Know You're Right",
            "erradas": ["Do Re Mi", "Old Age", "Verse Chorus Verse"]
        },
        {
            "pergunta": "Qual álbum ao vivo do Nirvana foi lançado em 1996 e documenta um show de 1994?",
            "correta": "From the Muddy Banks of the Wishkah",
            "erradas": [
                "MTV Unplugged in New York",
                "Live at Reading",
                "With the Lights Out"
            ]
        },
        {
            "pergunta": "Qual produtor remixou algumas faixas de In Utero a pedido da gravadora?",
            "correta": "Scott Litt",
            "erradas": [
                "Butch Vig",
                "Steve Albini",
                "Jack Endino"
            ]
        },
        {
            "pergunta": "Qual música do Nirvana foi originalmente escrita para o álbum Nevermind, mas acabou ficando em In Utero?",
            "correta": "Rape Me",
            "erradas": [
                "Heart-Shaped Box",
                "Milk It",
                "Dumb"
            ]
        },
        {
            "pergunta": "Qual era o nome da casa de shows de Seattle frequentemente associada ao início da carreira do Nirvana?",
            "correta": "The Crocodile Cafe",
            "erradas": [
                "The Paramount Theatre",
                "Showbox",
                "Moore Theatre"
            ]
        },
        {
            "pergunta": "Qual música do álbum Bleach foi regravada para Nevermind?",
            "correta": "About a Girl",
            "erradas": [
                "School",
                "Love Buzz",
                "Blew"
            ]
        },
        {
            "pergunta": "Quem desenhou a maior parte da arte e dos conceitos visuais criados por Kurt Cobain para a banda?",
            "correta": "Kurt Cobain",
            "erradas": [
                "Charles Peterson",
                "Robert Fisher",
                "Krist Novoselic"
            ]
        },
        {
            "pergunta": "Qual foi o único álbum de estúdio do Nirvana lançado pela gravadora Sub Pop?",
            "correta": "Bleach",
            "erradas": [
                "Nevermind",
                "In Utero",
                "Incesticide"
            ]
        },
        {
            "pergunta": "Qual música encerra o álbum In Utero na edição original?",
            "correta": "All Apologies",
            "erradas": [
                "Gallons of Rubbing Alcohol Flow Through the Strip",
                "Tourette's",
                "Milk It"
            ]
        }
    ],

"Led Zeppelin": [
        {
            "pergunta": "Em que ano o Led Zeppelin foi formado?",
            "correta": "1968",
            "erradas": ["1966", "1967", "1969"]
        },
        {
            "pergunta": "Em qual país a banda foi criada?",
            "correta": "Reino Unido",
            "erradas": ["Estados Unidos", "Irlanda", "Canadá"]
        },
        {
            "pergunta": "Quem era o vocalista principal do Led Zeppelin?",
            "correta": "Robert Plant",
            "erradas": ["Jimmy Page", "John Paul Jones", "Roger Daltrey"]
        },
        {
            "pergunta": "Quem era o guitarrista da banda?",
            "correta": "Jimmy Page",
            "erradas": ["Jeff Beck", "Eric Clapton", "John Paul Jones"]
        },
        {
            "pergunta": "Qual integrante tocava baixo e teclado?",
            "correta": "John Paul Jones",
            "erradas": ["John Bonham", "Robert Plant", "Jimmy Page"]
        },
        {
            "pergunta": "Quem era o baterista do Led Zeppelin?",
            "correta": "John Bonham",
            "erradas": ["Keith Moon", "Charlie Watts", "Mick Fleetwood"]
        },
        {
            "pergunta": "Qual era o nome da banda anterior de onde vieram alguns integrantes do Led Zeppelin?",
            "correta": "The Yardbirds",
            "erradas": ["Cream", "The Who", "The Kinks"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia do Led Zeppelin?",
            "correta": "Led Zeppelin",
            "erradas": ["Led Zeppelin II", "Led Zeppelin III", "Houses of the Holy"]
        },
        {
            "pergunta": "Em que ano foi lançado Led Zeppelin (o primeiro álbum)?",
            "correta": "1969",
            "erradas": ["1968", "1970", "1971"]
        },
        {
            "pergunta": "Qual música abre o primeiro álbum da banda?",
            "correta": "Good Times Bad Times",
            "erradas": ["Babe I'm Gonna Leave You", "Dazed and Confused", "Communication Breakdown"]
        },
        {
            "pergunta": "Qual álbum contém a música Whole Lotta Love?",
            "correta": "Led Zeppelin II",
            "erradas": ["Led Zeppelin", "Led Zeppelin III", "Physical Graffiti"]
        },
        {
            "pergunta": "Em que ano foi lançado Led Zeppelin II?",
            "correta": "1969",
            "erradas": ["1968", "1970", "1971"]
        },
        {
            "pergunta": "Qual música de Led Zeppelin III é fortemente inspirada no folk?",
            "correta": "That's the Way",
            "erradas": ["Immigrant Song", "Out on the Tiles", "Celebration Day"]
        },
        {
            "pergunta": "Qual álbum é conhecido informalmente como Led Zeppelin IV?",
            "correta": "Untitled",
            "erradas": ["Houses of the Holy", "Physical Graffiti", "Presence"]
        },
        {
            "pergunta": "Qual música de Led Zeppelin IV se tornou a mais famosa da banda?",
            "correta": "Stairway to Heaven",
            "erradas": ["Black Dog", "Rock and Roll", "Misty Mountain Hop"]
        },
        {
            "pergunta": "Qual canção começa com uma introdução de violão acústico e se transforma em um épico do rock?",
            "correta": "Stairway to Heaven",
            "erradas": ["Kashmir", "Black Dog", "Over the Hills and Far Away"]
        },
        {
            "pergunta": "Quem compôs a maior parte das letras do Led Zeppelin?",
            "correta": "Robert Plant",
            "erradas": ["Jimmy Page", "John Paul Jones", "John Bonham"]
        },
        {
            "pergunta": "Qual álbum contém a música Kashmir?",
            "correta": "Physical Graffiti",
            "erradas": ["Houses of the Holy", "Presence", "Led Zeppelin IV"]
        },
        {
            "pergunta": "Em que ano foi lançado Physical Graffiti?",
            "correta": "1975",
            "erradas": ["1973", "1974", "1976"]
        },
        {
            "pergunta": "Qual música de Physical Graffiti possui um riff marcante e foi amplamente utilizada em filmes e séries?",
            "correta": "Kashmir",
            "erradas": ["Trampled Under Foot", "Ten Years Gone", "In the Light"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Achilles Last Stand?",
            "correta": "Presence",
            "erradas": ["Physical Graffiti", "In Through the Out Door", "Houses of the Holy"]
        },
        {
            "pergunta": "Qual foi o último álbum de estúdio lançado pela banda antes da morte de John Bonham?",
            "correta": "In Through the Out Door",
            "erradas": ["Presence", "Coda", "Physical Graffiti"]
        },
        {
            "pergunta": "Em que ano John Bonham faleceu?",
            "correta": "1980",
            "erradas": ["1978", "1979", "1981"]
        },
        {
            "pergunta": "Qual foi a causa oficial do fim do Led Zeppelin?",
            "correta": "A morte de John Bonham",
            "erradas": [
                "Conflitos internos",
                "Problemas financeiros",
                "A saída de Robert Plant"
            ]
        },
        {
            "pergunta": "Qual música do Led Zeppelin foi inspirada na obra O Senhor dos Anéis?",
            "correta": "Ramble On",
            "erradas": ["Kashmir", "Black Dog", "The Ocean"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Black Dog?",
            "correta": "Led Zeppelin IV",
            "erradas": ["Led Zeppelin III", "Houses of the Holy", "Physical Graffiti"]
        },
        {
            "pergunta": "Qual música da banda possui o famoso refrão 'Hey, hey, mama, said the way you move...'?",
            "correta": "Black Dog",
            "erradas": ["Rock and Roll", "Whole Lotta Love", "The Ocean"]
        },
        {
            "pergunta": "Qual gravadora foi fundada pelo Led Zeppelin em 1974?",
            "correta": "Swan Song Records",
            "erradas": ["Atlantic Records", "Harvest Records", "EMI Records"]
        },
        {
            "pergunta": "Qual foi o último álbum de estúdio lançado após a morte de Bonham, com material inédito de estúdio?",
            "correta": "Coda",
            "erradas": ["Presence", "In Through the Out Door", "BBC Sessions"]
        },
        {
            "pergunta": "Quantos integrantes tinha a formação clássica do Led Zeppelin?",
            "correta": "4",
            "erradas": ["3", "5", "6"]
        },
        {
            "pergunta": "Qual música do Led Zeppelin foi tema de inúmeros programas de rádio e rankings de rock clássico?",
            "correta": "Stairway to Heaven",
            "erradas": ["Kashmir", "Black Dog", "Whole Lotta Love"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Immigrant Song?",
            "correta": "Led Zeppelin III",
            "erradas": ["Led Zeppelin II", "Led Zeppelin IV", "Physical Graffiti"]
        },
        {
            "pergunta": "Qual música foi inspirada por uma viagem da banda à Islândia?",
            "correta": "Immigrant Song",
            "erradas": ["Ramble On", "Kashmir", "The Ocean"]
        },
        {
            "pergunta": "Qual integrante produziu a maioria dos álbuns do Led Zeppelin?",
            "correta": "Jimmy Page",
            "erradas": ["Robert Plant", "John Paul Jones", "John Bonham"]
        },
        {
            "pergunta": "Qual era o nome original do grupo durante suas primeiras apresentações em 1968, antes de adotar o nome Led Zeppelin?",
            "correta": "The New Yardbirds",
            "erradas": ["The Yardbirds II", "The Hindenburgs", "Band of Joy"]
        },
        {
            "pergunta": "Quem sugeriu a expressão que inspirou o nome 'Led Zeppelin'?",
            "correta": "Keith Moon",
            "erradas": ["Jeff Beck", "Eric Clapton", "Pete Townshend"]
        },
        {
            "pergunta": "Qual foi o primeiro show da banda sob seu nome definitivo?",
            "correta": "Universidade de Surrey",
            "erradas": [
                "Royal Albert Hall",
                "Madison Square Garden",
                "Marquee Club"
            ]
        },
        {
            "pergunta": "Em qual cidade foi realizado esse show?",
            "correta": "Guildford",
            "erradas": ["Londres", "Manchester", "Liverpool"]
        },
        {
            "pergunta": "Qual música de Led Zeppelin I foi baseada na canção tradicional You Shook Me?",
            "correta": "You Shook Me",
            "erradas": [
                "I Can't Quit You Baby",
                "Dazed and Confused",
                "Communication Breakdown"
            ]
        },
        {
            "pergunta": "Qual álbum foi gravado em uma casa de campo chamada Bron-Yr-Aur, no País de Gales?",
            "correta": "Led Zeppelin III",
            "erradas": [
                "Led Zeppelin II",
                "Houses of the Holy",
                "Physical Graffiti"
            ]
        },
        {
            "pergunta": "Qual música instrumental de Led Zeppelin III recebeu o nome da casa Bron-Yr-Aur?",
            "correta": "Bron-Y-Aur Stomp",
            "erradas": [
                "Friends",
                "Gallows Pole",
                "Tangerine"
            ]
        },
        {
            "pergunta": "Qual símbolo representa Jimmy Page na capa interna de Led Zeppelin IV?",
            "correta": "Zoso",
            "erradas": [
                "Três círculos entrelaçados",
                "Pena dentro de um círculo",
                "Círculo com três ovais"
            ]
        },
        {
            "pergunta": "Qual símbolo representa John Bonham em Led Zeppelin IV?",
            "correta": "Três círculos entrelaçados",
            "erradas": [
                "Zoso",
                "Pena dentro de um círculo",
                "Círculo com três ovais"
            ]
        },
        {
            "pergunta": "Qual música de Led Zeppelin IV foi gravada quase inteiramente ao vivo no estúdio?",
            "correta": "Rock and Roll",
            "erradas": [
                "Black Dog",
                "Misty Mountain Hop",
                "Four Sticks"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro álbum duplo da banda?",
            "correta": "Physical Graffiti",
            "erradas": [
                "Houses of the Holy",
                "Presence",
                "In Through the Out Door"
            ]
        },
        {
            "pergunta": "Qual música de Physical Graffiti foi originalmente gravada durante as sessões de Led Zeppelin IV?",
            "correta": "Down by the Seaside",
            "erradas": [
                "Kashmir",
                "Trampled Under Foot",
                "Ten Years Gone"
            ]
        },
        {
            "pergunta": "Qual faixa de Presence foi gravada enquanto Robert Plant se recuperava de um grave acidente de carro?",
            "correta": "Achilles Last Stand",
            "erradas": [
                "Nobody's Fault but Mine",
                "For Your Life",
                "Tea for One"
            ]
        },
        {
            "pergunta": "Em qual país ocorreu esse acidente?",
            "correta": "Grécia",
            "erradas": [
                "França",
                "Itália",
                "Espanha"
            ]
        },
        {
            "pergunta": "Qual música de Presence possui mais de 10 minutos de duração e abre o álbum?",
            "correta": "Achilles Last Stand",
            "erradas": [
                "Tea for One",
                "Nobody's Fault but Mine",
                "For Your Life"
            ]
        },
        {
            "pergunta": "Qual foi o último show completo do Led Zeppelin com John Bonham?",
            "correta": "Eissporthalle, Berlim Ocidental, 7 de julho de 1980",
            "erradas": [
                "Knebworth Festival 1979",
                "Royal Albert Hall 1980",
                "Madison Square Garden 1980"
            ]
        },
        {
            "pergunta": "Em qual cidade aconteceu esse show?",
            "correta": "Berlim",
            "erradas": [
                "Londres",
                "Hamburgo",
                "Munique"
            ]
        },
        {
            "pergunta": "Qual música inédita de Coda foi originalmente gravada durante as sessões de Led Zeppelin III?",
            "correta": "Poor Tom",
            "erradas": [
                "Wearing and Tearing",
                "Bonzo's Montreux",
                "Ozone Baby"
            ]
        },
        {
            "pergunta": "Quem produziu todos os álbuns de estúdio do Led Zeppelin?",
            "correta": "Jimmy Page",
            "erradas": [
                "Robert Plant",
                "John Paul Jones",
                "Eddie Kramer"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa In the Light?",
            "correta": "Physical Graffiti",
            "erradas": [
                "Presence",
                "Houses of the Holy",
                "Led Zeppelin IV"
            ]
        },
        {
            "pergunta": "Qual foi a data da morte de John Bonham?",
            "correta": "25 de setembro de 1980",
            "erradas": [
                "24 de setembro de 1980",
                "25 de agosto de 1980",
                "26 de setembro de 1980"
            ]
        },
        {
            "pergunta": "Em qual evento histórico a banda se reuniu em 2007 para um show completo com Jason Bonham na bateria?",
            "correta": "Ahmet Ertegun Tribute Concert",
            "erradas": [
                "Live Aid",
                "Concert for George",
                "Rock and Roll Hall of Fame Concert"
            ]
        }
    ],

"AC/DC": [
        {
            "pergunta": "Em que ano o AC/DC foi formado?",
            "correta": "1973",
            "erradas": ["1971", "1974", "1975"]
        },
        {
            "pergunta": "Em qual país a banda foi criada?",
            "correta": "Austrália",
            "erradas": ["Escócia", "Inglaterra", "Estados Unidos"]
        },
        {
            "pergunta": "Quem foram os irmãos que fundaram o AC/DC?",
            "correta": "Angus Young e Malcolm Young",
            "erradas": [
                "Angus Young e George Young",
                "Malcolm Young e George Young",
                "Angus Young e Alex Young"
            ]
        },
        {
            "pergunta": "Qual integrante ficou conhecido por usar uniforme escolar nos shows?",
            "correta": "Angus Young",
            "erradas": ["Malcolm Young", "Bon Scott", "Brian Johnson"]
        },
        {
            "pergunta": "Quem foi o vocalista original que levou a banda ao sucesso internacional?",
            "correta": "Bon Scott",
            "erradas": ["Brian Johnson", "Dave Evans", "Axl Rose"]
        },
        {
            "pergunta": "Qual álbum foi o último gravado com Bon Scott?",
            "correta": "Highway to Hell",
            "erradas": ["Powerage", "Let There Be Rock", "Back in Black"]
        },
        {
            "pergunta": "Em que ano Bon Scott faleceu?",
            "correta": "1980",
            "erradas": ["1979", "1981", "1982"]
        },
        {
            "pergunta": "Quem assumiu os vocais após a morte de Bon Scott?",
            "correta": "Brian Johnson",
            "erradas": ["Dave Evans", "Axl Rose", "Phil Rudd"]
        },
        {
            "pergunta": "Qual álbum lançado em 1980 se tornou o maior sucesso comercial da banda?",
            "correta": "Back in Black",
            "erradas": ["For Those About to Rock", "Highway to Hell", "The Razors Edge"]
        },
        {
            "pergunta": "Qual música abre o álbum Back in Black?",
            "correta": "Hells Bells",
            "erradas": [
                "Back in Black",
                "Shoot to Thrill",
                "Rock and Roll Ain't Noise Pollution"
            ]
        },
        {
            "pergunta": "Qual música de Back in Black possui o famoso sino em sua introdução?",
            "correta": "Hells Bells",
            "erradas": [
                "Back in Black",
                "Shoot to Thrill",
                "You Shook Me All Night Long"
            ]
        },
        {
            "pergunta": "Qual música tem o refrão 'For Those About to Rock, We Salute You'?",
            "correta": "For Those About to Rock (We Salute You)",
            "erradas": [
                "Back in Black",
                "Thunderstruck",
                "Highway to Hell"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado o álbum Highway to Hell?",
            "correta": "1979",
            "erradas": ["1978", "1980", "1981"]
        },
        {
            "pergunta": "Qual música dá nome a esse álbum?",
            "correta": "Highway to Hell",
            "erradas": [
                "Touch Too Much",
                "Shot Down in Flames",
                "Girls Got Rhythm"
            ]
        },
        {
            "pergunta": "Quem é o guitarrista solo mais famoso do AC/DC?",
            "correta": "Angus Young",
            "erradas": ["Malcolm Young", "Stevie Young", "Cliff Williams"]
        },
        {
            "pergunta": "Qual integrante geralmente toca guitarra rítmica?",
            "correta": "Malcolm Young",
            "erradas": ["Angus Young", "Cliff Williams", "Phil Rudd"]
        },
        {
            "pergunta": "Qual álbum contém a música Thunderstruck?",
            "correta": "The Razors Edge",
            "erradas": ["Back in Black", "Black Ice", "Power Up"]
        },
        {
            "pergunta": "Em que ano foi lançado The Razors Edge?",
            "correta": "1990",
            "erradas": ["1988", "1989", "1991"]
        },
        {
            "pergunta": "Qual música do AC/DC começa com um dos riffs mais famosos da história do rock, tocado em uma única corda?",
            "correta": "Thunderstruck",
            "erradas": ["Back in Black", "Highway to Hell", "T.N.T."]
        },
        {
            "pergunta": "Qual álbum contém a faixa Hells Bells?",
            "correta": "Back in Black",
            "erradas": ["Highway to Hell", "The Razors Edge", "For Those About to Rock"]
        },
        {
            "pergunta": "Qual foi o primeiro álbum de estúdio com Brian Johnson nos vocais?",
            "correta": "Back in Black",
            "erradas": ["Highway to Hell", "Fly on the Wall", "Flick of the Switch"]
        },
        {
            "pergunta": "Qual música do AC/DC foi usada em inúmeros filmes, eventos esportivos e jogos eletrônicos?",
            "correta": "Thunderstruck",
            "erradas": [
                "Rock 'n' Roll Train",
                "Moneytalks",
                "Who Made Who"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Shoot to Thrill?",
            "correta": "Back in Black",
            "erradas": ["Highway to Hell", "The Razors Edge", "Powerage"]
        },
        {
            "pergunta": "Qual integrante do AC/DC faleceu em 2017?",
            "correta": "Malcolm Young",
            "erradas": ["Angus Young", "Brian Johnson", "Cliff Williams"]
        },
        {
            "pergunta": "Em que ano Malcolm Young deixou definitivamente a banda devido a problemas de saúde?",
            "correta": "2014",
            "erradas": ["2012", "2013", "2015"]
        },
        {
            "pergunta": "Qual álbum marcou o retorno da banda em 2020 após vários anos sem material inédito?",
            "correta": "Power Up",
            "erradas": ["Black Ice", "Rock or Bust", "Stiff Upper Lip"]
        },
        {
            "pergunta": "Qual música do álbum Power Up foi lançada como primeiro single?",
            "correta": "Shot in the Dark",
            "erradas": [
                "Realize",
                "Demon Fire",
                "Through the Mists of Time"
            ]
        },
        {
            "pergunta": "Qual gravadora ajudou a lançar internacionalmente o AC/DC nos anos 1970?",
            "correta": "Atlantic Records",
            "erradas": [
                "EMI Records",
                "Capitol Records",
                "Columbia Records"
            ]
        },
        {
            "pergunta": "Qual é o significado do nome AC/DC?",
            "correta": "Corrente Alternada/Corrente Contínua",
            "erradas": [
                "Australian Classic/Dirty Crew",
                "Amplified Current/Direct Current",
                "Alternating Concert/Direct Concert"
            ]
        },
        {
            "pergunta": "Quantos irmãos Young fizeram parte da formação clássica da banda?",
            "correta": "2",
            "erradas": ["1", "3", "4"]
        },
        {
            "pergunta": "Em qual cidade da Escócia nasceram Angus e Malcolm Young?",
            "correta": "Glasgow",
            "erradas": ["Edimburgo", "Aberdeen", "Dundee"]
        },
        {
            "pergunta": "Qual irmã dos irmãos Young inspirou o nome AC/DC ao vê-lo em uma máquina de costura?",
            "correta": "Margaret Young",
            "erradas": ["Ellen Young", "Mary Young", "Christine Young"]
        },
        {
            "pergunta": "Qual foi o primeiro álbum internacional do AC/DC?",
            "correta": "High Voltage",
            "erradas": ["T.N.T.", "Dirty Deeds Done Dirt Cheap", "Let There Be Rock"]
        },
        {
            "pergunta": "Qual vocalista cantou no álbum australiano High Voltage de 1975?",
            "correta": "Bon Scott",
            "erradas": ["Brian Johnson", "Dave Evans", "Mark Evans"]
        },
        {
            "pergunta": "Qual foi o primeiro álbum internacional lançado com Bon Scott nos vocais?",
            "correta": "High Voltage",
            "erradas": ["T.N.T.", "Dirty Deeds Done Dirt Cheap", "Powerage"]
        },
        {
            "pergunta": "Qual música abre o álbum Highway to Hell?",
            "correta": "Highway to Hell",
            "erradas": [
                "Girls Got Rhythm",
                "Touch Too Much",
                "Shot Down in Flames"
            ]
        },
        {
            "pergunta": "Quem produziu os álbuns Highway to Hell e Back in Black?",
            "correta": "Robert John 'Mutt' Lange",
            "erradas": [
                "George Young",
                "Harry Vanda",
                "Brendan O'Brien"
            ]
        },
        {
            "pergunta": "Em qual cidade Bon Scott foi encontrado inconsciente antes de sua morte?",
            "correta": "Londres",
            "erradas": ["Glasgow", "Sydney", "Manchester"]
        },
        {
            "pergunta": "Qual música de Back in Black foi composta como uma homenagem indireta a Bon Scott?",
            "correta": "Back in Black",
            "erradas": [
                "Hells Bells",
                "Shoot to Thrill",
                "You Shook Me All Night Long"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Let There Be Rock?",
            "correta": "Let There Be Rock",
            "erradas": ["Powerage", "High Voltage", "Dirty Deeds Done Dirt Cheap"]
        },
        {
            "pergunta": "Qual baixista participou da gravação de Highway to Hell?",
            "correta": "Cliff Williams",
            "erradas": ["Mark Evans", "Chris Slade", "Larry Van Kriedt"]
        },
        {
            "pergunta": "Qual álbum foi o último com Phil Rudd antes de sua saída em 1983?",
            "correta": "Flick of the Switch",
            "erradas": [
                "For Those About to Rock",
                "Fly on the Wall",
                "Back in Black"
            ]
        },
        {
            "pergunta": "Qual baterista substituiu Phil Rudd durante boa parte dos anos 1980?",
            "correta": "Simon Wright",
            "erradas": [
                "Chris Slade",
                "Tony Currenti",
                "Mark Evans"
            ]
        },
        {
            "pergunta": "Qual álbum marcou o retorno de Phil Rudd à banda?",
            "correta": "Ballbreaker",
            "erradas": [
                "The Razors Edge",
                "Stiff Upper Lip",
                "Black Ice"
            ]
        },
        {
            "pergunta": "Qual música do AC/DC foi utilizada na abertura do filme Iron Man 2?",
            "correta": "Shoot to Thrill",
            "erradas": [
                "Thunderstruck",
                "Back in Black",
                "Highway to Hell"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Who Made Who?",
            "correta": "Who Made Who",
            "erradas": [
                "Fly on the Wall",
                "The Razors Edge",
                "Blow Up Your Video"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro álbum de estúdio do AC/DC lançado no século XXI?",
            "correta": "Stiff Upper Lip",
            "erradas": [
                "Black Ice",
                "Ballbreaker",
                "Rock or Bust"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado Black Ice?",
            "correta": "2008",
            "erradas": ["2006", "2007", "2009"]
        },
        {
            "pergunta": "Qual música de The Razors Edge se tornou um dos maiores hinos esportivos do rock?",
            "correta": "Thunderstruck",
            "erradas": [
                "Moneytalks",
                "Fire Your Guns",
                "Are You Ready"
            ]
        },
        {
            "pergunta": "Qual integrante assumiu oficialmente a guitarra rítmica após a aposentadoria de Malcolm Young?",
            "correta": "Stevie Young",
            "erradas": [
                "Angus Young",
                "Cliff Williams",
                "Phil Rudd"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Rock 'n' Roll Train?",
            "correta": "Black Ice",
            "erradas": [
                "Power Up",
                "Rock or Bust",
                "Stiff Upper Lip"
            ]
        },
        {
            "pergunta": "Qual foi o último álbum lançado com Malcolm Young ainda vivo?",
            "correta": "Power Up",
            "erradas": [
                "Black Ice",
                "Rock or Bust",
                "Stiff Upper Lip"
            ]
        },
        {
            "pergunta": "Qual música encerra o álbum Back in Black?",
            "correta": "Rock and Roll Ain't Noise Pollution",
            "erradas": [
                "Shake a Leg",
                "Have a Drink on Me",
                "Back in Black"
            ]
        },
        {
            "pergunta": "Quem desenhou a famosa logo clássica do AC/DC com o raio entre as letras?",
            "correta": "Gerard Huerta",
            "erradas": [
                "Hugh Syme",
                "Storm Thorgerson",
                "Roger Dean"
            ]
        },
        {
            "pergunta": "Qual álbum do AC/DC vendeu mais cópias mundialmente?",
            "correta": "Back in Black",
            "erradas": [
                "Highway to Hell",
                "The Razors Edge",
                "For Those About to Rock"
            ]
        }
    ],

"Slipknot": [
        {
            "pergunta": "Em que ano o Slipknot foi formado?",
            "correta": "1995",
            "erradas": ["1993", "1994", "1996"]
        },
        {
            "pergunta": "Em qual cidade dos Estados Unidos a banda surgiu?",
            "correta": "Des Moines",
            "erradas": ["Chicago", "Cleveland", "Detroit"]
        },
        {
            "pergunta": "Em qual estado americano fica essa cidade?",
            "correta": "Iowa",
            "erradas": ["Illinois", "Ohio", "Kansas"]
        },
        {
            "pergunta": "Quem é o vocalista principal do Slipknot?",
            "correta": "Corey Taylor",
            "erradas": ["Anders Colsefni", "Shawn Crahan", "Jim Root"]
        },
        {
            "pergunta": "Qual integrante ficou famoso por usar uma máscara de palhaço durante muitos anos?",
            "correta": "Shawn Crahan",
            "erradas": ["Corey Taylor", "Chris Fehn", "Sid Wilson"]
        },
        {
            "pergunta": "Qual integrante é conhecido por tocar percussão e fazer backing vocals agressivos?",
            "correta": "Chris Fehn",
            "erradas": ["Craig Jones", "Paul Gray", "Mick Thomson"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia do Slipknot por uma grande gravadora?",
            "correta": "Slipknot",
            "erradas": [
                "Mate. Feed. Kill. Repeat.",
                "Iowa",
                "Vol. 3: (The Subliminal Verses)"
            ]
        },
        {
            "pergunta": "Em que ano esse álbum foi lançado?",
            "correta": "1999",
            "erradas": ["1998", "2000", "2001"]
        },
        {
            "pergunta": "Qual música do álbum Slipknot se tornou um dos maiores sucessos da banda?",
            "correta": "Wait and Bleed",
            "erradas": ["Surfacing", "Spit It Out", "Me Inside"]
        },
        {
            "pergunta": "Qual álbum contém a música Left Behind?",
            "correta": "Iowa",
            "erradas": [
                "Slipknot",
                "Vol. 3: (The Subliminal Verses)",
                ".5: The Gray Chapter"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado Iowa?",
            "correta": "2001",
            "erradas": ["2000", "2002", "2003"]
        },
        {
            "pergunta": "Qual álbum contém as faixas Duality e Before I Forget?",
            "correta": "Vol. 3: (The Subliminal Verses)",
            "erradas": [
                "Iowa",
                ".5: The Gray Chapter",
                "All Hope Is Gone"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado Vol. 3: (The Subliminal Verses)?",
            "correta": "2004",
            "erradas": ["2003", "2005", "2006"]
        },
        {
            "pergunta": "Qual música do Slipknot possui o verso 'I push my fingers into my eyes'?",
            "correta": "Duality",
            "erradas": ["Before I Forget", "Psychosocial", "Left Behind"]
        },
        {
            "pergunta": "Qual integrante morreu em 2010?",
            "correta": "Paul Gray",
            "erradas": ["Joey Jordison", "Chris Fehn", "Craig Jones"]
        },
        {
            "pergunta": "Qual instrumento Paul Gray tocava?",
            "correta": "Baixo",
            "erradas": ["Guitarra", "Bateria", "Percussão"]
        },
        {
            "pergunta": "Qual álbum foi lançado em 2008 e contém a música Psychosocial?",
            "correta": "All Hope Is Gone",
            "erradas": [
                "Vol. 3: (The Subliminal Verses)",
                "Iowa",
                ".5: The Gray Chapter"
            ]
        },
        {
            "pergunta": "Quem era o baterista fundador da banda?",
            "correta": "Joey Jordison",
            "erradas": ["Jay Weinberg", "Shawn Crahan", "Chris Fehn"]
        },
        {
            "pergunta": "Qual integrante saiu da banda em 2013 e depois retornou?",
            "correta": "Donnie Steele",
            "erradas": ["Jim Root", "Mick Thomson", "Craig Jones"]
        },
        {
            "pergunta": "Qual álbum marcou o retorno da banda após a morte de Paul Gray?",
            "correta": ".5: The Gray Chapter",
            "erradas": [
                "All Hope Is Gone",
                "We Are Not Your Kind",
                "The End, So Far"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado .5: The Gray Chapter?",
            "correta": "2014",
            "erradas": ["2013", "2015", "2016"]
        },
        {
            "pergunta": "Qual álbum contém a faixa Unsainted?",
            "correta": "We Are Not Your Kind",
            "erradas": [
                ".5: The Gray Chapter",
                "All Hope Is Gone",
                "The End, So Far"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado We Are Not Your Kind?",
            "correta": "2019",
            "erradas": ["2018", "2020", "2021"]
        },
        {
            "pergunta": "Qual música de We Are Not Your Kind foi indicada ao Grammy?",
            "correta": "Unsainted",
            "erradas": ["Nero Forte", "Birth of the Cruel", "Critical Darling"]
        },
        {
            "pergunta": "Qual álbum foi lançado em 2022?",
            "correta": "The End, So Far",
            "erradas": [
                "We Are Not Your Kind",
                ".5: The Gray Chapter",
                "All Hope Is Gone"
            ]
        },
        {
            "pergunta": "Qual número era tradicionalmente associado a Corey Taylor?",
            "correta": "#8",
            "erradas": ["#1", "#6", "#9"]
        },
        {
            "pergunta": "Qual número era associado a Joey Jordison?",
            "correta": "#1",
            "erradas": ["#2", "#3", "#8"]
        },
        {
            "pergunta": "Qual número era associado a Paul Gray?",
            "correta": "#2",
            "erradas": ["#1", "#4", "#7"]
        },
        {
            "pergunta": "Quantos integrantes compunham a formação clássica do Slipknot?",
            "correta": "9",
            "erradas": ["7", "8", "10"]
        },
        {
            "pergunta": "Qual é o símbolo mais famoso associado à banda?",
            "correta": "Nonagrama",
            "erradas": [
                "Pentagrama",
                "Cabra de Baphomet",
                "Máscara de palhaço"
            ]
        },
        {
            "pergunta": "Qual era o nome do primeiro álbum independente lançado pelo Slipknot em 1996?",
            "correta": "Mate. Feed. Kill. Repeat.",
            "erradas": [
                "Crowz",
                "Slipknot",
                "Iowa"
            ]
        },
        {
            "pergunta": "Quem era o vocalista da banda antes da entrada de Corey Taylor?",
            "correta": "Anders Colsefni",
            "erradas": [
                "Paul Gray",
                "Shawn Crahan",
                "Sid Wilson"
            ]
        },
        {
            "pergunta": "Qual integrante tocava guitarra no álbum independente Mate. Feed. Kill. Repeat. mas não permaneceu na formação clássica?",
            "correta": "Donnie Steele",
            "erradas": [
                "Jim Root",
                "Mick Thomson",
                "Josh Brainard"
            ]
        },
        {
            "pergunta": "Qual música de Mate. Feed. Kill. Repeat. foi regravada e transformada em Me Inside no álbum de 1999?",
            "correta": "Nature",
            "erradas": [
                "Only One",
                "Slipknot",
                "Gently"
            ]
        },
        {
            "pergunta": "Qual produtor trabalhou no álbum Slipknot (1999) e ajudou a moldar o som da banda?",
            "correta": "Ross Robinson",
            "erradas": [
                "Rick Rubin",
                "Terry Date",
                "Bob Rock"
            ]
        },
        {
            "pergunta": "Qual integrante usava o número #6?",
            "correta": "Shawn Crahan",
            "erradas": [
                "Corey Taylor",
                "Chris Fehn",
                "Craig Jones"
            ]
        },
        {
            "pergunta": "Qual integrante usava o número #7?",
            "correta": "Mick Thomson",
            "erradas": [
                "Jim Root",
                "Paul Gray",
                "Corey Taylor"
            ]
        },
        {
            "pergunta": "Qual música abre oficialmente o álbum Slipknot (desconsiderando a introdução 742617000027)?",
            "correta": "(sic)",
            "erradas": [
                "Eyeless",
                "Wait and Bleed",
                "Surfacing"
            ]
        },
        {
            "pergunta": "Qual faixa encerra o álbum Iowa?",
            "correta": "Iowa",
            "erradas": [
                "Left Behind",
                "People = Shit",
                "New Abortion"
            ]
        },
        {
            "pergunta": "Qual álbum do Slipknot contém a música The Nameless?",
            "correta": "Vol. 3: (The Subliminal Verses)",
            "erradas": [
                "Iowa",
                "All Hope Is Gone",
                ".5: The Gray Chapter"
            ]
        },
        {
            "pergunta": "Qual integrante foi expulso da banda em 2019 após uma disputa judicial?",
            "correta": "Chris Fehn",
            "erradas": [
                "Craig Jones",
                "Jim Root",
                "Sid Wilson"
            ]
        },
        {
            "pergunta": "Qual era o instrumento principal de Chris Fehn dentro do Slipknot?",
            "correta": "Percussão",
            "erradas": [
                "Baixo",
                "Guitarra",
                "Teclado"
            ]
        },
        {
            "pergunta": "Qual integrante entrou para substituir Paul Gray nos shows após sua morte?",
            "correta": "Donnie Steele",
            "erradas": [
                "Alessandro Venturella",
                "V-Man",
                "Jay Weinberg"
            ]
        },
        {
            "pergunta": "Qual baixista gravou o álbum .5: The Gray Chapter?",
            "correta": "Alessandro Venturella",
            "erradas": [
                "Donnie Steele",
                "Paul Gray",
                "Chris Fehn"
            ]
        },
        {
            "pergunta": "Qual música de .5: The Gray Chapter venceu o Grammy de Melhor Performance de Metal?",
            "correta": "Custer",
            "erradas": [
                "The Devil in I",
                "Killpop",
                "Sarcastrophe"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Nero Forte?",
            "correta": "We Are Not Your Kind",
            "erradas": [
                ".5: The Gray Chapter",
                "All Hope Is Gone",
                "The End, So Far"
            ]
        },
        {
            "pergunta": "Qual membro da banda é conhecido pelo apelido 'Clown'?",
            "correta": "Shawn Crahan",
            "erradas": [
                "Corey Taylor",
                "Sid Wilson",
                "Chris Fehn"
            ]
        },
        {
            "pergunta": "Qual integrante foi demitido em 2013 e posteriormente revelou sofrer de mielite transversa?",
            "correta": "Joey Jordison",
            "erradas": [
                "Chris Fehn",
                "Craig Jones",
                "Paul Gray"
            ]
        },
        {
            "pergunta": "Qual música de Vol. 3: (The Subliminal Verses) foi inspirada nos ataques de 11 de setembro, segundo Corey Taylor?",
            "correta": "Pulse of the Maggots",
            "erradas": [
                "Duality",
                "Vermilion",
                "Before I Forget"
            ]
        },
        {
            "pergunta": "Qual produtor lendário trabalhou em Vol. 3: (The Subliminal Verses)?",
            "correta": "Rick Rubin",
            "erradas": [
                "Ross Robinson",
                "Bob Rock",
                "Terry Date"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Gematria (The Killing Name)?",
            "correta": "All Hope Is Gone",
            "erradas": [
                "Iowa",
                "Vol. 3: (The Subliminal Verses)",
                ".5: The Gray Chapter"
            ]
        },
        {
            "pergunta": "Qual era o número de Craig Jones?",
            "correta": "#5",
            "erradas": ["#4", "#6", "#9"]
        },
        {
            "pergunta": "Qual integrante ficou famoso por usar uma máscara com nariz extremamente longo?",
            "correta": "Chris Fehn",
            "erradas": [
                "Shawn Crahan",
                "Sid Wilson",
                "Craig Jones"
            ]
        },
        {
            "pergunta": "Em qual ano Craig Jones deixou a banda?",
            "correta": "2023",
            "erradas": ["2021", "2022", "2024"]
        },
        {
            "pergunta": "Qual álbum foi o último a contar com Craig Jones como integrante oficial?",
            "correta": "The End, So Far",
            "erradas": [
                "We Are Not Your Kind",
                ".5: The Gray Chapter",
                "All Hope Is Gone"
            ]
        }
    ],

"Guns N' Roses": [
        {
            "pergunta": "Em que ano o Guns N' Roses foi formado?",
            "correta": "1985",
            "erradas": ["1983", "1984", "1986"]
        },
        {
            "pergunta": "Em qual cidade a banda foi criada?",
            "correta": "Los Angeles",
            "erradas": ["Nova York", "Seattle", "Chicago"]
        },
        {
            "pergunta": "Quem é o vocalista principal do Guns N' Roses?",
            "correta": "Axl Rose",
            "erradas": ["Slash", "Duff McKagan", "Izzy Stradlin"]
        },
        {
            "pergunta": "Qual guitarrista ficou famoso por usar cartola e óculos escuros?",
            "correta": "Slash",
            "erradas": ["Izzy Stradlin", "Gilby Clarke", "Buckethead"]
        },
        {
            "pergunta": "Qual era o nome artístico do baixista fundador Duff McKagan?",
            "correta": "Duff 'Rose' McKagan",
            "erradas": [
                "Duff Thunder",
                "Duff Rebel",
                "Duff Rocket"
            ]
        },
        {
            "pergunta": "Quem foi o baterista da formação clássica do álbum Appetite for Destruction?",
            "correta": "Steven Adler",
            "erradas": ["Matt Sorum", "Frank Ferrer", "Josh Freese"]
        },
        {
            "pergunta": "Qual foi o álbum de estreia da banda?",
            "correta": "Appetite for Destruction",
            "erradas": [
                "G N' R Lies",
                "Use Your Illusion I",
                "Chinese Democracy"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado Appetite for Destruction?",
            "correta": "1987",
            "erradas": ["1986", "1988", "1989"]
        },
        {
            "pergunta": "Qual música abre esse álbum?",
            "correta": "Welcome to the Jungle",
            "erradas": [
                "It's So Easy",
                "Paradise City",
                "Nightrain"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro single lançado de Appetite for Destruction?",
            "correta": "It's So Easy",
            "erradas": [
                "Welcome to the Jungle",
                "Paradise City",
                "Sweet Child O' Mine"
            ]
        },
        {
            "pergunta": "Qual música se tornou o maior sucesso comercial da banda?",
            "correta": "Sweet Child O' Mine",
            "erradas": [
                "Welcome to the Jungle",
                "Paradise City",
                "November Rain"
            ]
        },
        {
            "pergunta": "Qual canção contém o famoso solo final de Slash e o refrão 'Where do we go now?'?",
            "correta": "Sweet Child O' Mine",
            "erradas": [
                "Paradise City",
                "Patience",
                "Don't Cry"
            ]
        },
        {
            "pergunta": "Qual música de Appetite for Destruction fala sobre a vida difícil nas ruas?",
            "correta": "Welcome to the Jungle",
            "erradas": [
                "Rocket Queen",
                "Mr. Brownstone",
                "Paradise City"
            ]
        },
        {
            "pergunta": "Qual EP lançado em 1988 ajudou a consolidar o sucesso da banda?",
            "correta": "G N' R Lies",
            "erradas": [
                "Live ?!*@ Like a Suicide",
                "The Spaghetti Incident?",
                "Use Your Illusion"
            ]
        },
        {
            "pergunta": "Qual música do EP G N' R Lies gerou controvérsias por sua letra?",
            "correta": "One in a Million",
            "erradas": [
                "Patience",
                "Used to Love Her",
                "Mama Kin"
            ]
        },
        {
            "pergunta": "Em que ano foram lançados os álbuns Use Your Illusion I e Use Your Illusion II?",
            "correta": "1991",
            "erradas": ["1989", "1990", "1992"]
        },
        {
            "pergunta": "Qual música de Use Your Illusion I se tornou um dos maiores sucessos da banda e possui um videoclipe épico?",
            "correta": "November Rain",
            "erradas": [
                "Don't Cry",
                "Live and Let Die",
                "Coma"
            ]
        },
        {
            "pergunta": "Qual música de Use Your Illusion II começa com assobios e uma introdução marcante ao piano?",
            "correta": "Civil War",
            "erradas": [
                "Yesterdays",
                "Estranged",
                "Breakdown"
            ]
        },
        {
            "pergunta": "Quem toca piano em várias músicas famosas do Guns N' Roses?",
            "correta": "Axl Rose",
            "erradas": [
                "Slash",
                "Duff McKagan",
                "Dizzy Reed"
            ]
        },
        {
            "pergunta": "Qual música foi escrita em homenagem a Erin Everly, então namorada de Axl Rose?",
            "correta": "Sweet Child O' Mine",
            "erradas": [
                "Patience",
                "November Rain",
                "Don't Cry"
            ]
        },
        {
            "pergunta": "Qual integrante deixou a banda em 1996 e foi considerado insubstituível por muitos fãs?",
            "correta": "Slash",
            "erradas": [
                "Duff McKagan",
                "Matt Sorum",
                "Dizzy Reed"
            ]
        },
        {
            "pergunta": "Qual álbum de estúdio foi lançado em 2008 após mais de uma década de produção?",
            "correta": "Chinese Democracy",
            "erradas": [
                "Use Your Illusion II",
                "The Spaghetti Incident?",
                "Hard Skool"
            ]
        },
        {
            "pergunta": "Qual música abre o álbum Chinese Democracy?",
            "correta": "Chinese Democracy",
            "erradas": [
                "Shackler's Revenge",
                "Better",
                "Street of Dreams"
            ]
        },
        {
            "pergunta": "Em que ano Slash retornou oficialmente ao Guns N' Roses?",
            "correta": "2016",
            "erradas": ["2014", "2015", "2017"]
        },
        {
            "pergunta": "Qual baixista também retornou junto com Slash?",
            "correta": "Duff McKagan",
            "erradas": [
                "Tommy Stinson",
                "Chris Pitman",
                "Gilby Clarke"
            ]
        },
        {
            "pergunta": "Qual música do Guns N' Roses foi tema do filme Days of Thunder?",
            "correta": "Knockin' on Heaven's Door",
            "erradas": [
                "Civil War",
                "You Could Be Mine",
                "Patience"
            ]
        },
        {
            "pergunta": "Qual música de Use Your Illusion II fala sobre guerra e conflitos?",
            "correta": "Civil War",
            "erradas": [
                "Yesterdays",
                "Estranged",
                "So Fine"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Civil War?",
            "correta": "Use Your Illusion II",
            "erradas": [
                "Use Your Illusion I",
                "Chinese Democracy",
                "Appetite for Destruction"
            ]
        },
        {
            "pergunta": "Qual música do Guns N' Roses foi inspirada em um livro de Stephen King?",
            "correta": "Night Train",
            "erradas": [
                "Welcome to the Jungle",
                "Coma",
                "Paradise City"
            ]
        },
        {
            "pergunta": "Quantos integrantes compunham a formação clássica mais famosa da banda?",
            "correta": "5",
            "erradas": ["4", "6", "7"]
        },
        {
            "pergunta": "Qual banda surgiu da fusão dos grupos Hollywood Rose e L.A. Guns?",
            "correta": "Guns N' Roses",
            "erradas": [
                "Velvet Revolver",
                "Poison",
                "Skid Row"
            ]
        },
        {
            "pergunta": "Quem era o guitarrista líder do L.A. Guns que participou da formação inicial do Guns N' Roses?",
            "correta": "Tracii Guns",
            "erradas": [
                "Slash",
                "Izzy Stradlin",
                "Gilby Clarke"
            ]
        },
        {
            "pergunta": "Qual foi o primeiro EP lançado pelo Guns N' Roses?",
            "correta": "Live ?!*@ Like a Suicide",
            "erradas": [
                "G N' R Lies",
                "Use Your Illusion",
                "The Spaghetti Incident?"
            ]
        },
        {
            "pergunta": "Em que ano foi lançado o EP Live ?!*@ Like a Suicide?",
            "correta": "1986",
            "erradas": ["1985", "1987", "1988"]
        },
        {
            "pergunta": "Qual música de Appetite for Destruction foi originalmente escrita pela banda Hollywood Rose?",
            "correta": "Anything Goes",
            "erradas": [
                "Paradise City",
                "Mr. Brownstone",
                "Rocket Queen"
            ]
        },
        {
            "pergunta": "Quem produziu o álbum Appetite for Destruction?",
            "correta": "Mike Clink",
            "erradas": [
                "Bob Rock",
                "Rick Rubin",
                "Brendan O'Brien"
            ]
        },
        {
            "pergunta": "Qual música de Appetite for Destruction foi relançada em 1988 e finalmente alcançou o topo das paradas?",
            "correta": "Sweet Child O' Mine",
            "erradas": [
                "Welcome to the Jungle",
                "Paradise City",
                "Nightrain"
            ]
        },
        {
            "pergunta": "Qual integrante foi demitido em 1990 devido a problemas com drogas e álcool?",
            "correta": "Steven Adler",
            "erradas": [
                "Izzy Stradlin",
                "Duff McKagan",
                "Slash"
            ]
        },
        {
            "pergunta": "Quem substituiu Steven Adler na bateria durante os álbuns Use Your Illusion?",
            "correta": "Matt Sorum",
            "erradas": [
                "Josh Freese",
                "Frank Ferrer",
                "Tommy Aldridge"
            ]
        },
        {
            "pergunta": "Qual música de Use Your Illusion I conta com participação vocal de Shannon Hoon, da banda Blind Melon?",
            "correta": "Don't Cry",
            "erradas": [
                "November Rain",
                "Live and Let Die",
                "Bad Obsession"
            ]
        },
        {
            "pergunta": "Qual música de Use Your Illusion II possui mais de 9 minutos de duração?",
            "correta": "Estranged",
            "erradas": [
                "Civil War",
                "Yesterdays",
                "Locomotive"
            ]
        },
        {
            "pergunta": "Quem tocou o solo de guitarra na introdução de Civil War?",
            "correta": "Slash",
            "erradas": [
                "Izzy Stradlin",
                "Duff McKagan",
                "Axl Rose"
            ]
        },
        {
            "pergunta": "Qual integrante deixou a banda em 1991 alegando divergências com Axl Rose?",
            "correta": "Izzy Stradlin",
            "erradas": [
                "Slash",
                "Duff McKagan",
                "Matt Sorum"
            ]
        },
        {
            "pergunta": "Quem substituiu Izzy Stradlin na guitarra rítmica?",
            "correta": "Gilby Clarke",
            "erradas": [
                "Buckethead",
                "Robin Finck",
                "Richard Fortus"
            ]
        },
        {
            "pergunta": "Qual álbum contém a faixa Locomotive (Complicity)?",
            "correta": "Use Your Illusion II",
            "erradas": [
                "Use Your Illusion I",
                "Chinese Democracy",
                "Appetite for Destruction"
            ]
        },
        {
            "pergunta": "Qual foi o último álbum de estúdio lançado pela formação clássica antes de começar a se desfazer?",
            "correta": "Use Your Illusion II",
            "erradas": [
                "Use Your Illusion I",
                "Appetite for Destruction",
                "Chinese Democracy"
            ]
        },
        {
            "pergunta": "Qual álbum de covers foi lançado em 1993?",
            "correta": "The Spaghetti Incident?",
            "erradas": [
                "Chinese Democracy",
                "G N' R Lies",
                "Live Era '87–'93"
            ]
        },
        {
            "pergunta": "Qual ex-guitarrista do Nine Inch Nails entrou para o Guns N' Roses durante a era Chinese Democracy?",
            "correta": "Robin Finck",
            "erradas": [
                "Buckethead",
                "Richard Fortus",
                "Bumblefoot"
            ]
        },
        {
            "pergunta": "Em qual ano ocorreu o famoso incidente de Axl Rose em St. Louis, quando ele abandonou o palco após confrontar um fã?",
            "correta": "1991",
            "erradas": ["1989", "1990", "1992"]
        },
        {
            "pergunta": "Qual música abre o álbum Use Your Illusion II?",
            "correta": "Civil War",
            "erradas": [
                "Yesterdays",
                "14 Years",
                "Estranged"
            ]
        },
        {
            "pergunta": "Qual integrante gravou baixo em grande parte de Chinese Democracy?",
            "correta": "Tommy Stinson",
            "erradas": [
                "Duff McKagan",
                "Chris Pitman",
                "Paul Tobias"
            ]
        },
        {
            "pergunta": "Qual música de Chinese Democracy havia sido tocada ao vivo anos antes de seu lançamento oficial?",
            "correta": "Chinese Democracy",
            "erradas": [
                "Better",
                "Street of Dreams",
                "There Was a Time"
            ]
        },
        {
            "pergunta": "Quem desenhou a arte original da capa de Appetite for Destruction que acabou sendo substituída?",
            "correta": "Robert Williams",
            "erradas": [
                "Hugh Syme",
                "Storm Thorgerson",
                "Roger Dean"
            ]
        },
        {
            "pergunta": "Qual foi o nome da gigantesca turnê mundial realizada entre 1991 e 1993?",
            "correta": "Use Your Illusion Tour",
            "erradas": [
                "Appetite World Tour",
                "Paradise Tour",
                "World on Fire Tour"
            ]
        },
        {
            "pergunta": "Qual música encerra o álbum Use Your Illusion II?",
            "correta": "My World",
            "erradas": [
                "Estranged",
                "Locomotive",
                "You Could Be Mine"
            ]
        }
    ]
}

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    def escolher_banda_musical():

        print("=" * 43)
        print("┴┬┴┤(･_├┬┴┬┴ ESCOLHA UMA BANDA PARA COMEÇAR:")
        print("=" * 43)

        print("1 - Imagine Dragons")
        print("2 - Metallica")
        print("3 - Gorillaz")
        print("4 - Blur")
        print("5 - Linkin Park")
        print("6 - Nirvana")
        print("7 - Led Zeppelin")
        print("8 - AC/DC")
        print("9 - Slipknot")
        print("10 - Guns N' Roses")
        print()

    while True:
        escolha = input("(°o°) Escolha uma opção: ")

        if escolha == "1":
            return "Imagine Dragons"
        elif escolha == "2":
            return "Metallica"
        elif escolha == "3":
            return "Gorillaz"
        elif escolha == "4":
            return "Blur"
        elif escolha == "5":
            return "Linkin Park"
        elif escolha == "6":
            return "Nirvana"
        elif escolha == "7":
            return "Led Zeppelin"
        elif escolha == "8":
            return "AC/DC"
        elif escolha == "9":
            return "Slipknot"
        elif escolha == "10":
            return "Guns N' Roses"
        else:
            print("Opção inválida.\n")


    # 🏆 RANKING GLOBAL (dentro da execução)
    ranking = []

    # 🧠 controle de repetição
    perguntas_usadas = set()

    banda_escolhida = escolher_banda_musical()

    vidas = 3
    pontos = 0

    # pega todas perguntas da banda
    todas_perguntas = Questoes[banda_escolhida]

    # remove perguntas já usadas
    perguntas_disponiveis = [
        q for q in todas_perguntas
        if q["pergunta"] not in perguntas_usadas
    ]

    # embaralha
    random.shuffle(perguntas_disponiveis)

    for questao in perguntas_disponiveis:

        # marca como usada
        perguntas_usadas.add(questao["pergunta"])

        alternativas = [questao["correta"]]
        alternativas.extend(questao["erradas"])
        random.shuffle(alternativas)

        print("\n" + questao["pergunta"])
        print()

        for i, alternativa in enumerate(alternativas, start=1):
            print(f"{i} - {alternativa}")

        escolha = input("\nEscolha uma alternativa (1-4): ")

        indice_correto = alternativas.index(questao["correta"]) + 1

        if escolha.isdigit() and int(escolha) == indice_correto:
            print("( ͡° ͜ʖ ͡°) Você acertou!")
            pontos += 1
        else:
            print("(╬ Ò﹏Ó) Você errou!")
            vidas -= 1

            if vidas == 0:
                print("¯_(ツ)_/¯ Fim de Jogo!")
                break

        input("Pressione ENTER para continuar...")


    # 🏁 FINAL DO JOGO + RANKING
    nome = input("\n(⌐■_■) Digite seu nome: ")
    ranking.append((nome, pontos))

    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\n===(✧ω✧) RANKING (✧ω✧)===")
    for i, (nome, pontos) in enumerate(ranking, start=1):
        print(f"{i}º {nome} - {pontos} pontos")

    jogar_novamente = input(
        "\n Deseja jogar novamente? [s] ╭∩╮( •̀_•́ )╭∩╮ [n]: "
    ).strip().lower()

    if jogar_novamente == "s":
    break  # reinicia o quiz

    elif jogar_novamente == "n":
        print("(☞ﾟヮﾟ)☞ Obrigado por jogar!")
        exit()

    else:
        print("Digite apenas 's' ou 'n'.")
