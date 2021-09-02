function convertToRoman(num) {
  var roman = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1,
  };
  console.log("num = " + num);

  let str = "";

  for (var i in roman) {
    console.log("*");
    while (num >= roman[i]) {
      str += i;
      num -= roman[i];
      console.log(str);
    }
  }
  return str;
}

convertToRoman(999);
