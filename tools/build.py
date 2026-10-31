import os, shutil, html
from PIL import Image, ImageDraw, ImageFont
SRC=os.path.expanduser('~/Developer/folvane'); OUT=os.path.expanduser('~/Developer/folvane-site')
BASE='https://minh.systems/Folvane/'
STORE='https://apps.microsoft.com/detail/9NSDC58HLFRR'
for d in ('img','de'): os.makedirs(f'{OUT}/{d}',exist_ok=True)
# images
for lg in ('de','en'):
    for th in ('light','dark'):
        for n,name in ((2,'compare'),(3,'sync'),(4,'twoway'),(5,'duplicates'),(6,'textdiff')):
            im=Image.open(f'{SRC}/store/screenshots/{lg}/{th}/{n}-{name}.png').convert('RGB')
            im.save(f'{OUT}/img/{lg}-{th}-{name}.png',optimize=True)
logo=Image.open(f'{SRC}/src/Folvane.App/Assets/logo.png').convert('RGBA')
logo.save(f'{OUT}/img/logo.png'); logo.resize((64,64),Image.LANCZOS).save(f'{OUT}/favicon.png')
logo.save(f'{OUT}/favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64)])
logo.resize((180,180),Image.LANCZOS).save(f'{OUT}/img/apple-touch-icon.png')
# OG image
W,H=1200,630
og=Image.new('RGB',(W,H),(246,245,242)); dr=ImageDraw.Draw(og)
def font(sz,bold=False):
    for p in ('/System/Library/Fonts/Helvetica.ttc','/System/Library/Fonts/SFNS.ttf'):
        try: return ImageFont.truetype(p,sz,index=1 if bold else 0)
        except Exception: pass
    return ImageFont.load_default()
shot=Image.open(f'{SRC}/store/screenshots/en/light/2-compare.png').convert('RGB')
sw=720; sh=int(shot.height*sw/shot.width); shot=shot.resize((sw,sh),Image.LANCZOS)
dr.rounded_rectangle((440,230,440+sw+4,230+sh+4),14,fill=(255,255,255),outline=(210,206,198),width=2)
og.paste(shot,(442,232))
og.paste(logo.resize((96,96),Image.LANCZOS),(60,60),logo.resize((96,96),Image.LANCZOS))
dr.text((176,78),'Folvane',font=font(56,True),fill=(30,34,48))
dr.text((60,200),'Two folders.',font=font(64,True),fill=(30,34,48))
dr.text((60,276),'One look.',font=font(64,True),fill=(63,79,200))
for i,t in enumerate(('Compare and sync folders','Preview, undo, offline','One-time purchase, Windows')):
    dr.text((60,400+i*40),t,font=font(28),fill=(94,99,114))
og.save(f'{OUT}/img/og.png',optimize=True)

# ---------- content ----------
L={}
L['en']=dict(code='en',loc='en_US',home='',sl='en',
 tag='Folder compare & sync',
 nav=[('features','Features'),('safe','Safety'),('price','Price'),('faq','FAQ')],
 support='Support',privacy='Privacy',imprint='Legal notice',skip='Skip to content',
 files=dict(index='index.html',privacy='privacy.html',support='support.html',imprint='imprint.html'),
 other='de/',otherlbl='DE',othername='Zu Deutsch wechseln',
 get='Get it from the Microsoft Store',getsub='Folvane – €9.99, one-time',
 title='Folvane – Folder Compare & Sync for Windows',
 desc='Compare two folders on Windows, see what is missing, newer or different, and sync with a preview. Undo any sync. Offline, no account, one-time purchase.',
 h1='Two folders. <em>One look.</em>',
 lead='Folvane shows you which files are missing, newer or different – and syncs your folders when you want, with a preview, backups and one-click undo. Everything stays on your PC.',
 meta='Windows 10 (1809+) and 11 · x64 and ARM64 · English and German · One-time purchase, no subscription',
 feat_h='Everything you need to keep folders in step',
 feats=[('Compare','Every file with its state: identical, left only, right only, left newer, right newer or different. By size and date in seconds, or byte by byte. Color filters and instant search.'),
  ('Sync with preview','Mirror either way, update the right side without deleting anything, or two-way where the newer file wins. Every action is listed first and can be unticked.'),
  ('Undo and history','Replaced and removed files are backed up first. Roll back the last sync completely with one click. Every run is kept in the history with a log.'),
  ('Text diff','Double-click a changed text file to see both versions side by side. Changed, added and removed lines are highlighted; F8 jumps to the next change.'),
  ('Profiles','Save a folder pair with its filters and sync mode, e.g. “Photos → USB stick”, and compare it again with one click.'),
  ('Duplicates','Find identical files across both folders by content, not by name, and move copies to the Recycle Bin. One copy always stays.'),
  ('Reports','Save the result as PDF, HTML or CSV – for clients, colleagues or your own records.'),
  ('Command line','Start from a terminal or script: <code>folvane --profile "Photos → USB stick"</code> or <code>folvane &lt;left&gt; &lt;right&gt;</code>.')],
 shots_h='See it in action',
 caps=['See instantly what’s missing, newer or different','Sync with a preview – nothing happens without you','Two-way sync: the newer file wins','Find duplicate files and reclaim space','What changed? Text files side by side'],
 alts=['Folvane comparing two folders with colored states','Sync preview listing every action','Two-way sync preview','Duplicate files found across two folders','Text diff with highlighted lines'],
 safe_h='Safe by design',
 safe_lead='A folder tool touches your real files, so Folvane is built to ask first and to be reversible.',
 safe=[('Preview first','Nothing is copied or removed until you have seen the list and confirmed it.'),
  ('Backups and undo','Files that are replaced or removed are backed up in a hidden <code>.folvane-backup</code> folder, so the last sync can be rolled back.'),
  ('Safe copying','Copies are written completely before they replace anything, and keep their modified date.'),
  ('Conflicts stay untouched','If both sides changed, two-way sync leaves the files alone instead of guessing.'),
  ('Recycle Bin for duplicates','Duplicate copies go to the Recycle Bin, and one copy is always kept.'),
  ('Offline and private','No account, no cloud, no ads, no telemetry. Logs stay on your PC.')],
 cmp_h='How it compares to free tools',
 cmp_lead='Free tools can be a fine choice. This is what Folvane adds, and a checklist worth running through for any tool you consider.',
 cmp_cols=('','Folvane','Typical free tools'),
 cmp=[('Preview before every sync','Always','Varies'),('One-click undo of the last sync','Yes, with history and logs','Often not available'),('Side-by-side text diff','Built in','Sometimes a separate tool'),('Saved profiles and command line','Yes','Varies'),('Duplicate finder','Built in','Often a separate tool'),('PDF, HTML and CSV reports','Yes','Rarely'),('Modern Windows 11 look, light and dark','Yes','Often dated'),('Ads or bundled offers','None','Varies'),('Updates and support through the Store','Yes','Varies')],
 price_h='Simple pricing',price='€9.99',
 price_p='One-time purchase through the Microsoft Store. No subscription, no account, no in-app purchases. The price shown in the Store applies; it can vary by country and local taxes.',
 req_h='System requirements',
 req=['Windows 10 version 1809 or newer, or Windows 11','x64 or ARM64 PC','About 150 MB of storage','No internet connection needed to use the app'],
 faq_h='Frequently asked questions',
 faq=[('Does it work with USB drives and network shares?','Yes, with anything Windows shows as a folder. For FAT/exFAT drives and memory cards there is a time tolerance and the option “ignore 1-hour offset” for daylight saving time.'),
  ('Does two-way sync detect deleted files?','No, on purpose. Without a stored previous state that would be guesswork. Use “Mirror” when deletions should be carried over; it is always previewed and backed up.'),
  ('Can I undo a sync?','Yes. Replaced and removed files are backed up first, and the last sync can be rolled back from the history.'),
  ('How are files compared?','By size and date (fast) or byte by byte (certain). You can include only certain types such as *.jpg; *.docx, or exclude patterns such as node_modules; .git; *.tmp.'),
  ('Does Folvane send data to the internet?','No. The app has no network access for your data, no account and no telemetry. See the <a href="{privacy}">privacy page</a>.'),
  ('Is there a subscription?','No. It is a one-time purchase.')],
 more='More questions and contact',
 sup_title='Support – Folvane',sup_desc='Help, answers and contact for Folvane.',sup_h='Support',
 sup_intro='Answers to common questions, and how to reach us.',
 sup_more=[('Keyboard shortcuts','F5 compare · Ctrl+O choose left folder · Ctrl+Shift+O choose right folder · Ctrl+F search · Ctrl+E report · F8 next change in the text diff.'),
  ('Where are my backups?','Backups of a sync are stored in the hidden <code>.folvane-backup</code> folder inside the affected folder. Use “History” in the app to undo a sync instead of restoring files by hand.'),
  ('Command line','Run <code>folvane &lt;left&gt; &lt;right&gt;</code> to compare two folders, or <code>folvane --profile "Name"</code> to open a saved profile.'),
  ('Refunds and purchases','Purchases, licenses and refunds are handled by the Microsoft Store. Use your Microsoft account’s order history for that.')],
 contact_h='Contact',contact_p='Questions or bug reports? Email us and mention your Windows version and Folvane version. The full provider details are in the <a href="{imprint}">legal notice</a>.',
 contact_mail='Email',
 contact_note='App: Folvane – Folder Compare & Sync · Microsoft Store ID 9NSDC58HLFRR',
 priv_title='Privacy – Folvane',priv_desc='Privacy policy for Folvane and this website.',
 imp_title='Legal notice – Folvane',imp_desc='Legal notice and provider information for Folvane.',
 foot_note='No cookies, no trackers, no external scripts.',
 nf_t='Page not found',nf_p='This page does not exist.',nf_a='Back to the home page'
)
L['de']=dict(code='de',loc='de_DE',home='',sl='de',
 tag='Ordner vergleichen & synchronisieren',
 nav=[('features','Funktionen'),('safe','Sicherheit'),('price','Preis'),('faq','FAQ')],
 support='Support',privacy='Datenschutz',imprint='Impressum',skip='Zum Inhalt',
 files=dict(index='index.html',privacy='privacy.html',support='support.html',imprint='impressum.html'),
 other='../',otherlbl='EN',othername='Switch to English',
 get='Im Microsoft Store herunterladen',getsub='Folvane – 9,99 €, einmalig',
 title='Folvane – Ordner vergleichen & synchronisieren unter Windows',
 desc='Zwei Ordner unter Windows vergleichen, fehlende, neuere und geänderte Dateien sehen und mit Vorschau abgleichen. Jeder Abgleich rückgängig. Offline, ohne Konto, Einmalkauf.',
 h1='Zwei Ordner. <em>Ein Blick.</em>',
 lead='Folvane zeigt dir, welche Dateien fehlen, neuer oder anders sind – und gleicht deine Ordner auf Wunsch ab: mit Vorschau, Sicherungen und Rückgängig mit einem Klick. Alles bleibt auf deinem PC.',
 meta='Windows 10 (1809+) und 11 · x64 und ARM64 · Deutsch und Englisch · Einmalkauf, kein Abo',
 feat_h='Alles, damit deine Ordner im Gleichschritt bleiben',
 feats=[('Vergleichen','Jede Datei mit ihrem Zustand: gleich, nur links, nur rechts, links neuer, rechts neuer oder unterschiedlich. Nach Größe und Datum in Sekunden oder Byte für Byte. Farbige Filter und Sofortsuche.'),
  ('Sync mit Vorschau','Spiegeln in beide Richtungen, rechts aktualisieren ohne etwas zu löschen oder Zwei-Wege-Abgleich, bei dem die neuere Datei gewinnt. Jede Aktion steht vorher in der Liste und lässt sich abwählen.'),
  ('Rückgängig und Verlauf','Überschriebene und entfernte Dateien werden vorher gesichert. Den letzten Abgleich nimmst du mit einem Klick vollständig zurück. Jeder Lauf steht mit Protokoll im Verlauf.'),
  ('Textvergleich','Doppelklick auf eine geänderte Textdatei zeigt beide Fassungen nebeneinander. Geänderte, neue und gelöschte Zeilen sind farbig markiert; F8 springt zur nächsten Änderung.'),
  ('Profile','Ordnerpaar mit Filtern und Abgleich-Art speichern, z. B. „Fotos → USB-Stick“, und mit einem Klick erneut vergleichen.'),
  ('Duplikate','Identische Dateien über beide Ordner am Inhalt statt am Namen finden und Kopien in den Papierkorb verschieben. Eine Datei bleibt immer erhalten.'),
  ('Berichte','Ergebnis als PDF, HTML oder CSV speichern – für Kunden, Kollegen oder die eigene Ablage.'),
  ('Kommandozeile','Aus Terminal oder Skript starten: <code>folvane --profile "Fotos → USB-Stick"</code> oder <code>folvane &lt;links&gt; &lt;rechts&gt;</code>.')],
 shots_h='Folvane in Aktion',
 caps=['Sieh sofort, was fehlt, neuer oder anders ist','Abgleichen mit Vorschau – nichts passiert ungefragt','Zwei-Wege-Abgleich: die neuere Datei gewinnt','Doppelte Dateien finden und Platz zurückholen','Was hat sich geändert? Textdateien nebeneinander'],
 alts=['Folvane vergleicht zwei Ordner mit farbigen Zuständen','Sync-Vorschau mit allen Aktionen','Vorschau des Zwei-Wege-Abgleichs','Doppelte Dateien in zwei Ordnern gefunden','Textvergleich mit markierten Zeilen'],
 safe_h='Sicher by design',
 safe_lead='Ein Ordnerwerkzeug fasst deine echten Dateien an. Deshalb fragt Folvane zuerst und lässt sich zurücknehmen.',
 safe=[('Erst Vorschau','Nichts wird kopiert oder entfernt, bevor du die Liste gesehen und bestätigt hast.'),
  ('Sicherungen und Rückgängig','Überschriebene oder entfernte Dateien werden im versteckten Ordner <code>.folvane-backup</code> gesichert, sodass sich der letzte Abgleich zurücknehmen lässt.'),
  ('Sicheres Kopieren','Kopien werden erst vollständig geschrieben, dann ersetzt, und behalten ihr Änderungsdatum.'),
  ('Konflikte bleiben unangetastet','Wurden beide Seiten geändert, lässt der Zwei-Wege-Abgleich die Dateien in Ruhe, statt zu raten.'),
  ('Papierkorb für Duplikate','Doppelte Kopien wandern in den Papierkorb, eine Datei bleibt immer erhalten.'),
  ('Offline und privat','Kein Konto, keine Cloud, keine Werbung, keine Telemetrie. Protokolle bleiben auf deinem PC.')],
 cmp_h='Der Vergleich zu kostenlosen Tools',
 cmp_lead='Kostenlose Tools können eine gute Wahl sein. Das bringt Folvane mit, und es ist eine Checkliste, die sich für jedes Tool lohnt.',
 cmp_cols=('','Folvane','Typische kostenlose Tools'),
 cmp=[('Vorschau vor jedem Abgleich','Immer','Unterschiedlich'),('Letzten Abgleich mit einem Klick rückgängig','Ja, mit Verlauf und Protokoll','Oft nicht vorhanden'),('Textvergleich nebeneinander','Eingebaut','Teils ein separates Programm'),('Profile und Kommandozeile','Ja','Unterschiedlich'),('Duplikate finden','Eingebaut','Oft ein separates Programm'),('Berichte als PDF, HTML, CSV','Ja','Selten'),('Moderne Windows-11-Optik, hell und dunkel','Ja','Oft in die Jahre gekommen'),('Werbung oder Zusatzangebote','Keine','Unterschiedlich'),('Updates und Support über den Store','Ja','Unterschiedlich')],
 price_h='Einfacher Preis',price='9,99 €',
 price_p='Einmalkauf über den Microsoft Store. Kein Abo, kein Konto, keine Käufe in der App. Maßgeblich ist der im Store angezeigte Preis; er kann je nach Land und Steuern abweichen.',
 req_h='Systemanforderungen',
 req=['Windows 10 ab Version 1809 oder Windows 11','x64- oder ARM64-PC','Etwa 150 MB Speicherplatz','Keine Internetverbindung zur Nutzung nötig'],
 faq_h='Häufige Fragen',
 faq=[('Funktioniert es mit USB-Sticks und Netzlaufwerken?','Ja, mit allem, was Windows als Ordner anzeigt. Für FAT/exFAT-Laufwerke und Speicherkarten gibt es eine Zeittoleranz und die Option „1 Stunde Versatz ignorieren“ für die Sommerzeit.'),
  ('Erkennt der Zwei-Wege-Abgleich gelöschte Dateien?','Nein, mit Absicht. Ohne gespeicherten Vorzustand wäre das geraten. Nutze „Spiegeln“, wenn Löschungen übernommen werden sollen; das steht immer in der Vorschau und wird gesichert.'),
  ('Kann ich einen Abgleich rückgängig machen?','Ja. Überschriebene und entfernte Dateien werden vorher gesichert, den letzten Abgleich nimmst du im Verlauf zurück.'),
  ('Wie werden Dateien verglichen?','Nach Größe und Datum (schnell) oder Byte für Byte (sicher). Du kannst nur bestimmte Typen wie *.jpg; *.docx einschließen oder Muster wie node_modules; .git; *.tmp ausschließen.'),
  ('Sendet Folvane Daten ins Internet?','Nein. Die App sendet keine Daten, hat kein Konto und keine Telemetrie. Siehe <a href="{privacy}">Datenschutz</a>.'),
  ('Gibt es ein Abo?','Nein, es ist ein Einmalkauf.')],
 more='Weitere Fragen und Kontakt',
 sup_title='Support – Folvane',sup_desc='Hilfe, Antworten und Kontakt zu Folvane.',sup_h='Support',
 sup_intro='Antworten auf häufige Fragen und der Weg zum Kontakt.',
 sup_more=[('Tastaturkürzel','F5 Vergleichen · Strg+O linken Ordner wählen · Strg+Umschalt+O rechten Ordner wählen · Strg+F Suche · Strg+E Bericht · F8 nächste Änderung im Textvergleich.'),
  ('Wo liegen meine Sicherungen?','Sicherungen eines Abgleichs liegen im versteckten Ordner <code>.folvane-backup</code> im jeweiligen Ordner. Nutze im Programm den „Verlauf“, um einen Abgleich rückgängig zu machen, statt Dateien von Hand zurückzukopieren.'),
  ('Kommandozeile','<code>folvane &lt;links&gt; &lt;rechts&gt;</code> vergleicht zwei Ordner, <code>folvane --profile "Name"</code> öffnet ein gespeichertes Profil.'),
  ('Kauf und Erstattung','Käufe, Lizenzen und Erstattungen laufen über den Microsoft Store. Nutze dafür den Bestellverlauf deines Microsoft-Kontos.')],
 contact_h='Kontakt',contact_p='Fragen oder Fehler? Schreib uns und nenne deine Windows- und Folvane-Version. Die vollständigen Anbieterangaben stehen im <a href="{imprint}">Impressum</a>.',
 contact_mail='E-Mail',
 contact_note='App: Folvane – Ordner vergleichen & synchronisieren · Microsoft-Store-ID 9NSDC58HLFRR',
 priv_title='Datenschutz – Folvane',priv_desc='Datenschutzerklärung für Folvane und diese Website.',
 imp_title='Impressum – Folvane',imp_desc='Impressum und Anbieterkennzeichnung für Folvane.',
 foot_note='Keine Cookies, keine Tracker, keine externen Skripte.',
 nf_t='Seite nicht gefunden',nf_p='Diese Seite gibt es nicht.',nf_a='Zur Startseite'
)
PRIV={'en':'''<h1>Privacy</h1>
<p>Last updated: 31 October 2026. The controller is the provider named in the <a href="{imprint}">legal notice</a>.</p>
<h2>The Folvane app</h2>
<p>Folvane does not collect, store or transmit any personal data. The app has no internet connection, no account, no ads, no analytics or crash services.</p>
<ul>
<li>Folvane only reads the folders you choose, and only writes to them when you run or undo a sync or move files to the Recycle Bin. Backups of a sync are kept in a hidden <code>.folvane-backup</code> folder inside that folder; the log stays on your PC only.</li>
<li>Settings and the list of recent folder pairs are stored locally on your PC (app data folder) and are removed on uninstall.</li>
<li>Reports (PDF, HTML, CSV) are saved only where you choose.</li>
</ul>
<p>Purchase and installation are handled by the Microsoft Store under Microsoft's privacy statement; we only receive aggregated sales and crash statistics without names.</p>
<h2>This website</h2>
<p>This site is served by GitHub Pages (GitHub Inc., USA), which processes technically necessary access data such as IP addresses to deliver the site and prevent abuse (Art. 6(1)(f) GDPR). We use no cookies, no trackers and no external fonts or scripts. Links to the Microsoft Store leave this site; Microsoft's privacy statement applies there.</p>
<h2>Your rights</h2>
<p>You have the right to access, rectification, erasure, restriction, data portability and objection, and to lodge a complaint with a supervisory authority. Contact: see the <a href="{imprint}">legal notice</a>.</p>''',
'de':'''<h1>Datenschutz</h1>
<p>Stand: 31. Oktober 2026. Verantwortlich ist der im <a href="{imprint}">Impressum</a> genannte Anbieter.</p>
<h2>Die App Folvane</h2>
<p>Folvane erhebt, speichert und überträgt keine personenbezogenen Daten. Die App hat keine Internetverbindung, kein Konto, keine Werbung, keine Analyse- oder Absturzdienste.</p>
<ul>
<li>Folvane liest nur die Ordner, die du auswählst, und schreibt nur dorthin, wenn du einen Abgleich ausführst, ihn rückgängig machst oder Dateien in den Papierkorb verschiebst. Sicherungen eines Abgleichs liegen im versteckten Ordner <code>.folvane-backup</code> im jeweiligen Ordner, das Protokoll nur lokal auf deinem PC.</li>
<li>Einstellungen und die Liste zuletzt verwendeter Ordnerpaare liegen lokal auf deinem PC (App-Datenordner). Sie werden beim Deinstallieren entfernt.</li>
<li>Berichte (PDF, HTML, CSV) speichert Folvane nur dort, wo du es auswählst.</li>
</ul>
<p>Kauf und Installation laufen über den Microsoft Store. Dabei gilt die Datenschutzerklärung von Microsoft; wir erhalten von Microsoft nur zusammengefasste Verkaufs- und Absturzstatistiken ohne Namen.</p>
<h2>Diese Website</h2>
<p>Die Seite wird über GitHub Pages (GitHub Inc., USA) ausgeliefert. GitHub verarbeitet dabei technisch notwendige Zugriffsdaten wie die IP-Adresse, um die Seite auszuliefern und vor Missbrauch zu schützen (Art. 6 Abs. 1 lit. f DSGVO). Wir setzen keine Cookies, keine Tracker und keine externen Schriften oder Skripte ein. Links zum Microsoft Store verlassen diese Seite; dort gilt die Datenschutzerklärung von Microsoft.</p>
<h2>Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit und Widerspruch sowie auf Beschwerde bei einer Datenschutzaufsichtsbehörde. Kontakt: siehe <a href="{imprint}">Impressum</a>.</p>'''}
IMP={'en':('Legal notice','Information pursuant to § 5 DDG (German Digital Services Act)','Germany','Contact','Email','Scope','This legal notice applies to this website and the Windows app “Folvane – Folder Compare &amp; Sync”. It matches the central <a href="https://minh.systems/impressum/">legal notice of minh.systems</a>.','Consumer dispute resolution','We are neither willing nor obliged to take part in dispute resolution proceedings before a consumer arbitration board.'),
 'de':('Impressum','Angaben gemäß § 5 DDG','Deutschland','Kontakt','E-Mail','Geltungsbereich','Dieses Impressum gilt für diese Website und die Windows-App „Folvane – Ordner vergleichen &amp; synchronisieren“. Es entspricht dem zentralen <a href="https://minh.systems/impressum/">Impressum von minh.systems</a>.','Verbraucherstreitbeilegung','Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.')}

def head(c,page,title,desc,pre,og='img/og.png'):
    f=c['files']; o=L['de' if c['code']=='en' else 'en']
    url=lambda cc,p: BASE+('' if cc=='en' else 'de/')+('' if p=='index' else L[cc]['files'][p])
    here=url(c['code'],page)
    return f'''<!doctype html>
<html lang="{c['code']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#3f4fc8">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="en" href="{url('en',page)}">
<link rel="alternate" hreflang="de" href="{url('de',page)}">
<link rel="alternate" hreflang="x-default" href="{url('en',page)}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Folvane">
<meta property="og:locale" content="{c['loc']}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{here}"><meta property="og:image" content="{BASE}img/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Folvane – folder compare &amp; sync for Windows">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{pre}favicon.png" type="image/png"><link rel="icon" href="{pre}favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{pre}img/apple-touch-icon.png">
<link rel="stylesheet" href="{pre}style.css?v=2">
<script src="{pre}site.js" defer></script>
</head>
'''
def shell(c,page,title,desc,body,cls=''):
    pre='' if c['code']=='en' else '../'
    f=c['files']; sub='' if c['code']=='en' else 'de/'
    otherpage=L['de' if c['code']=='en' else 'en']['files'][page]
    oth=c['other']+('' if page=='index' else otherpage)
    home='./'
    nav=''.join(f'<a href="{home}#{k}">{v}</a>' for k,v in c['nav']) if page=='index' else ''.join(f'<a href="{home}#{k}">{v}</a>' for k,v in c['nav'][:1]+c['nav'][2:3])
    return head(c,page,title,desc,pre)+f'''<body class="{cls}">
<a class="skip" href="#main">{c['skip']}</a>
<header class="top"><nav aria-label="Main" class="wrap">
<a class="brand" href="{home}"><img alt="" width="36" height="36" src="{pre}img/logo.png"><span>Folvane<small>{c['tag']}</small></span></a>
<div class="links">{nav}<a href="{f['support']}">{c['support']}</a><a class="lang" href="{oth}" hreflang="{'de' if c['code']=='en' else 'en'}" lang="{'de' if c['code']=='en' else 'en'}" aria-label="{c['othername']}">{c['otherlbl']}</a></div>
</nav></header>
<main id="main">
{body}
</main>
<footer class="wrap footer">
<a href="{home}">Folvane</a> · <a href="{f['support']}">{c['support']}</a> · <a href="{f['privacy']}">{c['privacy']}</a> · <a href="{f['imprint']}">{c['imprint']}</a>
<p>© 2026 Minh Studios · Michel Nguyen</p>
<p>{c['foot_note']}</p>
</footer>
</body>
</html>
'''
def picture(c,name,alt,eager=False):
    l=c['code']; pre='' if l=='en' else '../'
    return f'<picture><source media="(prefers-color-scheme: dark)" srcset="{pre}img/{l}-dark-{name}.png"><img src="{pre}img/{l}-light-{name}.png" alt="{html.escape(alt)}" width="1366" height="820" {"fetchpriority=high" if eager else "loading=lazy"} decoding="async"></picture>'
def storebtn(c):
    return f'<a class="btn store" href="{STORE}" rel="noopener"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 22 22"><path fill="currentColor" d="M2 3.5 10 2.4v8H2zM11 2.3 20 1v9.4h-9zM2 11.6h8v8L2 18.5zM11 11.6h9V21l-9-1.3z"/></svg><span>{c["get"]}<small>{c["getsub"]}</small></span></a>'
def mailhtml(c):
    return f'<span class="mail" data-mail>mip [at] gmx.biz</span>'

def index(c):
    f=c['files']; name=['compare','sync','twoway','duplicates','textdiff']
    feats=''.join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t,d in c['feats'])
    shots=''.join(f'<figure><div class="frame">{picture(c,n,a)}</div><figcaption>{cap}</figcaption></figure>' for n,a,cap in zip(name[1:],c['alts'][1:],c['caps'][1:]))
    safe=''.join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t,d in c['safe'])
    th=c['cmp_cols']
    rows=''.join(f'<tr><th scope="row">{a}</th><td class="yes">{b}</td><td>{d}</td></tr>' for a,b,d in c['cmp'])
    req=''.join(f'<li>{r}</li>' for r in c['req'])
    faq=''.join(f'<details><summary>{q}</summary><p>{a.format(privacy=f["privacy"])}</p></details>' for q,a in c['faq'])
    body=f'''<section class="hero wrap">
<h1>{c['h1']}</h1>
<p class="lead">{c['lead']}</p>
<p>{storebtn(c)}</p>
<p class="note">{c['meta']}</p>
<div class="frame big">{picture(c,'compare',c['alts'][0],True)}</div>
</section>
<section id="features" class="wrap"><h2>{c['feat_h']}</h2><div class="grid">{feats}</div></section>
<section id="shots" class="wrap"><h2>{c['shots_h']}</h2><div class="shots">{shots}</div></section>
<section id="safe" class="wrap"><h2>{c['safe_h']}</h2><p class="sub">{c['safe_lead']}</p><div class="grid">{safe}</div></section>
<section id="compare" class="wrap"><h2>{c['cmp_h']}</h2><p class="sub">{c['cmp_lead']}</p>
<div class="tablewrap"><table><thead><tr><th scope="col"><span class="sr">{c['cmp_h']}</span></th><th scope="col">{th[1]}</th><th scope="col">{th[2]}</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section id="price" class="wrap two"><div class="card pricecard"><h2>{c['price_h']}</h2><p class="price">{c['price']}</p><p>{c['price_p']}</p><p>{storebtn(c)}</p></div>
<div class="card"><h2>{c['req_h']}</h2><ul class="ticks">{req}</ul></div></section>
<section id="faq" class="wrap doc"><h2>{c['faq_h']}</h2>{faq}<p><a href="{f['support']}">{c['more']} →</a></p></section>'''
    return shell(c,'index',c['title'],c['desc'],body,'home')
