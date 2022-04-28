var money = -2;
var allMoneyLvl = 0;
var salary = 1;
var salaryInSec = 0;
var moneyInBank = 0;

var allMoney = 0;

var allMoneyForFlats = 0;
var allMoneyForCars = 0;
var allMoneyForTech = 0;
var allMoneyForObjects = 0;

var flats = 0;
var cars = 0;
var tech = 0;
var objects = 0;

var testForSituation = false;
var testForAchievements = 0;



//Массивы
var rowText = [
    "Непридвиденные затраты",
    "Ремонт техники",
    "Загубил кошелёк",
    "В банке ошибка и с вашего счёта списали деньги"
];

// Проверка есть ли сохранение
if_have_save();

//При нажатии на body добавляются деньги
document.body.onclick = function () {
    money += salary;
    allMoneyLvl += salary;
}

//Функция обновление счётчика денег
function moneyText() {
    document.getElementById("money").innerHTML = money + ' $';
    document.getElementById("moneyInSec").innerHTML = salary + " $/Click ----- " + salaryInSec + ' $/Sec';
    document.getElementById("moneyInBank").innerHTML = "Счёт в банке: " + moneyInBank + ' $';
    document.getElementById("moneyMain").innerHTML = "Счёт: " + money + ' $';
}

//Функция для зароботка money в секунду
function moneyInSec() {
    money += salaryInSec;
    allMoneyLvl += salaryInSec;
}

//Прокачка умений +1 доллар за нажатие
function Num1(a, b) {
    if (money >= a) {
        money -= a;
        salary += b;
    }
}

//Прокачка пассивного дохода
function Num2(a, b) {
    if (money >= a) {
        money -= a;
        salaryInSec += b;
    }
}

//Надпись при победе
function win() {
    if (money >= 100000000) {
        money -= 100000000;
        document.getElementById("win").style.display = "block";
        document.getElementById("win_btn").style.display = "none";
        document.getElementById("restart_btn").style.display = "block";
        setTimeout(function () {
            document.getElementById("win").style.display = "none";
        }, 3000);
    }
}

//Сбросить всё
function restart() {
    money = 0;
    allMoneyLvl = 0;
    salary = 1;
    salaryInSec = 0;
    moneyInBank = 0;
    allMoney = 0;
    allMoneyForFlats = 0;
    allMoneyForCars = 0;
    allMoneyForTech = 0;
    allMoneyForObjects = 0;
    flats = 0;
    cars = 0;
    tech = 0;
    objects = 0;

    document.getElementById("restart_btn").style.display = "none";
    document.getElementById("win_btn").style.display = "block";
    document.getElementById("restartCheck").style.display = "none";
}

//Спросить о сбросе
function restartCheck() {
    document.getElementById("restartCheck").style.display = "block";
}

//Скрыть запрос сброса
function restartHide() {
    document.getElementById("restartCheck").style.display = "none";
}

//Включить вкладки
function statistics() {
    document.getElementById("statistics").style.display = "block";
}
function shop() {
    document.getElementById("shop").style.display = "block";
}
function bank() {
    document.getElementById("bank").style.display = "block";
}
function information() {
    document.getElementById("information").style.display = "block";
}

//Положить деньги на счёт банка
function putMoney() {
    var inputMoney = document.getElementById("inputMoney").value;
    if (money >= inputMoney) {
        moneyInBank += Number(inputMoney);
        money -= inputMoney;
    }
}

//Положить все деньги на счёт банка
function putAllMoney() {
    moneyInBank += Number(money);
    money -= money;
}

//Снять деньги
function withdrawMoney() {
    var inputMoney = document.getElementById("inputMoney").value;
    if (moneyInBank >= inputMoney) {
        money += Number(inputMoney);
        moneyInBank -= inputMoney;
    }
}

//Снять все деньги
function withdrawAllMoney() {
    money += Number(moneyInBank);
    moneyInBank -= moneyInBank;
}

//Закрыть вкладку
function exit(el) {
    document.getElementById(el).style.display = "none";
}

