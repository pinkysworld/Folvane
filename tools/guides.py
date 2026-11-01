# Landing pages (exec'd by build.py). Honest, no competitor claims.
GUIDES={'en':{},'de':{}}
GUIDES['en']['check']=dict(
 title='Check your backup – is the backup folder complete? | Folvane',
 desc='How to check on Windows whether a backup folder is complete and up to date, and what Folvane shows. Folvane compares folders; it does not schedule backups.',
 h1='Check your backup on Windows',
 lead='A backup you never checked is a guess. Here is a simple way to see whether your backup folder really contains everything from the original, and which files are missing or out of date.',
 secs=[('The idea','Compare the original folder (left) with the backup folder (right). Every file ends up in one of a few states, so gaps are visible at a glance instead of buried in thousands of files.'),
  ('Steps with Folvane','<ol><li>Choose the original folder on the left and the backup folder on the right.</li><li>Press F5 to compare. By size and date this takes seconds; choose byte-by-byte if you want to be certain that the content is identical.</li><li>Read the states: <strong>identical</strong> means the backup is current. <strong>Left only</strong> means the file exists in the original but not in the backup. <strong>Left newer</strong> means the backup holds an older version. <strong>Right only</strong> means the backup contains a file that is no longer in the original.</li><li>Use the color filters to show just the problems, or search for a name.</li><li>Double-click a changed text file to see both versions side by side.</li><li>Save the result as a PDF, HTML or CSV report if you want to keep a record.</li></ol>'),
  ('Bringing the backup up to date','If the backup should match the original, Folvane can sync it. Every action is listed in a preview first, and you can untick single items. “Update right side” copies new and changed files without deleting anything; “Mirror” also removes files that are not in the original. Replaced and removed files are backed up first, so the last sync can be undone from the history.'),
  ('Honest limits','<ul><li>Folvane <strong>compares and syncs folders when you start it</strong>. It does not schedule or run backups in the background. To keep a backup current you run the comparison again, or let another tool create the backup and use Folvane to check it.</li><li>A matching comparison shows that two folders have the same files. It does not prove that the backup can be restored, that the drive is healthy, or that you have an additional copy somewhere else.</li><li>Files that are open or locked by other programs may not be copied; the sync log tells you about failures.</li><li>Two-way sync does not detect deleted files. Use mirror when deletions should be carried over.</li></ul>')],
 faq=[('Does Folvane make backups automatically?','No. It compares two folders and syncs them on demand, with a preview and undo. It has no scheduler.'),
  ('Can I check an external drive or network share?','Yes, anything Windows shows as a folder. For FAT/exFAT drives there is a time tolerance for timestamp differences.'),
  ('Does it work offline?','Yes. Folvane needs no internet connection, no account and sends no data.'),
  ('What if the backup has files the original does not?','They show as “right only”. Folvane does not remove them unless you choose a mirror sync, which is always previewed and backed up first.')])
GUIDES['en']['cmpwin']=dict(
 title='Compare folders on Windows – see what differs | Folvane',
 desc='Compare two folders on Windows and see which files are missing, newer or different. Folvane shows every file with its state, offers a text diff and syncs with preview and undo.',
 h1='Compare folders on Windows',
 lead='Windows Explorer shows you folders one at a time. To find out how two folders differ you need to see them side by side, file by file. Folvane does that and lets you act on the result.',
 secs=[('What you see','Both folders are listed together. Each file has a state: identical, left only, right only, left newer, right newer or different. Color filters and instant search help in large folders, and sub-folders are included.'),
  ('How files are compared','Quick mode compares size and modification date and finishes in seconds. Byte-by-byte mode reads the content and tells you for sure whether two files are the same. You can include only certain types such as <code>*.jpg; *.docx</code> or exclude patterns such as <code>node_modules; .git; *.tmp</code>.'),
  ('Looking inside files','Double-click a changed text file for a side-by-side text diff with changed, added and removed lines highlighted; F8 jumps to the next change. A duplicates view finds identical files by content instead of by name.'),
  ('Acting on the result','You can sync in either direction, update one side without deleting anything, or use two-way sync where the newer file wins. Nothing happens before you have seen the list, replaced files are backed up first and the last sync can be undone. Profiles store a folder pair with its filters so you can repeat the comparison with one click, and results can be saved as PDF, HTML or CSV.'),
  ('Good to know','<ul><li>Folvane is for Windows 10 (1809+) and 11, x64 and ARM64. It works offline, needs no account and has no telemetry.</li><li>It compares when you start it; it is not a background sync service.</li><li>Two-way sync leaves files alone if both sides changed, and does not detect deletions.</li></ul>')],
 faq=[('Can I compare two folders without changing anything?','Yes. Comparing only reads. Nothing is copied or removed until you review the preview and confirm a sync.'),
  ('Does it compare file contents?','Yes, in byte-by-byte mode. The default quick mode uses size and date.'),
  ('Can I compare folders on a USB stick or network drive?','Yes, anything Windows shows as a folder.'),
  ('How much does it cost?','9.99 EUR as a one-time purchase from the Microsoft Store. No subscription. The price shown in the Store applies.')])
