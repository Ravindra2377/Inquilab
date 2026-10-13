#!/usr/bin/env python3
"""Applies the agreed fixes to inquilab-constitution.html.
Usage:  python apply_fixes.py [path/to/inquilab-constitution.html]
A backup (.bak) is saved first. Each fix reports APPLIED or NOT FOUND."""
import sys, shutil, os

path = sys.argv[1] if len(sys.argv) > 1 else "inquilab-constitution.html"
shutil.copy(path, path + ".bak")
with open(path, encoding="utf-8", newline="") as f:
    s = f.read()

FIXES = [
# 1. SIR definition
("SIR definition card",
'''["SIR and your roll","SIR और आपकी सूची","The Summary of the Integrated Rolls (SIR) is a routine update, not a re-registration drive. If your name was dropped, applying via Form 6 is the fastest fix.","SIR (समेकित मतदाता सूची का सारांश) एक नियमित अपडेट है, पुनः-पंजीकरण अभियान नहीं। नाम हटा हो तो फ़ॉर्म 6 सबसे तेज़ उपाय है।"]''',
'''["What SIR means","SIR का मतलब","SIR stands for Special Intensive Revision, a more intensive exercise than the routine yearly revision of the rolls. Its schedule and phases differ by state, so check your state's notices on the official ECI site. If your name is missing or wrong, apply with Form 6 or correct it with Form 8, keep your reference number, and note your state's deadline for claims and objections.","SIR का पूरा नाम Special Intensive Revision (विशेष गहन पुनरीक्षण) है, जो मतदाता सूची के नियमित वार्षिक पुनरीक्षण से अधिक गहन प्रक्रिया है। इसका कार्यक्रम राज्य के अनुसार अलग होता है, इसलिए ECI की आधिकारिक साइट पर अपने राज्य की सूचनाएँ देखें। नाम न हो या गलत हो तो फ़ॉर्म 6 से आवेदन करें या फ़ॉर्म 8 से सुधार कराएँ, संदर्भ संख्या रखें और अपने राज्य में दावे-आपत्ति की अंतिम तिथि नोट करें।"]'''),

("Voter section intro",
'''<p class="sub" data-h="चुनाव आयोग ने SIR के बाद नई सूचियाँ बनाई हैं। जाँचें कि आपका नाम है या नहीं, और नहीं है तो नीचे के चरणों से जुड़ें।">After the SIR exercise, the Election Commission has prepared updated rolls. Check whether your name is on the list, and if not, follow the steps below to register.</p>''',
'''<p class="sub" data-h="आपके राज्य में SIR (विशेष गहन पुनरीक्षण) जारी हो सकता है या पूरा हो चुका हो सकता है। जाँचें कि आपका नाम सूची में है या नहीं, और नहीं है तो नीचे के चरणों का पालन करें।">Depending on your state, the SIR (Special Intensive Revision) may be ongoing or completed. Check whether your name is on the list, and if not, follow the steps below.</p>'''),

("Not found? (English)",
'''<b>Not found?</b> Don't panic. Your name may have been dropped during the SIR update. Apply fresh using Form 6 (see below).''',
'''<b>Not found?</b> Don't panic. Your name may be missing for several reasons, including a revision exercise in your state. Check your state's claims-and-objections deadline, then apply with Form 6 (see below).'''),

("Not found? (Hindi)",
'''<b>नहीं मिला?</b> घबराएँ नहीं। SIR अपडेट में नाम हट सकता है। फ़ॉर्म 6 से नया आवेदन करें (नीचे देखें)।''',
'''<b>नहीं मिला?</b> घबराएँ नहीं। नाम कई कारणों से छूट सकता है, जिनमें आपके राज्य में चल रहा पुनरीक्षण भी शामिल है। अपने राज्य में दावे-आपत्ति की अंतिम तिथि देखें, फिर फ़ॉर्म 6 से आवेदन करें (नीचे देखें)।'''),

# 2. Voting ID wording
("Voting ID card",
'''["No ID needed to vote","वोट देने के लिए EPIC ज़रूरी नहीं","You can vote with 12 other IDs including Aadhaar, passport, MNREGA card and PAN.","आप आधार, पासपोर्ट, मनरेगा कार्ड और पैन सहित 12 अन्य पहचान पत्रों से भी वोट दे सकते हैं।"]''',
'''["EPIC isn't the only accepted ID","वोट के लिए सिर्फ़ EPIC ही मान्य नहीं","You must be on the electoral roll. If you don't have your EPIC, you can show another photo ID approved by the ECI, such as Aadhaar, passport, driving licence, PAN card or MGNREGA job card. Check the full, current list on the ECI site.","आपका नाम मतदाता सूची में होना ज़रूरी है। EPIC न हो तो आप ECI द्वारा मान्य कोई अन्य फ़ोटो पहचान पत्र दिखा सकते हैं, जैसे आधार, पासपोर्ट, ड्राइविंग लाइसेंस, पैन कार्ड या मनरेगा जॉब कार्ड। पूरी और नवीनतम सूची ECI साइट पर देखें।"]'''),

# 3. Qualifying dates
("Who can apply (English)",
'''<b>Who can apply</b> Any Indian citizen who is 18 or older on the qualifying date (1 January of the current year) and is ordinarily resident at the address.''',
'''<b>Who can apply</b> Any Indian citizen who turns 18 on or before a qualifying date and is ordinarily resident at the address. The ECI now has four qualifying dates each year (1 January, 1 April, 1 July, 1 October), and you can apply in advance from age 17. Check the ECI site for current rules.'''),

("Who can apply (Hindi)",
'''<b>कौन आवेदन कर सकता है</b> कोई भी भारतीय नागरिक जो अर्हता तिथि (चालू वर्ष की 1 जनवरी) को 18 वर्ष या अधिक हो और उस पते पर सामान्यतः निवास करता हो।''',
'''<b>कौन आवेदन कर सकता है</b> कोई भी भारतीय नागरिक जो किसी अर्हता तिथि तक 18 वर्ष का हो जाए और उस पते पर सामान्यतः निवास करता हो। ECI की अब साल में चार अर्हता तिथियाँ हैं (1 जनवरी, 1 अप्रैल, 1 जुलाई, 1 अक्टूबर) और 17 वर्ष की आयु से अग्रिम आवेदन किया जा सकता है। वर्तमान नियम ECI साइट पर देखें।'''),

# 4. Form 6 documents
("Offline photos (English)",
'''fill it, attach two passport photos and self-attested copies of the proofs, and submit''',
'''fill it, attach a recent passport-size photo and copies of the documents listed on the current form, and submit'''),

("Offline photos (Hindi)",
'''भरें, दो पासपोर्ट फ़ोटो और प्रमाण-पत्रों की स्व-सत्यापित प्रतियाँ लगाएँ, और''',
'''भरें, हाल की पासपोर्ट-साइज़ फ़ोटो और वर्तमान फ़ॉर्म में बताए दस्तावेज़ों की प्रतियाँ लगाएँ, और'''),

("Online proofs (English)",
'''Upload a passport-size photo, age proof (birth certificate''',
'''Upload a passport-size photo, age proof as listed on the current Form 6 (birth certificate'''),

("Online proofs (Hindi)",
'''पासपोर्ट-साइज़ फ़ोटो, आयु प्रमाण (जन्म प्रमाण पत्र''',
'''पासपोर्ट-साइज़ फ़ोटो, आयु प्रमाण (वर्तमान फ़ॉर्म 6 में बताए अनुसार; जैसे जन्म प्रमाण पत्र'''),

# 5. Hindi typo (all occurrences)
("Hindi typo",
'''अनुपातिक''', '''आनुपातिक'''),

# 6. ECI link in Hindi mode
("Hindi voter note link",
'''data-h="निर्वाचन आयोग की आधिकारिक वेबसाइट: voters.eci.gov.in — ऑनलाइन और ऑफ़लाइन दोनों तरीके मान्य हैं।"''',
'''data-h="निर्वाचन आयोग की आधिकारिक वेबसाइट: <a href='https://voters.eci.gov.in/' target='_blank' rel='noopener'>voters.eci.gov.in</a> — ऑनलाइन और ऑफ़लाइन दोनों तरीके मान्य हैं।"'''),

# 7. Remove Google Fonts, use system fonts
("Remove Google Fonts link",
'''<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mukta:wght@400;600;800&family=Yatra+One&display=swap">''', ''''''),

("Body font",
'''font:400 17px/1.6 Mukta,"Noto Sans Devanagari",system-ui,sans-serif''',
'''font:400 17px/1.6 system-ui,"Segoe UI","Noto Sans Devanagari","Nirmala UI",sans-serif'''),

("Heading font",
'''font-family:"Yatra One",serif''',
'''font-family:Georgia,"Noto Serif Devanagari","Nirmala UI",serif'''),

("Button/label fonts",
'''Mukta,sans-serif''',
'''system-ui,"Noto Sans Devanagari","Nirmala UI",sans-serif'''),

# 8. Share-preview meta tags
("Open Graph tags",
'''<title>Inquilab Zindabad – Know your Constitution, protest peacefully</title>''',
'''<title>Inquilab Zindabad – Know your Constitution, protest peacefully</title>
<meta property="og:type" content="website">
<meta property="og:title" content="Inquilab Zindabad – Know your Constitution, protest peacefully">
<meta property="og:description" content="Your fundamental rights, the rules of peaceful protest, voter registration guide, and what to do if detained, in plain language, in English and Hindi.">
<meta property="og:locale" content="en_IN">
<!-- Add after hosting: <meta property="og:url" content="https://YOUR-SITE-URL/"> and <meta property="og:image" content="https://YOUR-SITE-URL/preview.png"> -->
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0d1b4c">'''),

# 9. Honest claims about identity
("About subtitle",
'''<p class="sub" data-h="यह एक स्वतंत्र, गुमनाम नागरिक पहल है।">An independent, anonymous citizen initiative.</p>''',
'''<p class="sub" data-h="यह एक स्वतंत्र नागरिक पहल है।">An independent citizen initiative.</p>'''),

("Anonymous card",
'''["Anonymous by design","गुमनाम, जान-बूझकर","The creators of this page do not identify themselves, because the message matters more than the messenger. This keeps the focus on the Constitution, not on any individual.","इस पेज के रचनाकार अपनी पहचान नहीं बताते, क्योंकि संदेश, संदेशवाहक से ज़्यादा महत्वपूर्ण है। इससे ध्यान संविधान पर रहता है, किसी व्यक्ति पर नहीं।"]''',
'''["No names on the page","पेज पर कोई नाम नहीं","The creators choose not to publish their names, because the message matters more than the messenger. This keeps the focus on the Constitution, not on any individual.","रचनाकार अपने नाम प्रकाशित न करने का विकल्प चुनते हैं, क्योंकि संदेश, संदेशवाहक से ज़्यादा महत्वपूर्ण है। इससे ध्यान संविधान पर रहता है, किसी व्यक्ति पर नहीं।"]'''),
]

ok = 0
for name, old, new in FIXES:
    n = s.count(old)
    if n:
        s = s.replace(old, new)
        print("APPLIED   (%d)  %s" % (n, name))
        ok += 1
    else:
        print("NOT FOUND       %s  <- check this one by hand" % name)

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)

readme = os.path.join(os.path.dirname(os.path.abspath(path)), "README.md")
if not os.path.exists(readme):
    with open(readme, "w", encoding="utf-8") as f:
        f.write("""# Inquilab Zindabad: Know your Constitution

A free, bilingual (English/Hindi) civic guide to India's fundamental rights, the rules of peaceful protest, what to do if detained, and how to check or register on the electoral roll.

**Educational information, not legal advice.** Laws, forms, dates and helpline numbers change. Always confirm with official sources (legislative.gov.in, voters.eci.gov.in) or a lawyer.

## Run it
Open `inquilab-constitution.html` in any browser. No build step, no tracking, no external requests.

## Contribute corrections
Open an issue or pull request. Please include a link to an official source for every factual change.
""")
    print("CREATED   README.md")

print("\nDone: %d of %d fixes applied. Backup saved as %s.bak" % (ok, len(FIXES), path))
