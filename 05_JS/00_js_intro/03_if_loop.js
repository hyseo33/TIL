// If문
// switch
/*
const fruit = 'papayas'

switch (fruit) {
  case 'oranges':
    console.log('oranges are 2000...won')
    break
  case 'mangoes':
    console.log('mangoes are $4000')
    break
  case 'papayas':
    console.log('papayas are 500won')
    // break
  default:
    console.log('sorry, we are out of ' + fruit + '.')
}


// 반복문

// while loop
let i = 0

while (i < 6) {
  console.log(i)
  i++
}

// for loop
// for 문 내에서 사용하는 변수 j가 false가 되면 반복 중지

for (let j = 0; j < 6; j++) {
  console.log(j)
}
*/

// for of

const numbers = [0, 1, 2, 3, 4, 5]

// let - 재할당 있음
for (let number of numbers) {
  console.log(number)
}

for (let number of [0, 1, 2, 3, 4, 5]) {
  console.log(number)
}
// const - 재할당 없음
for (const number of [0, 1, 2, 3, 4, 5]) {
  console.log(number)
}