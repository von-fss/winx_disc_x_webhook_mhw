import sqlite3
con = sqlite3.connect("winx_webhook.db")

cur = con.cursor()

teste = cur.execute("select * from last_posts")

print(teste.fetchall())

[(1899146829461168452, "The Ajarakan hunter armor's silhoutte resembles flames, while the design draws on elements of Japanese legends. The Palico armor is heavily inspired by guardian dog statues (Koma-inu) found in Japan, to express the Palico's duty to protect hunters. #MHWilds https://t.co/C9bxaozZHd", '2025-03-10T17:14:23.000Z', 1), 
 (1899555283636036040, 'What are your current primary and secondary weapons in #MHWilds? https://t.co/Ik4U969r42', '2025-03-11T20:17:26.000Z', 1), 
 (1899625399191060987, '📜 EVENT QUEST 📜\n\nA Tempered Chatacabra stands between you and a pile of Hard and Advanced Armor Spheres in "Tongue-Tied"!\n\nThis quest joins last week\'s "Kut-Ku Gone Cuckoo" that has special headgear material rewards!\n\nBoth available until Mar. 18, 4:59pm PT / 23:59pm GMT. https://t.co/GTvRPIPuhQ', '2025-03-12T00:56:03.000Z', 1), 
 (1899777331025072328, 'Hunters! Did you know we have some dedicated regional accounts for Monster Hunter? \n\nFR: @MH_Officiel_FR\nDE: @DEMonsterHunter\nES: @ESMonsterHunter\nAR: @MonsterHunterAR\nPL: @MonsterHunterPL\n\nIf any catch your interest, drop them a follow for localised content and more! https://t.co/YwRdoIu7Qk', '2025-03-12T10:59:46.000Z', 1), 
 (1899868262973780255, 'Since Ajarakan fights with powerful punches, the shape of a fist is included in the Sword &amp; Shield, almost like a gauntlet. Fighting with this set looks as if the hunter is punching with a flame-clad left fist, and guarding with their right arm. #MHWilds https://t.co/NmM9Ybbt9X', '2025-03-12T17:01:06.000Z', 1)]