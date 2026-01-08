---
layout: post
author: weezel
title: "Klimakiller Bitcoin"
categories: [umwelt, klima, mining]
image: assets/images/2023-08-18-klimakiller/cover.jpg
tags: [featured]
---

Wenn man der FAZ und seiner Quelle Alex de Vries Glauben schenkt, ist **Bitcoin ein ["Klimakiller"](https://www.faz.net/aktuell/finanzen/bitcoin-als-klimakiller-der-energieverbrauch-der-digitalwaehrung-18574317.html)**. 

Ein Killer? Wie der Terminator? Die Killermaschine **T-800**, die geschickt wurde, um Sarah Connor unerbittlich zu jagen und zu töten. „What the FAZ?[!](https://leo-mattes.com/wp-content/uploads/2022/12/BitSkit-I-dontt-give-a-FUD-Too-Bit-To-Fail.mp3)“ 

![](/assets/images/2023-08-18-klimakiller/1.jpg)

_Abb. 1: Der T-800 (CC BY 2.0)_


_Anscheinend ist Bitcoin in den Augen mancher der T-800 für unser Klima. Schauen wir uns an, ob an dieser Analogie vielleicht etwas dran ist._

Wenn man den ökologischen Fußabdruck von Bitcoin bewerten will, sollte man zunächst den Nutzen von Bitcoin und seinem Proof-of-Work (PoW) Konsensmechanismus verstehen. 

Bitcoin ist ein nicht-inflationierbarer **Wertspeicher** auf einem zensurresistenten, **globalen Zahlungsnetzwerk**, das jedem zugänglich ist.
Es ist gleichzeitig ein Werkzeug gegen finanzielle Zensur ([Bitcoin as a Nonviolent Tool Against State Financial Censorship](https://www.doria.fi/handle/10024/187407)) und gegen Geldmengeninflation
([1,2 Milliarden Menschen leben in Ländern mit zwei- oder dreistelliger Inflationsrate](https://news.bitcoin.com/1-2-billion-people-live-under-double-digit-inflation-many-have-found-escape-in-bitcoin-says-hrfs-alex-gladstein/)).

Für das Funktionieren des Bitcoin-Netzwerks ist PoW-Mining unerlässlich. 
Kritiker des hohen Energieverbrauchs des **Proof-of-Work** (Arbeitsnachweis) sehen in **Proof-of-Stake** (PoS) eine Alternative, die den Energieverbrauch senkt. Bei PoS werden neue Blöcke nicht basierend auf Rechenleistung erzeugt, sondern durch zufällig ausgewählte Validatoren des Netzwerkes. Je höher der Einsatz (Stake) an Coins, desto höher die Wahrscheinlichkeit ausgewählt zu werden und den Block Reward zu bekommen. Wer also viele Coins hat, kann viel staken und bekommt somit auch mehr neue Coins mit denen er wieder mehr staken kann. Die Vermögensverteilung konzentriert sich. Das ist problematisch, weil Vermögen und Netzwerkeinfluss in PoS-Netzwerken nicht, wie in PoW-Netzwerken, getrennt ist. Die **Gewaltenteilung des Bitcoin Netzwerks** in Netzwerkknotenbetreiber, Miner und Vermögende existiert in PoS Netzwerken nicht. Hier sind *staking node* Betreiber Vermögende, Mining- und Netzwerkknoten in Personalunion. Und weil man in PoS-Netzwerken mit mehr Coins mehr Staking Nodes betreiben kann, bedeutet die **Konzentration der Vermögensverteilung** auch eine **Zentralisierung des Netzwerkeinflusses**. Vereinfacht formuliert bedeutet PoS, dass die Reichen mehr Einfluss haben und diesen systemimmanent, risikolos weiter ausbauen können. Wer das gut findet, findet auch die FIFA oder Staatsoberhäupter mit mehr als 20 Jahren Amtszeit toll.

Der Einsatz der **realen Ressource Energie** bei PoW zum rechnerischen Nachweis (*computational proof*) hat weitere Vorteile gegenüber dem rein kryptographischen Nachweis (*cryptographic proof*) bei PoS. Da bei PoS lediglich die kryptographischen Schlüssel der gestakten Coins als Ressource zum Erstellen neuer Blöcke benötigt werden, könnte ein einzelner Dienstleister in einem einzigen Rechenzentrum das gesamte Netzwerk betreiben. Verglichen damit würde eine geografische Zentralisierung von Bitcoin-Minern lokal eine extrem hohe Stromlast Erzeugen, die ab einer gewissen Hashrate unwirtschaftlich und physikalisch zunehmend unrealistisch ist. Eine **geografische Dezentralisierung** ist somit systemimmanent.

Eine PoW Blockchain ist zudem fälschungssicherer und robuster gegenüber Störungen. Wenn ein Akteur versucht, Transaktionen zu manipulieren, müsste er alle vorherigen PoW Rechnungen schnell genug wiederholen, um die kontinuierlichen Arbeitsnachweise des Netzwerks zu übertreffen. Je mehr Blöcke nach einem Block gefunden wurden, desto fälschungssicherer sind die Transaktionen darin. Die **Summe der geleisteten Arbeit** dient zudem der Identifikation der längsten und damit echten Blockchain. Bei einem Ausfall kann sich das PoW-Netzwerk somit sofort auf die echte Chain einigen und das Zahlungsnetzwerk läuft weiter und ist nicht auf menschliche Koordination angewiesen.

**PoS ist kein gleichwertiger Ersatz** für Bitcoins extrem robusten PoW-Mechanismus, auch Nakamoto Konsens genannt. Ein Konsensmechanismus, der eine permanente und unumkehrbare Aufzeichnung von Transaktionen ohne zentrale Instanz und in maximaler Dezentralität ermöglicht und gleichzeitig die faire Verteilung neuer Bitcoin regelt. Dabei belohnt es die Miner für den Einsatz einer realen Ressource zur Sicherung des Netzwerks: Energie.




##  Energie

Davon nutzt das **Bitcoin Netzwerk** laut CCAF ca. **121 TWh pro Jahr**, was 0,19 % des weltweiten Energie- und 0,55% des weltweiten Stromverbrauchs ausmacht. ([Stand 09/2023, CCAF](https://ccaf.io/cbnsi/cbeci/comparisons)).

Ist das viel oder wenig für ein globales Zahlungsnetzwerk das heute schon Millionen von Menschen nutzen und Milliarden von Dollar Wert absichert?

Der **Wertspeicher Gold** und dessen Industrie verbauchen jährlich zwischen [130](https://ccaf.io/cbnsi/cbeci/comparisons) und [240](https://docsend.com/view/adwmdeeyfvqwecj2) TWh.
Den Verbrauch des globalen **Zahlungsnetzwerks der Banken** hat Michel Khazzaka in seinem wissenschaftlichen Paper 
“[Bitcoin: Cryptopayments Energy Efficieny](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4125499#)" 
untersucht.

Er berechnet und vergleicht den **Energieverbrauch des derzeitigen monetären Zahlungssystems** mit Bitcoin. Er betont, dass man alle Bereiche des klassischen monetären Zahlungssystems einbeziehen muss, die Bitcoin potentiell ersetzen kann: Erzeugung von Banknoten und Münzen, Bargeldmanagement an Bankautomaten, Kartenzahlungen, Bank- und Interbankengeschäfte. 

 
![](/assets/images/2023-08-18-klimakiller/2.png)

_Abb. 2: Vergleich des abgeschätzten, jährlichen Energieverbrauchs des Bitcoin Netzwerks mit Goldindustrie und Bankensystem. Quellen: [CCAF](https://ccaf.io/cbnsi/cbeci/comparisons), [Galaxy Digital Bericht](https://docsend.com/view/adwmdeeyfvqwecj2), [“Bitcoin: Cryptopayments Energy Efficieny”](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4125499#)_


**Anteil Erneuerbarer Energiequellen**

Der Unterschied zum Betreiben von Banken und Goldminen ist, dass **Bitcoin ausschließlich Strom** als Treibstoff nutzt. Prinzipiell ist Bitcoin Mining somit genauso klimaschädlich wie Elektroauto fahren. Der globale Strommix besteht immer noch zu [63% aus fossilen Energieträgern.](https://ourworldindata.org/electricity-mix)
Eine genaue Berechnung zum Anteil erneuerbarer Energien muss also einbeziehen, woher Mining Geräte ihren Strom beziehen und **welcher Strommix genutzt wird**. Während das Cambridge Centre for Alternative Finance (CCAF) einen durchschnittlichen Strommix mit 38% Erneuerbaren berechnet, kommt das Bitcoin Mining Council (BMC) auf 59% emissionsfreie Energiequellen.  Und weil das BMC quasi in Selbstauskunft berichtet und das CCAF eine unabhängige wissenschaftliche Einrichtung ist, wird medial eher der niedrigere Wert zitiert. Die [Berechnung des CCAF basiert](https://ccaf.io/cbnsi/cbeci/ghg/methodology) dabei auf der Länderzuordnung der Miner basierend auf deren IP-Adressen und dem jeweiligen Strommix des Landes (bzw. Region des Landes für China und die USA) und ist demzufolge nur eine grobe Näherung. 

Übrigens, die mit Abstand am meisten zitierten Zahlen zum Bitcoin Mining basieren auf den [zurecht kritisierten Berechnungen](https://bitcoinmagazine.com/business/not-science-digiconomist-bitcoin) des bei der niederländischen Zentralbank angestellten Datenanalysten ([Alex de Vries/Digiconomist](https://www.linkedin.com/in/alex-de-vries-a5b51349)) – die Quelle des [Killer-FAZ-Artikels](https://www.faz.net/aktuell/finanzen/bitcoin-als-klimakiller-der-energieverbrauch-der-digitalwaehrung-18574317.html).

Die vor kurzem veröffentlichte Analysemethode von [Karim Helmy](https://twitter.com/karimhelpme)  und [Coinmetrics](https://twitter.com/coinmetrics), in der Miningeräte (ASICs) über ihren Fingerprint identifiziert werden konnten, liefert über die Hashrate die zur Zeit [genauesten Rückschlüsse über die Energienutzung des Bitcoin Netzwerks](https://twitter.com/karimhelpme/status/1668592294440890368?s=20).
Im Vergleich von Cambridge und Digiconomist zeigt sich, dass Digiconomist zwischenzeitlich den Verbrauch um mehr als 100% überschätzt hat. Da Digiconomist den Bitcoinpreis als Grundlage für seine Berechnung nutzt, wird zum Zeitpunkt des medialen Hypes auch ein maßlos überschätzte Energienutzung errechnet, die dann direkt als schockierende Statements abgedruckt werden.

![](/assets/images/2023-08-18-klimakiller/3.png)

_Abb. 3: [Energieverbrauch des Bitcoin Netzwerks berechnet über Nonce-Analysemthode]( 
https://twitter.com/karimhelpme/status/1668592294440890368?s=20)_

Aber zurück zum Strommix. Da das Cambridge-Modell basierend auf dem Durchschnitt der jeweiligen Region für die meisten Miner einen 30 bis 40 prozentigen Anteil Erneuerbarer veranschlagt, werden dabei off-grid Anlagen nicht getrennt betrachtet. Das sind Anlagen, die nicht mit einem Stromnetz verbunden sind. Diese nutzen aber fast ausschließlich grüne Energiequellen.
Der [ESG-Analyst Daniel Batten](https://twitter.com/DSBatten) hat mit seinem [BEEST Model](https://batcoinz.com/BEEST/) (BITCOIN ENERGY & EMISSIONS SUSTAINABILITY TRACKER) diesen und weitere Faktoren mit einbezogen.
Nach seiner detaillierteren Berechnung verwendet das Bitcoin Netzwerk gegenwärtig mindestens **52,6% emissionsfreie Energie**. Das liegt weit über dem [globalen Durchschnitt von 36,7%]( 
https://ourworldindata.org/electricity-mix).

![](/assets/images/2023-08-18-klimakiller/4.png)

_Abb. 4: [Bitcoins emissionsfreie Energienutzung nach BEEST Model](https://batcoinz.com/BEEST/)_ 


Das CCAF-Modell berücksichtigt z.B. nicht die off-grid Miner, die nicht am Stromnetz sind (10,8%), Methan Flaring (1,0%) und die Abwanderung der Miner aus Kasachstan (1,8%). Unter Berücksichtigung dieser Ausschlüsse ergibt sich ein nachhaltiger Energiemix von 52,6 %. Diese Zahl stellt eine untere Schätzung von Daniel Batten dar und ist daher nicht unvereinbar mit der BMC-Studie, die 59,9 % emissionsfreie Energie ausweist.

Übrigens, die Arbeit von Daniel Batten und die Dialogbereitschaft der Verantwortlichen zeigt Wirkung. Zwischen Recherche und Verfassen dieses Artikels hat das CCAF seine Zahlen zum Energieverbrauch des Bitcoin Netzwerks deutlich nach unten korrigiert.
In ihrer [Stellungnahme](https://www.jbs.cam.ac.uk/2023/bitcoin-electricity-consumption/)
beschreiben sie im Detail, wie sie den Cambridge Bitcoin Electricity Consumption Index (CBECI) überarbeitet haben. 

 

![](/assets/images/2023-08-18-klimakiller/5.png)

_Abb. 5: Anteil nicht-fossiler Energien des Bitcoin Netzwerks mit Goldindustrie und Bankensystem. Quellen: [CCAF](https://ccaf.io/cbnsi/cbeci/ghg), [Daniel Batten](https://batcoinz.com/comparing-bitcoin-mining-to-other-industries-energy-mix/), [BMC](https://bitcoinminingcouncil.com/bitcoin-mining-council-survey-confirms-year-on-year-improvements-in-sustainable-power-and-technological-efficiency-in-h1-2023/), [Goldmoney Research Bericht](https://www.goldmoney.com/research/gold-price-framework-vol-2-the-energy-side-of-the-equation-part-ii), [Daniel Batten](https://batcoinz.com/comparing-bitcoin-mining-to-other-industries-energy-mix/)_

Der Bankensektor nutzt etwa den globalen Durchschnitt (wenn man den Pendelverkehr der Bankangestellten nicht mitrechnet). Während [die Goldindustrie nur zu 1/3 elektrifiziert arbeitet](https://www.goldmoney.com/research/gold-price-framework-vol-2-the-energy-side-of-the-equation-part-ii) und bei nur 13% landet.
Wie sehen die Treibhausgas-Emissionen im Vergleich aus?

## Emissionen

Basierend auf den Berechnungen von Batten oder dem CCAF liegt das Bitcoin Netzwerk bei [34-63 Mt/Jahr CO<sub>2</sub>e](https://batcoinz.com/accurately-dynamically-calculating-bitcoin-network-emissions/). Das entspricht ca. einem Tausendstel der globalen Treibhausgasemissionen.

**Wieviel verursacht der Wertspeicher Gold?** 

Von dem in 2022 [gefördertem Gold](https://de.statista.com/statistik/daten/studie/1171928/umfrage/verteilung-der-weltweiten-goldnachfrage-nach-sektoren/)
 wurde lediglich 7% von der Industrie verarbeitet. Der Rest wurde zu gleichen Teilen (je 46%) in der Schmuckbranche (46%) verarbeitet oder als direkter Wertspeicher (47%) u.a. von Zentralbanken gekauft. 
Die **Goldindustrie ist für ca. 126 Mt CO2e/Jahr** verantwortlich. Selbst wenn wir Schmuck als Wertspeicher ausklammern, liegen die Emissionen, die auf die reine Wertspeichernutzung (47%) von Gold zurückzuführen sind, bei ca. 60 Mt CO2e/Jahr und sind somit vergleichbar mit dem Bitcoin Netzwerk. 
Mit Gold kann ich aber nur sehr schlecht meinen Kaffee an der Ecke, meine Rechnungen in Deutschland oder Dienstleister in anderen Ländern bezahlen. 

**Wieviel verursacht das Bankensystem?**

Banken liegen laut der [Schätzung von Hass McCook]( https://hassmccook.medium.com/comparing-bitcoins-environmental-impact-f56b18014f64), die sich deckt mit dem berechneten Energieverbrauch von Michel Khazzaka und dem Anteil erneuerbarer Energien des globalen Strommixes, bei ca. **400 Mt CO2e/Jahr**. Das entspricht in etwa dem 10-fachen des Bitcoin Netzwerks. Das Paper von Michel Khazzaka [“Bitcoin: Cryptopayments Energy Efficieny”](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4125499#) überschlägt zudem, dass die Menge an Arbeitnehmern, die zu Bankfilialen pendeln müssen, diesen Wert vermutlich noch einmal mehr als verdreifachen würden.


![](/assets/images/2023-08-18-klimakiller/6.png)

_Abb. 6: Vergleich Treibhausgas-Emissionen des Bitcoin Netzwerks mit der Goldindustrie und dem Bankensystem. Quellen: [Daniel Batten](https://batcoinz.com/accurately-dynamically-calculating-bitcoin-network-emissions/), [CCAF](https://ccaf.io/cbnsi/cbeci/ghg), [“Gold and climate change” Bericht](https://www.gold.org/download/file/14316/gold-and-climate-change-current-and-future-impacts-3.pdf), [McCook Medium](https://hassmccook.medium.com/comparing-bitcoins-environmental-impact-f56b18014f64)_ 

Was ebenfalls nicht ungenannt bleiben sollte: In den Emissionswerten der Banken sind die Investitionen des Bankensektors in fossile Brennstoff Industrien noch nicht eingerechnet. 
Das Geld von Privatpersonen und Unternehmen liegt nicht nur passiv auf Bankkonten, um Zinsen zu erwirtschaften. Mit diesen Einlagen werden per Investition oder Kreditvergabe weitere Unternehmen finanziert, die weitere Emissionen verursachen.
Die Emissionen, die durch globale Finanzunternehmen auf diese Art verursacht werden, sind im Durchschnitt mehr als [700 Mal höher als ihre direkten betrieblichen Emissionen](https://cdn.cdp.net/cdp-production/cms/reports/documents/000/005/741/original/CDP-Financial-Services-Disclosure-Report-2020.pdf?1619537981).

Der **US-Bankensektor war in 2020** für die [Finanzierung von schätzungsweise **2000 Mt CO<sub>2</sub>e** verantwortlich](https://static1.squarespace.com/static/6281708e8ff18c23842b1d0b/t/6283204b3556a5125ce13b37/1652760661661/The+Carbon+Bankroll+Report+%285-17-2022%29.pdf). Das entspricht ca. der **50-fachen Emissionsmenge des Bitcoin Netzwerks**. Und weil manche Autoren gerne unangebrachte Ländervergleiche machen: Wäre der US-Bankensektor ein Land, wäre er allein der fünftgrößte Treibhausgas-Emittent ([Artikel: "bitcoin vs. banks"](https://bitcoinsozial.de/bitcoin_vs_banks/))


## Der Trend 

Über die letzten Jahre hat sich der Anteil erneuerbarer Energien für Bitcoin-Mining erhöht und liegt mittlerweile deutlich vor anderen Sektoren. Das ist möglich durch die steigende Anzahl von Mining Projekten, die gezielt erneuerbare Energie nutzen. 

[Daniel Batten zählt](https://twitter.com/DSBatten/status/1586551389492084736?s=20) mittlerweile **18 klimaneutrale** (Cleanspark, DPO, Blockfusion, Aspen, Bitfarms, Gryphon, Soluna, Hive, Cowa, Sato, Genesis, Iris, Gridshare, CyberianMine, DameTech, Arkon Energy, Blockstream/Block/Tesla, El Salvador + Tether) und **12 klimapositive** Unternehmen (Crusoe, GreenMiningCapital, ArthurMining, JAI, Giga, Nakamotor, Imperium Digital, Vespene, NodalPower, Scilling, Biomining).
Klimapositives Bitcoin Mining? Wie ist das möglich?
Die Emissionsreduktion des potenteren Klimagases Methan durch Verbrennung zum weniger potenten CO<sub>2</sub> mindert den Treibhauseffekt des freigesetzten Gases [(Forbes)]( 
https://www.forbes.com/sites/digital-assets/2023/07/08/bitcoin-network-to-reduce-more-emissions-than-its-energy-sources-produce/?sh=60e9ad5744d5).
Rein **rechnerisch** könnte das **Bitcoin-Netzwerk in wenigen Jahren** durch die Reduktion an Methanemissionen sogar **CO<sub>2</sub>-Equivalent-negativ** werden.

**Warum wird zunehmend mehr grünes Mining betrieben?**

Der Grund dafür kann Altruismus sein. Aber es gibt auch marktwirtschaftliche Anreize dies zu tun.
**Miner konkurrieren untereinander um eine unelastische Menge abbaubarer Bitcoin pro Zeiteinheit**. Das bedeutet, dass die Einnahmen für alle bereits arbeitenden Miner sinkt, wenn mehr Mining Geräte ans Netz gehen. 

Das ist anders als bspw. beim Goldabbau. Unternehmen 1 baut nicht weniger ab, nur weil Unternehmen 2 in einer anderen Mine mit mehr Aufwand mehr abbaut. Die Gold-Fördermenge ist elastisch. Wenn der Goldpreis steigt, steigt auch die Fördermenge.

Da Bitcoin-Miner durch den *difficulty adjusted PoW* Mechanismus um eine mathematisch festgelegte, konstante Menge abbaubarer Bitcoin pro Zeiteinheit konkurrieren, sinken die Einnahmen für alle bereits arbeitenden Miner, wenn mehr Mining Geräte ans Netz gehen. 
Die Einnahmen der Miner, die sie pro Rechenoperation (Hash) bekommen nennt sich Hashpreis (z.B. Dollar/TH) und dieser fällt kontinuierlich (egal ob in Bitcoin oder Dollar gemessen).

![](/assets/images/2023-08-18-klimakiller/7.png)

_Abb. 7: [Hashpreis der letzten 6 Jahre in Dollar pro Terahash (TH)](https://charts.woobull.com/bitcoin-hash-price/)_ 

Durch eine steigende Hashrate im Netzwerk wird der Hashpreis und somit die Einnahmen der Unternehmen immer geringer. Die **Nutzung von günstigen Energiequellen** wird somit immer wichtiger, um die Betriebskosten zu senken und profitabel zu bleiben. Gleichzeitig sind **erneuerbare Energiequellen** wie Solar- und Windenergie subventionsbereinigt seit ca. 10 Jahren [günstiger als fossile Energieträger]( https://www.lazard.com/research-insights/2023-levelized-cost-of-energyplus/). Die zunehmende Nutzung dieser Energiequellen im Mining-Prozess ist eine logische Folge. 

Als Faustregel gilt: Nur Strom, der 5 cent/kWh oder weniger kostet ist profitabel für Miner.
Würde fossile Energie nicht massiv subventioniert werden ([global 6,8% des BIPs](https://www.diw.de/de/diw_01.c.827737.de/nachrichten/schluss_mit_den_gigantischen_subventionen_fuer_kohle__oel_und_gas.html)) 
wären sie deutlich teurer und die Bitcoin Hashrate vermutlich schon heute deutlich grüner.

In der Debatte oft übersehen, aber ein wichtiger Sonderfall: **Am günstigsten ist Strom, wenn er keinen Abnehmer findet.** Das ist entweder der Fall, wenn der Erzeuger nicht am Stromnetz hängt und einspeisen kann („stranded energy“) oder es kurzfristig zu wenige Abnehmer für den gerade erzeugten Strom gibt. Letzteres wird zukünftig durch den [Ausbau erneuerbarer Energie häufiger der Fall sein](https://bitcoinsozial.de/ziemlich-beste-freunde/).
Um das Stromnetz stabil zu halten, müssen Solar- oder Windanlagen leider regelmäßig abgeschaltet werden und erzeugen so Kosten.

Mehr als [500 Mio. Pfund](https://www.power-technology.com/news/scottish-first-minister-calls-for-increased-energy-storage-following-curtailment-costs/) und [800 Mio. Euro]( https://taz.de/Zu-langsamer-Ausbau-der-Stromnetze/!5902431/) wurden im Jahr 2021 auf britischen bzw. deutsche Energierechnungen aufgeschlagen, weil die nationalen Stromnetze die [Windparks für die Drosselung („curtailment“)](https://www.cleanenergywire.org/news/germany-curtails-four-percent-renewable-power-production-due-grid-bottlenecks) bezahlen mussten. 

Die Stromnetze könnten den Erzeugern statt Ausgleichszahlungen eine Infrastrukturförderung zahlen, die den Anschluss von Mining Geräten finanziert. Diese würden erstens **kurzfristig überproduzierter Strom abnehmen können (Laststeuerung - „demand response“)** und zweitens **einen monetären Ausgleich für die Windparks schaffen**, die die Kosten nicht auf Energierechnungen aufschlagen müssen und drittens zur Dezentralisierung eines globalen Zahlungssystems beitragen. 

Energieerzeuger könnten ihren Output auf diese Art gezielt einsetzen. Das Mining Unternehmen Iris Energy hat das erkannt und setzt sich gezielt zwischen grüne Energie Erzeuger und Stromnetz. Da Preise im Stromnetz deutlich volatiler sind als der Bitcoinpreis, **gleichen sie dynamisch die Rentabilität des Bitcoin-Minings gegen die Strommarktpreise aus**. Ist der Strompreis bei geringem Bedarf niedrig, erzeugen sie Bitcoin. Ist der Strompreis hoch, schalten sie Miner ab und verkaufen den Strom ins Netz. Durch dieses automatische Hin- und Herschwenken des Outputs erreichen sie den höchsten Gewinn, glätten die Strommarktpreise und sind gute Kunden für die Erzeuger grüner Energie.  In der Praxis hat Iris Energy an seinem Standort in West Texas, mit Zugang zu viel überschüssiger Windenergie, damit im [August 2023 seine Einnahmen pro Bitcoin verdoppelt](https://irisenergy.gcs-web.com/news-releases/news-release-details/iris-energy-announces-monthly-investor-update-august-2023).

**Langfristig werden grüne Mining Unternehmen, die überschüssige oder gedrosselte Energie nutzen und bei Stromspitzen für das Abschalten bezahlt werden, den Hashpreis weiter drücken und somit die alten fossilen Miner verdrängen.**

Dass grünes Bitcoin-Mining zur **Nettodekarbonisierung der Energienetze** führen kann, schlussfolgerten im August 2023 sowohl das Paper „[Bitcoin’s Carbon Footprint Revisited](https://www.mdpi.com/2078-1547/14/3/35)", als auch KPMG.
Im [KPMG Bericht](https://advisory.kpmg.us/content/dam/advisory/en/pdfs/2023/bitcoins-role-esg-imperative.pdf)
bewerten Consolvo und Caron Bitcoin nach ESG-Maßstäben und geben zu E wie Environment an, dass Bitcoin die **Stabilisierung von Energienetzen, die Reduktion von Treibhausgasemissionen und das Betreiben nachhaltiger Wärmekopplung für Gewerbe- und Wohnimmobilien** verbessern kann.

Auch medial könnte sich der Wind also drehen, wenn diese Erkenntnisse in den Mainstream vordringen und sich weiter in der Praxis bewahrheiten.


## Bitcoin ist der T-800 

Der Klimawandel ist real und stellt uns vor eine große Aufgabe. Bitcoin läuft zwar zu mehr als 50% auf emissionsfreier Energie, aber ist noch CO<sub>2</sub>-positiv und somit in diesem Bereich noch Teil des Problems. 
Die Emissionswerte von Gold und Banken liegen in Summe jedoch mindestens zehn Mal höher. Verglichen dazu ist Bitcoin also sicher kein „Killer".

...Oder doch?
In **Terminator 2: Tag der Abrechnung** erleben wir einen T-800, der die Seiten wechselt und John Connor beschützt. Die Verwandlung des T-800 **vom Bösewicht zum Helden** markiert den Beginn seiner langen Reise. 

Das Bitcoin Netzwerk ist heute schon deutlich **klimaschonender als das, was es ersetzen kann**.
Wir könnten in den kommenden Jahrzehnten durch die Nutzung von Bitcoin, die Emissionswerte der Goldindustrie und des Bankensektors senken. 

Es wird sich zeigen, welche Rolle Bitcoin in der Zukunft spielen wird. Das Drehbuch liegt in unserer Hand. 

![](/assets/images/2023-08-18-klimakiller/Ende.png)

