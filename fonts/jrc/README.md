# JRC Typography — drop-in folder

This folder hosts the **J.R. Company** local typography system.
The site looks for **3 font roles**, defined as CSS variables in
`typography.css`:

| Role            | CSS variable        | Used for                                            |
|-----------------|---------------------|-----------------------------------------------------|
| **Display**     | `--font-display`    | Hero titles, section titles, card titles, big H1/H2 |
| **Body**        | `--font-body`       | Paragraphs, descriptions, navigation, button text   |
| **Technical**   | `--font-technical`  | Eyebrows, badges, small uppercase labels            |

## How to install the fonts

1. **Copy your font files into THIS folder** (`fonts/jrc/`).
2. Prefer `.woff2`. If you only have `.ttf` / `.otf`, that's fine.
3. **Rename** the files (or update `typography.css`) so they match the
   expected names below. Renaming is the fastest path because then no
   CSS edit is needed.

### Expected file names (Phase 1 placeholders)

Drop these exact file names in here and the site will pick them up
automatically:

```
fonts/jrc/
  ├── jrc-display.woff2     ← bold / condensed industrial face (700–900)
  ├── jrc-body.woff2        ← clean readable sans (300–500)
  └── jrc-technical.woff2   ← uppercase technical / mono-ish (500–700)
```

You can also drop `.ttf` / `.otf` versions with the same base name —
the CSS already lists every common format as a fallback.

### If your fonts have multiple weight files

If you have separate files per weight (e.g. `Display-Bold.woff2`,
`Display-Black.woff2`, `Body-Regular.woff2`, `Body-Light.woff2`),
**just paste them all here and tell me the file names.** I'll update
`typography.css` to register each weight individually so the browser
picks the closest match.

## Phase 2 — after you paste the fonts

Tell me:

1. The exact file names you pasted
2. Which file is **display** (bold/condensed)
3. Which file is **body** (clean / readable)
4. Which file is **technical** (if you have a third one — optional)

I'll re-read the folder and rewrite the `@font-face` block with the
real file names and proper weight ranges.

## Why this approach

- Keeps the website's existing layout, spacing, colors and components
  completely untouched.
- Re-maps the legacy `'Vazirmatn'` family used in inline styles to the
  local fonts, so old declarations keep working with the new look.
- Single source of truth: every page links to one file
  (`fonts/jrc/typography.css`).
- No Windows-specific paths in production CSS — only relative URLs.
