// Function
/*
// 선언식
function add (num1, num2) {
  return num1 + num2
}

console.log(add(2, 7))

// 표현식
const sub = function(num1, num2) {
  return num1 - num2
}

console.log(sub(7, 2))

// JS에서는 함수도 하나의 값
console.log(typeof add) // function
console.log(typeof sub) // function


// Arrow Function (화살표 함수)
// why arrow function?
// 화살표 함수는 항상 익명 함수
// 1. function keyword 생략 가능
// 2. 함수 매개변수가 1개라면 () 생략 가능
// 3. 함수 바디의 표현식이 하나라면 {}와 return 생략 가능

// 함수 표현식
const ssafy1 = function() {
  return 'Hello!'
}
console.log(ssafy1())

// 화살표 함수로 바꿔보기!
// 1. function 키워드를 삭제할 수 있음!
const ssafy1 = (name) => { return `Hello! ${name}`}
console.log(ssafy1('hyeyoung'))

// 2. () 생략 할 수 있다.(인자가 1개 있을 때)
const ssafy1 = name => { return `Hello! ${name}`}
console.log(ssafy1('hyeyoung'))

// 3. {}와 return 생략
const ssafy1 = name => `Hello ${name}`
console.log(ssafy1('hyeyoung'))


// 예제
let square = function(num) {
  return num ** 2
}


// 1. function 키워드 삭제
let square = (num) => { return num ** 2}
console.log(square(2))

// 2. () 생략 할 수 있다.(인자가 1개 있을 때)
let square = num => { return num ** 2}
console.log(square(2))


// 3. {}와 return 생략
let square = num => num ** 2
console.log(square(2))


// 4. 인자가 없을 때 -> (), _로 표현 가능
let noArgs = () => 'No Args'
console.log(noArgs())

noArgs = _ => 'No'
console.log(noArgs())


// 5-1. object를 리턴하려고 한다면? -> return을 명시한다.
let returnObject = () => { return {key: 'value'}}
console.log(returnObject())
console.log(typeof returnObject()) //object

// 5-2. return을 적지않고 object를 return 하고 싶다면 ()를 활용
returnObject = () => ({key: 'value'})
console.log(returnObject())
console.log(typeof returnObject()) //object

// 5-3. return 문을 적지 않았을때
returnObject = () => {key: 'value'}
console.log(returnObject()) // undefined
console.log(typeof returnObject()) // undefined

// 기본 인자(default args)

// 기본 인자를 줄 때는 인자 개수와 상관없이 괄호를 꼭 해야한다.
// 괄호가 없으면 syntax errer 발생
const sayHello = (name='noName') => `hi ${name}`

console.log(sayHello('hy'))
console.log(sayHello())


// 익명 함수/1회용 함수
// 즉시 실행 함수는 초기화에 많이 사용된다.

// function (num) { return num ** 3 }

// 1. 익명함수 -> 변수에 담아 사용(표현식)
const cube = function (num) { return num ** 3 }
const squareRoot = num => num ** 0.5

console.log(cube(3))
console.log(squareRoot(3))

// 2. 즉시실행함수 -> 주로, 초기화에 많이 사용 된다.
console.log((function (num) { return num ** 3})(2)) // 8
console.log((num => num ** 0.5)(4)) // 2


// 함수 호이스팅

ssafy()

function ssafy() {
  console.log('hoisting!')
}

///////////let으로 선언/////////////////

ssafy2()

let ssafy2 = function () {
  console.log('hoisting!')
}

// JS 엔진이 코드를 해석하는 과정
// 1. 변수 선언 -> let은 var와 달리 초기화가 동시에 진행되지 않음
let ssafy2
// 2. 함수 호출 -> ssafy2가 초기화가 안됨
ssafy2() 
// 3. 변수에 할당
ssafy2 = function() {
  console.log('hoisting!')
}

////////////var로 선언////////////////

ssafy3()

var ssafy3 = function() {
  console.log('hoisting!')
}

// JS 엔진이 코드를 해석하는 과정
// 1. 변수 호이스팅. 선언과 초기화가 동시에 일어남
var ssafy3
// 2. 함수 호출 -> let과 달리 초기값 undefined가 들어감. 
// 함수를 호출하는 시점에서 ssafy3에 함수가 담겨있지 않고 undefined가 들어 있어서
ssafy3()
// 3. 함수가 아니라는 typeerror 메세지를 보냄
ssafy3 = function() {
  console.log('hoisting!')
}
*/