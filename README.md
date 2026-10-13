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

Because the site is a self-contained, static single-page document, you do not need any build tool, Node.js, or complex environment.

### Option 1: Open Directly in a Browser
Double-click `index.html` or open it in any modern browser:
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

## Typography & System Fonts

To protect user privacy, guarantee instant rendering on 2G/weak connections, and avoid external network requests or heavy assets, the site uses native, privacy-first system fonts:
- **Body & Content**: `system-ui, "Segoe UI", "Noto Sans Devanagari", "Nirmala UI", sans-serif`
- **Headings & Slogans**: `Georgia, "Noto Serif Devanagari", "Nirmala UI", serif`

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
