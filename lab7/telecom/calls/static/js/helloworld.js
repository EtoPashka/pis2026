var groupmates = [
    {
        "name": "Павел",
        "surname": "Османов",
        "group": "БСТ2354",
        "marks": [5, 5, 4]
    },
    {
        "name": "Андрей",
        "surname": "Замахаев",
        "group": "БСТ2351",
        "marks": [3, 5, 5]
    },
    {
        "name": "Илана",
        "surname": "Гагкоева",
        "group": "БСТ2353",
        "marks": [5, 4, 4]
    },
    {
        "name": "Дмитрий",
        "surname": "Бочкарев",
        "group": "БСТ2356",
        "marks": [3, 4, 3]
    },
    {
        "name": "Малинин",
        "surname": "Александр",
        "group": "БСТ2354",
        "marks": [5, 3, 5]
    },
    {
        "name": "Игнатенко",
        "surname": "Александр",
        "group": "БСТ2352",
        "marks": [4, 4, 4]
    }
]

console.log(groupmates);

var rpad = function(str, length) {
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет
    str = str.toString(); // преобразование в строку
    while (str.length < length) {
        str = str + ' '; // добавление пробела в конец строки
    }
    return str; // когда все пробелы добавлены, возвратить строку
};

var printStudents = function(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 10),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i < students.length; i++) {
        // в цикле выводится каждый экземпляр студента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 10),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};

var filterByGroup = function(students) {
    var targetGroup = prompt("Введите группу для фильтрации (например, БСТ1234):");
    // для удаления лишних пробельных символов используется метод trim()
    if (targetGroup === null || targetGroup.trim() === "") {
        console.log("Группа не задана, фильтрация по группе отменена.\n");
        return students;
    }
    var filtered = [];
    var normalizedGroup = targetGroup.trim().toLowerCase();
    for (var i = 0; i < students.length; i++) {
        if (students[i]['group'].toLowerCase() === normalizedGroup) {
            filtered.push(students[i]);
        }
    }
    console.log("Произведена фильтрация по группе " + targetGroup.trim() + ".\n");
    return filtered;
};

var getAverageMark = function(marks) {
    if (!marks || marks.length === 0) {
        return 0;
    }
    var sum = 0;
    for (var i = 0; i < marks.length; i++) {
        sum += marks[i];
    }
    return sum / marks.length;
};

var filterByAverageMark = function(students) {
    var input = prompt("Введите минимальный средний балл (например, 4.2):");
    if (input === null || input.trim() === "") {
        console.log("Средний балл не задан, фильтрация отменена.\n");
        return students;
    }
    var minAvg = parseFloat(input.replace(',', '.'));
    if (isNaN(minAvg)) {
        console.log("Введено некорректное число.\n");
        return students;
    }
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        if (getAverageMark(students[i]['marks']) > minAvg) {
            filtered.push(students[i]);
        }
    }
    console.log("Произведена фильтрация по среднему баллу выше " + minAvg + ".\n");
    return filtered;
};

printStudents(filterByAverageMark(groupmates)); 

