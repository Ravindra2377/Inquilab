# Inquilab Zindabad

An independent, static, bilingual (English & Hindi) civic reference on India's Constitution, rights and safety during peaceful protest, custody procedures, landmark Supreme Court rulings, and voter registration.

---

## What This Site Is

- **Constitutional Rights Reference**: Plain-language summaries of fundamental rights under Articles 14, 19, 20(3), 21, 22, 32/226, 324–326, and fundamental duties under Article 51A.
- **Peaceful Protest Guide**: Lawful preparation, on-ground conduct, and legal boundaries (e.g., Section 163 BNSS / earlier Section 144 CrPC, public order limits).
- **Detention & Custody Checklist**: Step-by-step procedural safeguards under Article 22 and Supreme Court precedents (such as *D.K. Basu*), printable as a pocket card.
- **Voter Registration & Form 6 Guide**: How to check your status on the electoral roll, how to register via Form 6, ECI qualifying dates, and context regarding the Special Intensive Revision (SIR).
- **Privacy-First & Self-Contained**: No cookies, no analytics, no external tracking, no third-party CDNs, and zero third-party network requests.

---

## Disclaimer

> **Educational information only, not legal advice.**
> Laws, judicial interpretations, administrative procedures, and statutory forms change over time. Readers should independently verify all legal provisions, form requirements, dates, and helpline numbers with official sources, legal aid authorities (such as NALSA), or qualified legal practitioners before taking action.

Official constitutional texts can be accessed at [legislative.gov.in](https://legislative.gov.in/constitution-of-india/).
Official electoral services and schedules are published at [voters.eci.gov.in](https://voters.eci.gov.in/).

---

## How to Run Locally

Because the site is a static single-page document with self-hosted assets, you do not need any build tool, Node.js, or complex environment.

### Option 1: Open Directly in a Browser
Double-click `index.html` (or `inquilab-constitution.html`) or open it in any modern browser:
```bash
# On Linux
xdg-open index.html

# On macOS
open index.html

# On Windows
start index.html
```

### Option 2: Serve via a Local Web Server
If you prefer testing over HTTP:
```bash
python3 -m http.server 8000
```
Then navigate to `http://localhost:8000` in your browser.

---

## Typography & Self-Hosted Fonts

To protect user privacy and avoid third-party tracking, all Google Fonts requests have been removed. The site is configured to load fonts locally from the `fonts/` directory with `font-display: swap`:

### Required Font Files
The following `.woff2` files should reside in the `fonts/` directory:

| Filename | Family | Weight | Subset |
| :--- | :--- | :--- | :--- |
| `mukta-400-devanagari.woff2` | Mukta | 400 (Regular) | Devanagari |
| `mukta-400-latin-ext.woff2` | Mukta | 400 (Regular) | Latin Extended |
| `mukta-400-latin.woff2` | Mukta | 400 (Regular) | Latin |
| `mukta-600-devanagari.woff2` | Mukta | 600 (SemiBold) | Devanagari |
| `mukta-600-latin-ext.woff2` | Mukta | 600 (SemiBold) | Latin Extended |
| `mukta-600-latin.woff2` | Mukta | 600 (SemiBold) | Latin |
| `mukta-800-devanagari.woff2` | Mukta | 800 (ExtraBold) | Devanagari |
| `mukta-800-latin-ext.woff2` | Mukta | 800 (ExtraBold) | Latin Extended |
| `mukta-800-latin.woff2` | Mukta | 800 (ExtraBold) | Latin |
| `yatra-one-400-devanagari.woff2` | Yatra One | 400 (Regular) | Devanagari |
| `yatra-one-400-latin-ext.woff2` | Yatra One | 400 (Regular) | Latin Extended |
| `yatra-one-400-latin.woff2` | Yatra One | 400 (Regular) | Latin |

### Fallback Font Stack
If local font files are unavailable, the CSS falls back to system fonts:
- **Body & Content**: `system-ui, "Noto Sans Devanagari", "Segoe UI", sans-serif`
- **Headings & Slogans**: `Georgia, serif`

---

## Contributing Corrections

Corrections, factual updates, and improvements to legal citations are welcomed.

When submitting an issue or pull request:
1. **Provide an official source link**: Reference official gazettes, Supreme Court / High Court judgment texts, ECI notifications, or government statutes.
2. **Keep wording neutral and factual**: Avoid partisan claims, speculative numbers, or editorial commentary.
3. **Maintain privacy standards**: Do not introduce third-party trackers, scripts, CDNs, or external requests.
4. **Preserve bilingual parity**: Ensure that corresponding English and Hindi translations are provided for all content additions.

---

## License

This project is dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. See the [LICENSE](LICENSE) file for details.
