const questoes = {
    "Imagine Dragons": [
      {
        pergunta: "Em que cidade a banda "
                + "foi formada?",
        correta: "Las Vegas",
        erradas: ["Seattle",
                   "Los Angeles",
                   "Phoenix"]
      },
      // ... mais perguntas
    ],
    "Metallica": [ /* ... */ ]
  };

  function escolherBandaMusical() {
    console.log("ESCOLHA UMA BANDA:");
    console.log("1 - Imagine Dragons");
    console.log("2 - Metallica");
    // ...
  
    const bandas = {
      "1": "Imagine Dragons",
      "2": "Metallica",
      // ...
    };
  
    while (true) {
      const escolha = readline
        .question("Escolha: ");
  
      if (bandas[escolha]) return bandas[escolha];
      console.log("Opcao invalida.");
    }
}

function shuffle(array) {
    // Algoritmo de Fisher-Yates
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
  
  shuffle(perguntasDisponiveis);
  
  const alternativas = shuffle(
    [questao.correta, ...questao.erradas]
);

const readline = require("readline-sync");
const letras = ["A", "B", "C", "D"];

let escolha;
while (true) {
  escolha = readline
    .question("Escolha (A-D): ")
    .trim()
    .toUpperCase();

  if (letras.includes(escolha)) break;
  console.log("Digite apenas A, B, C ou D.");
}

const inicioPergunta = Date.now();
// ... usuario responde ...
const tempoResposta =
  (Date.now() - inicioPergunta) / 1000;

if (escolha === letraCorreta) {
  if (tempoResposta <= 5) {
    console.log("Acertou rapido! +2 pontos");
    pontos += 2;
  } else {
    console.log("Voce acertou!");
    pontos += 1;
  }
} else {
  console.log("Voce errou!");
  vidas -= 1;
}

const ranking = [];

ranking.push({ nome, pontos, tempoTotal });

ranking.sort((a, b) =>
  b.pontos - a.pontos || a.tempoTotal - b.tempoTotal
);

console.log("=== RANKING ===");
ranking.forEach((r, i) => {
  console.log(
    `${i + 1}o ${r.nome} - ${r.pontos} pontos - `
    + `${r.tempoTotal.toFixed(1)} segundos`
  );
});