//Обновление статистики
function statisticsUpdate() {
    document.getElementById("statisticsMoney").innerHTML = money + " $";
    document.getElementById("allMoneyLvl").innerHTML = allMoneyLvl + " $";
    document.getElementById("allMoneyInStatistics").innerHTML = allMoney + " $";
    document.getElementById("allMoneyForFlats").innerHTML = flats + " шт. Общая стоимость: " + allMoneyForFlats + " $";
    document.getElementById("allMoneyForCars").innerHTML = cars + " шт. Общая стоимость: " + allMoneyForCars + " $";
    document.getElementById("allMoneyForTech").innerHTML = tech + " шт. Общая стоимость: " + allMoneyForTech + " $";
    document.getElementById("allMoneyForObjects").innerHTML = objects + " шт. Общая стоимость: " + allMoneyForObjects + " $";
}

//Квартира
function flat(sum) {
    if (money > sum) {
        money -= sum;
        flats++;
        allMoneyForFlats += sum;
        allMoney += sum;
    }  
}
//Машина
function car(sum) {
    if (money > sum) {
        money -= sum;
        cars++;
        allMoneyForCars += sum;
        allMoney += sum;
    }  
}
//Техника
function tech_Func(sum) {
    if (money > sum) {
        money -= sum;
        tech++;
        allMoneyForTech += sum;
        allMoney += sum;
    }  
}
//Разное
function object(sum) {
    if (money > sum) {
        money -= sum;
        objects++;
        allMoneyForObjects += sum;
        allMoney += sum;
    }  
}

//Уровни
function lvl() {
    if (allMoneyLvl > -1 && allMoneyLvl <= 500 ) {
        document.getElementById("personal").style.backgroundImage = "url(src/lvl1.png)";
    }
    if (allMoneyLvl > 500 && allMoneyLvl <= 5000) {
        document.getElementById("personal").style.backgroundImage = "url(src/lvl2.png)";
    }
    if (allMoneyLvl > 5000 && allMoneyLvl <= 250000) {
        document.getElementById("personal").style.backgroundImage = "url(src/lvl3.png)";
    }
    if (allMoneyLvl > 250000 && allMoneyLvl <= 1000000) {
        document.getElementById("personal").style.backgroundImage = "url(src/lvl4.png)";
    }
    if (allMoneyLvl > 1000000 && allMoneyLvl <= 10000000) {
        document.getElementById("personal").style.backgroundImage = "url(src/lvl5.png)";
    }
    if (allMoneyLvl > 10000000 && allMoneyLvl <= 100000000) {
        document.getElementById("personal").style.backgroundImage = "url(src/lvl6.png)";
    }
    if (allMoneyLvl > 100000000) {
        document.getElementById("personal").style.backgroundImage = "url(src/lvl7.png)";
    }
}

//Рандомные затраты
function random() {
    if (money > 100 && testForSituation == false) {
        if (Math.floor(Math.random()*100) == Math.floor(Math.random()*100)) {
            let randomMoney = String(Math.floor(money / 100*(Math.random()*100)));
            document.getElementById("situation1").innerHTML = rowText[Math.floor(Math.random()*5)];
            document.getElementById("situation2").innerHTML = "-" + randomMoney + " $";
            document.getElementById("situation").style.display = "block";
            money -= randomMoney;
            testForSituation = true;
        }
    }
}

//Спрятать уведомление
function hideSituation() {
    document.getElementById("situation").style.display = "none";
    setTimeout(timerForShowSituation, 30000); 
}

//Таймер для повтора
function timerForShowSituation() {
    testForSituation = false;
}

//Дать время пользователю почитать 
function timerForHideSituation() {
    setTimeout(hideSituation, 3000);
}

//Функция для изминение статуса достижений
function statusAchievements(id) {
    document.getElementById(id).style.background = "green";
    document.getElementById(id).style.color = "white";
    testForAchievements++;
}

