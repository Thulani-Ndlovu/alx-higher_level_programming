#!/usr/bin/node
exports.converter = function (base) {
  if (base < 2 || base > 36) {
    return;
  }

  return function (number) {
    if (number < 0) {
      return;
    }

    if (number === 0) {
      return '0';
    }

    return (function convertToBase (number) {
      if (number < base) {
        return (number < 10 ? number.toString() : String.fromCharCode(65 + number - 10));
      }
      return convertToBase(Math.floor(number / base)) + convertToBase(number % base);
    })(number);
  };
};
