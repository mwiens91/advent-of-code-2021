#!/usr/bin/env node

// Read input
const fs = require("fs");
const input = fs
  .readFileSync("input.txt", "utf8")
  .split(/\n/)
  .filter((x) => x);

// Cast to integer
const depths = input.map((x) => parseInt(x));

// Find the number of increases
let count = 0;

depths.forEach((x, i) => {
  if (i >= 3) {
    count += depths[i] - depths[i - 3] > 0 ? 1 : 0;
  }
});

// Print result
console.log(count);
