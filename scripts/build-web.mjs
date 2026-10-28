// Збирає веб-частину в папку www: нативні плагіни + застосунок
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
  external: ['@capacitor/*'],
});
copyFileSync('src/index.html', 'www/index.html');
try { copyFileSync('src/styles.css', 'www/style.css'); } catch(e) {}
console.log('Веб-частину зібрано у www/');
