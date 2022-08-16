#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] == null) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
