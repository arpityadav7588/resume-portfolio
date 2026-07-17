const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const outputDir = path.join(__dirname, '..', 'assets', 'img');
if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

const images = [
  {
    input: path.join(__dirname, '..', 'assets', 'c7774d6e-8c96-4dde-9e49-d24064189762.png'),
    baseName: 'profile',
    sizes: [400, 800, 1200],
    quality: 80,
  },
  {
    input: path.join(__dirname, '..', 'assets', 'image.png'),
    baseName: 'career-ai',
    sizes: [400, 800],
    quality: 78,
  },
  {
    input: path.join(__dirname, '..', 'assets', 'Screenshot 2026-03-15 211236.png'),
    baseName: 'mobile-service',
    sizes: [400, 800],
    quality: 78,
  },
  {
    input: path.join(__dirname, '..', 'assets', 'Screenshot 2026-03-19 084814.png'),
    baseName: 'ets2-launcher',
    sizes: [400, 800],
    quality: 78,
  },
];

async function processImages() {
  for (const img of images) {
    const metadata = await sharp(img.input).metadata();
    console.log(`\nProcessing: ${path.basename(img.input)} (${metadata.width}x${metadata.height})`);

    for (const w of img.sizes) {
      const outPath = path.join(outputDir, `${img.baseName}-${w}w.webp`);
      await sharp(img.input)
        .resize(w, null, { withoutEnlargement: true })
        .webp({ quality: img.quality, effort: 6 })
        .toFile(outPath);
      const stat = fs.statSync(outPath);
      console.log(`  -> ${img.baseName}-${w}w.webp  (${(stat.size / 1024).toFixed(1)} KB)`);
    }
  }
  console.log('\nDone! All images optimized.');
}

processImages().catch(console.error);
