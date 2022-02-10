const isOddEven = function (number) {
    if (number % 2 == 0) return 'Even'
    else return 'Odd'
}

const isOddEvenObject = function (userArray) {
    constructor = {}
    for (let i = 0; i < userArray.length; i++) {
        constructor[userArray[i]] = isOddEven(userArray[i])
    }
    return constructor
}
