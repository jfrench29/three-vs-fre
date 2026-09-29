# 3 vs. Fre

An affectionate golf roast. Static HTML, CSS, and JavaScript; no paid hosting, database, or build required. The public website is in `site/`. Originals remain local and ignored by Git. Web images are resized and exported without original EXIF metadata.

## Preview and edit

Run `python3 -m http.server 4173 --directory site` and open http://localhost:4173.
Edit `site/index.html` for text and photos, `site/styles.css` for appearance, and `site/script.js` for committee rulings. Push to main to publish through GitHub Actions.

The page deliberately avoids invented scores, named photo identifications, and a fabricated win count. Photo captions are comic commentary, not quotes from Jason.

## Domain setup in Squarespace

GitHub account: `jfrench29`. Repository: `three-vs-fre`.
Set the custom domain to `fredesucksatgolf.com` in repository Settings → Pages **before** changing DNS. Domain verification via GitHub Settings → Pages is recommended; copy the account-specific TXT record GitHub provides if verifying.

In Squarespace's domain DNS settings, replace conflicting website records for `@` and `www` with:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | jfrench29.github.io |

Preserve unrelated MX/TXT records (including email and verification records). Remove conflicting parking/forwarding records and obsolete AAAA records for the website hosts. DNS and certificate provisioning can take up to 24 hours. Enable Enforce HTTPS in GitHub Pages once available. Test both the apex and www domains before printing.

Source: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## QR artwork

`print/frede-qr.svg` is the vector master; `print/frede-qr.png` is the raster version. Both encode `https://fredesucksatgolf.com`, with error correction Q and four modules of white quiet zone. No subscription or QR service is involved.

Send the SVG to the ball printer. Keep it black on opaque white, square, undistorted, with the white border intact. Do not overlay a face/logo or wrap text into the quiet zone. Ask the printer to recommend a scannable size for its process and provide a physical sample. Test several phones on the actual ball under normal lighting before a full order. A successful digital decode does not establish that a small curved print will scan. If the print area is too small, put the QR on a towel tag, ball sleeve, or bag tag and use “3 vs. Fre” on the ball.

Optional image regeneration uses Pillow, pillow-heif, and qrcode: `python scripts/prepare_assets.py` (requires the original local photos).

## Ideas for next year's offenses

- **The Frede Defense Fund:** a clearly fake campaign whose only goal is buying him two teammates. No payment collection.
- **Official excuses bingo:** wind, greens, format, equipment, committee interference.
- **A protest towel:** “My complaint was denied 3–1.”
- **A trophy plaque:** “Excellence Through Numerical Superiority.”
- **A ball sleeve:** “If found, please return to the winning team. There are three of us.”
- **A real rivalry ledger:** actual year, course, format, result, score, and one quote per match once supplied.
- **A ceremonial fairness slider:** moving it toward “fair” makes the committee reject the change.
- **An annual press conference:** a short real clip of the crew explaining how hard it is to beat one man with three men.

Alternative visual directions: a courtroom evidence locker (“The People vs. Frede”), or a wildly self-important sports network (“FreSPN”). This version uses an old-fashioned championship aesthetic.
