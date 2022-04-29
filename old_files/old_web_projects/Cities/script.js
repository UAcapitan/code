let cities = [
    "Киев",
    "Москва",
    "Минск",
    "Прага",
    "Токио",
    "Пекин",
    "Монако",
    "Варшава",
    "Лондон",
    "Париж",
    "Амстердам",
    "Стамбул",
    "Вашингтон",
    "Рим"
]

let random = Math.floor(Math.random()*cities.length);

let word = cities[random].toLowerCase();

let secretWord = [];

for (let i = 0; i < word.length; i++) {
    secretWord.push("_");
}

let p = 0;

document.getElementById("text").innerHTML = secretWord.join(" ");

function submit() {
    let inputWord = document.getElementById("word").value;
    if (inputWord == word) {
        for (let i = 0; i < word.length; i++) {
                secretWord[i] = word[i];
        }
    } else {
        for (let i = 0; i < word.length; i++) {
            if (inputWord == word[i]) {
                secretWord[i] = inputWord;
            }
        }
    }
    p++;
    document.getElementById("text").innerHTML = secretWord.join(" ");
    document.getElementById("p").innerHTML = "Попыток: " + p;
    document.getElementById("word").value = "";
    if (word == secretWord.join("")) {
        win();
    }
}

function win() {
    document.getElementById("win").style.display = "block";
    document.getElementById("p_win").innerHTML = "Попыток: " + p;
}

function restart() {
    random = Math.floor(Math.random()*cities.length);

    word = cities[random].toLowerCase();

    secretWord = [];

    for (let i = 0; i < word.length; i++) {
        secretWord.push("_");
    }

    p = 0;

    document.getElementById("text").innerHTML = secretWord.join(" ");
    document.getElementById("win").style.display = "none";
    document.getElementById("word").value = "";
    document.getElementById("p").innerHTML = "Попыток: 0";
}

$(document).keypress(function (e) {
    if (e.which == 13) {
        if (document.getElementById("win").style.display == "block") {
            restart();
        } else {
            submit();
        }
    }
})