#!/usr/bin/node
let fs = require('fs');
let textA = fs.readFileSync(fileA, 'utf8');
let textB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, textA + textB);