def support(c):
    f=c['files']
    faq=''.join(f'<details><summary>{q}</summary><p>{a.format(privacy=f["privacy"])}</p></details>' for q,a in c['faq'])
    more=''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in c['sup_more'])
    body=f'''<div class="wrap doc"><h1>{c['sup_h']}</h1><p class="lead2">{c['sup_intro']}</p>
<h2>{c['faq_h']}</h2>{faq}{more}
<section class="card"><h2>{c['contact_h']}</h2><p>{c['contact_p'].format(imprint=f['imprint'])}</p><p>{c['contact_mail']}: {mailhtml(c)}</p><p class="note">{c['contact_note']}</p></section></div>'''
    return shell(c,'support',c['sup_title'],c['sup_desc'],body,'document-page')
def privacy(c):
    f=c['files']
    return shell(c,'privacy',c['priv_title'],c['priv_desc'],f'<div class="wrap doc">{PRIV[c["code"]].format(imprint=f["imprint"])}</div>','document-page')
def imprint(c):
    t,h,cty,k,em,sc,sct,vs,vst=IMP[c['code']]; f=c['files']
    body=f'''<div class="wrap doc"><h1>{t}</h1>
<section class="card"><h2>{h}</h2><address>Michel Nguyen<br>Minh Nguyen Studios<br>Windmühlenstr. 74<br>07937 Zeulenroda-Triebes<br>{cty}</address></section>
<section class="card"><h2>{k}</h2><p>{em}: {mailhtml(c)}</p></section>
<section class="card"><h2>{sc}</h2><p>{sct}</p></section>
<section class="card"><h2>{vs}</h2><p>{vst}</p><p><a href="{f['privacy']}">{c['privacy']}</a></p></section></div>'''
    return shell(c,'imprint',c['imp_title'],c['imp_desc'],body,'document-page')