GUIDES['de']['check']=dict(
 title='Backup prüfen – ist der Backup-Ordner vollständig? | Folvane',
 desc='So prüfst du unter Windows, ob ein Backup-Ordner vollständig und aktuell ist, und was Folvane anzeigt. Folvane vergleicht Ordner; es plant keine Backups.',
 h1='Backup prüfen unter Windows',
 lead='Ein Backup, das nie geprüft wurde, ist eine Vermutung. So siehst du einfach, ob dein Backup-Ordner wirklich alles aus dem Original enthält und welche Dateien fehlen oder veraltet sind.',
 secs=[('Die Idee','Vergleiche den Originalordner (links) mit dem Backup-Ordner (rechts). Jede Datei bekommt einen Zustand, sodass Lücken sofort auffallen, statt zwischen tausenden Dateien unterzugehen.'),
  ('Schritte mit Folvane','<ol><li>Wähle links den Originalordner und rechts den Backup-Ordner.</li><li>Drücke F5 zum Vergleichen. Nach Größe und Datum dauert das Sekunden; wähle Byte für Byte, wenn du sicher sein willst, dass der Inhalt gleich ist.</li><li>Lies die Zustände: <strong>Gleich</strong> heißt, das Backup ist aktuell. <strong>Nur links</strong> heißt, die Datei gibt es im Original, aber nicht im Backup. <strong>Links neuer</strong> heißt, das Backup hat eine ältere Fassung. <strong>Nur rechts</strong> heißt, das Backup enthält eine Datei, die es im Original nicht mehr gibt.</li><li>Mit den farbigen Filtern zeigst du nur die Probleme, oder du suchst nach einem Namen.</li><li>Doppelklick auf eine geänderte Textdatei zeigt beide Fassungen nebeneinander.</li><li>Speichere das Ergebnis bei Bedarf als PDF-, HTML- oder CSV-Bericht.</li></ol>'),
  ('Backup aktualisieren','Soll das Backup dem Original entsprechen, kann Folvane es abgleichen. Jede Aktion steht vorher in einer Vorschau, einzelne Punkte lassen sich abwählen. „Rechts aktualisieren“ kopiert neue und geänderte Dateien, ohne etwas zu löschen; „Spiegeln“ entfernt zusätzlich Dateien, die im Original fehlen. Überschriebene und entfernte Dateien werden vorher gesichert, der letzte Abgleich lässt sich im Verlauf rückgängig machen.'),
  ('Ehrliche Grenzen','<ul><li>Folvane <strong>vergleicht und gleicht Ordner ab, wenn du es startest</strong>. Es plant oder führt keine Backups im Hintergrund aus. Um ein Backup aktuell zu halten, startest du den Vergleich erneut, oder du erstellst das Backup mit einem anderen Programm und prüfst es mit Folvane.</li><li>Ein übereinstimmender Vergleich zeigt, dass zwei Ordner dieselben Dateien enthalten. Er beweist nicht, dass sich das Backup wiederherstellen lässt, dass der Datenträger gesund ist oder dass es eine weitere Kopie an einem anderen Ort gibt.</li><li>Dateien, die von anderen Programmen geöffnet oder gesperrt sind, werden eventuell nicht kopiert; das Protokoll des Abgleichs zeigt Fehler.</li><li>Der Zwei-Wege-Abgleich erkennt keine gelöschten Dateien. Nutze „Spiegeln“, wenn Löschungen übernommen werden sollen.</li></ul>')],
 faq=[('Macht Folvane automatisch Backups?','Nein. Es vergleicht zwei Ordner und gleicht sie auf Wunsch ab, mit Vorschau und Rückgängig. Eine Zeitplanung gibt es nicht.'),
  ('Kann ich eine externe Festplatte oder ein Netzlaufwerk prüfen?','Ja, alles, was Windows als Ordner anzeigt. Für FAT/exFAT-Laufwerke gibt es eine Zeittoleranz bei Zeitstempeln.'),
  ('Funktioniert das offline?','Ja. Folvane braucht keine Internetverbindung und kein Konto und sendet keine Daten.'),
  ('Was, wenn das Backup Dateien enthält, die das Original nicht hat?','Sie erscheinen als „nur rechts“. Folvane entfernt sie nur, wenn du einen Spiegel-Abgleich wählst, der immer vorher angezeigt und gesichert wird.')])
