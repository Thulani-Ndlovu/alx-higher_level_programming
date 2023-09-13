#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (base < 2 || base > 36 || number < 0) {
      return;
    }

    if (number === 0) {
      return '0';
    }

    let result = '';
    while (number > 0) {
      const remainder = number % base;
      if (remainder < 10) {
        result = remainder + result;
      } else {
        result = String.fromCharCode(65 + remainder - 10) + result;
      }
      number = Math.floor(number / base);
    }

    return result;
  };
};