for cc,pre in (('en',''),('de','de/')):
    c=L[cc]; f=c['files']
    for page,fn in (('index',index),('support',support),('privacy',privacy),('imprint',imprint)):
        name='index.html' if page=='index' else f[page]
        open(f'{OUT}/{pre}{name}','w').write(fn(c))
# 404 (absolute paths for /Folvane/)
open(f'{OUT}/404.html','w').write(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark"><meta name="robots" content="noindex">
<title>404 – Folvane</title><link rel="icon" href="/Folvane/favicon.png"><link rel="stylesheet" href="/Folvane/style.css?v=2"></head>
<body class="document-page"><header class="top"><nav class="wrap"><a class="brand" href="/Folvane/"><img alt="" width="36" height="36" src="/Folvane/img/logo.png"><span>Folvane</span></a></nav></header>
<main class="wrap doc"><h1>404</h1><p>{L['en']['nf_p']} / {L['de']['nf_p']}</p>
<p><a href="/Folvane/">{L['en']['nf_a']}</a> · <a href="/Folvane/de/">{L['de']['nf_a']}</a></p></main></body></html>
''')
open(f'{OUT}/robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
pages=['index','support','privacy','imprint']
def u(cc,p): return BASE+('' if cc=='en' else 'de/')+('' if p=='index' else L[cc]['files'][p])
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
for cc in ('en','de'):
    for p in pages:
        sm+=f'<url><loc>{u(cc,p)}</loc><xhtml:link rel="alternate" hreflang="en" href="{u("en",p)}"/><xhtml:link rel="alternate" hreflang="de" href="{u("de",p)}"/><xhtml:link rel="alternate" hreflang="x-default" href="{u("en",p)}"/><lastmod>2026-10-31</lastmod></url>\n'
open(f'{OUT}/sitemap.xml','w').write(sm+'</urlset>\n')
open(f'{OUT}/site.js','w').write('''(function(){var u=['m','i','p'].join(''),d=['gmx','biz'].join('.');
document.querySelectorAll('[data-mail]').forEach(function(el){var a=document.createElement('a');a.href='mai'+'lto:'+u+'@'+d;a.textContent=u+'@'+d;el.replaceChildren(a);});})();
''')
open(f'{OUT}/.nojekyll','w').write('')
open(f'{OUT}/README.md','w').write('# Folvane website\n\nStatic site (no build step) for Folvane – Folder Compare & Sync. Published via GitHub Pages at https://minh.systems/Folvane/.\n\n- English: repository root. German: `de/`.\n- Microsoft Store: https://apps.microsoft.com/detail/9NSDC58HLFRR\n')