GUIDES['de']['cmpwin']=dict(
 title='Ordner vergleichen unter Windows – Unterschiede sehen | Folvane',
 desc='Zwei Ordner unter Windows vergleichen und sehen, welche Dateien fehlen, neuer oder anders sind. Folvane zeigt jede Datei mit Zustand, bietet Textvergleich und Abgleich mit Vorschau und Rückgängig.',
 h1='Ordner vergleichen unter Windows',
 lead='Der Windows-Explorer zeigt Ordner einzeln. Um zu erkennen, wie sich zwei Ordner unterscheiden, musst du sie Datei für Datei nebeneinander sehen. Folvane macht das und lässt dich auf das Ergebnis reagieren.',
 secs=[('Was du siehst','Beide Ordner stehen gemeinsam in einer Liste. Jede Datei hat einen Zustand: gleich, nur links, nur rechts, links neuer, rechts neuer oder unterschiedlich. Farbfilter und Sofortsuche helfen in großen Ordnern, Unterordner sind eingeschlossen.'),
  ('Wie Dateien verglichen werden','Der schnelle Modus vergleicht Größe und Änderungsdatum und ist in Sekunden fertig. Byte für Byte liest den Inhalt und sagt dir sicher, ob zwei Dateien gleich sind. Du kannst nur bestimmte Typen wie <code>*.jpg; *.docx</code> einschließen oder Muster wie <code>node_modules; .git; *.tmp</code> ausschließen.'),
  ('Blick in die Dateien','Doppelklick auf eine geänderte Textdatei zeigt einen Textvergleich nebeneinander mit markierten geänderten, neuen und gelöschten Zeilen; F8 springt zur nächsten Änderung. Die Duplikat-Ansicht findet identische Dateien am Inhalt statt am Namen.'),
  ('Auf das Ergebnis reagieren','Du kannst in beide Richtungen abgleichen, eine Seite aktualisieren ohne etwas zu löschen oder den Zwei-Wege-Abgleich nutzen, bei dem die neuere Datei gewinnt. Nichts passiert, bevor du die Liste gesehen hast, überschriebene Dateien werden vorher gesichert und der letzte Abgleich lässt sich rückgängig machen. Profile speichern ein Ordnerpaar mit Filtern für den nächsten Vergleich mit einem Klick, Ergebnisse gibt es als PDF, HTML oder CSV.'),
  ('Gut zu wissen','<ul><li>Folvane läuft unter Windows 10 (1809+) und 11, x64 und ARM64. Es arbeitet offline, braucht kein Konto und hat keine Telemetrie.</li><li>Es vergleicht, wenn du es startest; es ist kein Synchronisationsdienst im Hintergrund.</li><li>Der Zwei-Wege-Abgleich lässt Dateien in Ruhe, wenn beide Seiten geändert wurden, und erkennt keine Löschungen.</li></ul>')],
 faq=[('Kann ich zwei Ordner vergleichen, ohne etwas zu ändern?','Ja. Das Vergleichen liest nur. Nichts wird kopiert oder entfernt, bevor du die Vorschau geprüft und einen Abgleich bestätigt hast.'),
  ('Werden auch Dateiinhalte verglichen?','Ja, im Modus Byte für Byte. Der schnelle Standardmodus nutzt Größe und Datum.'),
  ('Kann ich Ordner auf einem USB-Stick oder Netzlaufwerk vergleichen?','Ja, alles, was Windows als Ordner anzeigt.'),
  ('Was kostet Folvane?','9,99 € als Einmalkauf im Microsoft Store. Kein Abo. Maßgeblich ist der im Store angezeigte Preis.')])

def guide(c,key):
    import json
    g=GUIDES[c['code']][key]; l=c['code']; f=c['files']
    other='cmpwin' if key=='check' else 'check'
    secs=''.join(f'<h2>{h}</h2><p>{t}</p>' if not t.startswith('<') else f'<h2>{h}</h2>{t}' for h,t in g['secs'])
    faq=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in g['faq'])
    ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in g['faq']]}
    extra='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>\n'
    body=f'''<div class="wrap doc"><h1>{g['h1']}</h1><p class="lead2">{g['lead']}</p>
{secs}
<h2>{c['faq_h']}</h2>{faq}
<section class="card"><h2>Folvane</h2><p>{c['getsub']}. {c['meta']}</p><p>{storebtn(c)}</p></section>
<p><a href="{f[other]}">{c['g_cmp'] if other=='cmpwin' else c['g_chk']} →</a> · <a href="./">Folvane</a></p></div>'''
    return shell(c,key,g['title'],g['desc'],body,'document-page',extra)
