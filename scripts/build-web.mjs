// Збирає веб-частину в папку www: JS для нативних плагінів + сам застосунок.
import { build } from 'esbuild';
import { mkdirSync, copyFileSync } from 'node:fs';

mkdirSync('www', { recursive: true });
await build({
  entryPoints: ['src/native.js'],
  bundle: true,
  format: 'iife',
  outfile: 'www/native.js',
  minify: true,
  target: 'es2020',
});
copyFileSync('src/index.html', 'www/index.html');
console.log('Веб-частину зібрано у www/');
