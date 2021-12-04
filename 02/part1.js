#!/usr/bin/env node

// Read input
const fs = require("fs");
const input = fs
  .readFileSync("input.txt", "utf8")
  .split(/\n/)
  .filter((x) => x);

// Split the lines and cast second index to integer
const data = input
  .map((x) => x.split(/\s/))
  .map(([x1, x2]) => [x1, parseInt(x2)]);

// Find final positions
let depthCount = 0;
let forwardCount = 0;

data.forEach(([instruction, num]) => {
  if (instruction === "forward") {
    forwardCount += num;
  } else {
    depthCount += (instruction === "down" ? 1 : -1) * num;
  }
});

// Print result
console.log(depthCount * forwardCount);