//Проверка достижений
function achievements() {
    if (allMoneyLvl >= 100) {
        statusAchievements("achievements1");
    }
    if (allMoneyLvl >= 1000) {
        statusAchievements("achievements2");
    }
    if (allMoneyLvl >= 1000000) {
        statusAchievements("achievements3");
    }
    if (allMoneyLvl >= 1000000000) {
        statusAchievements("achievements4");
    }
    if (allMoneyLvl >= 100000000000) {
        statusAchievements("achievements5");
    }
    if (allMoneyForFlats >= 100000000) {
        statusAchievements("achievements6");
    }
    if (allMoneyForCars >= 10000000) {
        statusAchievements("achievements7");
    }
    if (allMoneyForTech >= 1000000) {
        statusAchievements("achievements8");
    }
    if (allMoneyForObjects >= 10000000000) {
        statusAchievements("achievements9");
    }
    if (flats + cars + tech + objects >= 1000 && allMoneyForFlats + allMoneyForCars + allMoneyForTech + allMoneyForObjects >= 100000000) {
        statusAchievements("achievements10");
    }
    if (salaryInSec >= 100) {
        statusAchievements("achievements11");
    }
    if (salary >= 100000) {
        statusAchievements("achievements12");
    }
    if (salaryInSec >= 1000000) {
        statusAchievements("achievements13");
    }
    if (salaryInSec >= 1000000000) {
        statusAchievements("achievements14");
    }
    if (testForAchievements == 14) {
        statusAchievements("achievements15");
    }
    testForAchievements = 0;
}

//Открыть достижения
function open_achievements() {
    document.getElementById("achievements").style.display = "block";
}

// Сохранение результатов игры
function save_game() {
    save_info = [money, allMoneyLvl, salary, salaryInSec,moneyInBank,allMoney,allMoneyForFlats,allMoneyForCars,
                 allMoneyForTech,allMoneyForObjects,flats,cars,tech,objects,
                 testForSituation,testForAchievements];
    localStorage.setItem('save_game', save_info);
}

// Загрузка результатов игры
function load_game() {
    game_load = (localStorage.getItem('save_game')).split(',');
    money = Number(game_load[0]);
    allMoneyLvl = Number(game_load[1]);
    salary = Number(game_load[2]);
    salaryInSec = Number(game_load[3]);
    moneyInBank = Number(game_load[4]);
    allMoney = Number(game_load[5]);
    allMoneyForFlats = Number(game_load[6]);
    allMoneyForCars = Number(game_load[7]);
    allMoneyForTech = Number(game_load[8]);
    allMoneyForObjects = Number(game_load[9]);
    flats = Number(game_load[10]);
    cars = Number(game_load[11]);
    tech = Number(game_load[12]);
    objects = Number(game_load[13]);
    testForSituation = Boolean(game_load[14]);
    testForAchievements = Number(game_load[15]);
    exit("training");
    close_menu();
}

// Закрытие меню
function close_menu() {
    document.getElementById("menu").style.display = "none";
}

// Открыть меню
function open_menu() {
    document.getElementById("menu").style.display = "block";
    if_have_save();
    save_game();
}

// Если есть сохранение - уведомление при создании новой игры
function if_have_save() {
    if (localStorage.getItem('save_game') == null) {
        document.getElementById('load_game').disabled = true;
    } else {
        document.getElementById('load_game').disabled = false;
    }
}

// Проверка больше ли денег чем 100$ в банке
function money_in_bank() {
    if (moneyInBank > 100) {
        document.getElementById('percent_in_bank').style.display = 'block';
    } else {
        document.getElementById('percent_in_bank').style.display = 'none';
    }
}

// Процент банка
function percent_in_bank() {
    if (moneyInBank > 100) {
        percent = Math.floor(moneyInBank / 100);
        moneyInBank = moneyInBank - percent;
    }
}

// Спросить хочет ли игрок начать новую игру
function if_new_game() {
    if (localStorage.getItem('save_game') != null ) {
        document.getElementById('new_game').style.display = 'block';
    }
}

// Закрыть запрос о новой игре
function close_new_game() {
    document.getElementById('save_game').style.display = 'none';
}




//Функции которые повторяются
setInterval(moneyText, 300);
setInterval(moneyInSec, 1000);
setInterval(lvl, 1000)
setInterval(random, 1000);
setInterval(achievements, 1000);
setInterval(money_in_bank, 1000);
setInterval(percent_in_bank, 60000);
setInterval(save_game, 60000)