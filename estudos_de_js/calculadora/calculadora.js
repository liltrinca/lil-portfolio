const soma = (a, b) => a + b
const subtracao = (a, b) => a - b 
const multiplicacao = (a , b) => a * b
const divisao = (a , b) => a / b

const calcLabel = document.getElementById("calcLabel")

const clickedButton = function (buttonId) {
    calcLabel.innerHTML += `${buttonId}`
}

