#!/usr/bin/node
let fs = require('fs');
const fs = require('fs');
const A = fs.readFileSync(process.argv[2], 'utf8');
const B = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], A + B);
