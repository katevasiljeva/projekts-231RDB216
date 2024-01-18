# projekts-231RDB216
## Projekta uzdevums:
Projekta uzdevums ir izveidot programmu, kas automatizē kādu no ikdienas uzdevumiem. Uzdevums, ko manis izstrādātais projekts automatizē, ir dzīvokļu sludinājumu apskatīšana un atbildēšana uz tiem. Izvēlējos apstrādāt vietnē ss.lv publicētos dzīvokļu sludinājumus, apkopojot tos excel failā.
## Programmas darbība:
Programma, pirmkārt, atver sludinājumu vietni ss.lv. Sludinājumu izvēlnē tiek atlasīta sadaļa "Dzīvokļi", pēc tam "Rīga", pēc tam "Vecrīga". Lai padarītu programmu lietderīgāku, tiek atlsaīti sev piemērotāki sludinājumi, kas ietilpst konkrētā cenas (250 - 600 eur) un citu kritēriju (dzīvoklis atrodas ne zemāk kā 2. stāvā) kategorijā. Programma atrod katra individuālā sludinājuma id, un saglabā tos sarakstā, no saraksta izņemot katru tukšo vērtību. Tad, izmantojot for ciklu, programma secīgi apmeklē sludinājumu, sludinājuma lapā atrod informāciju par cenu, ielu, platību, istabu skaitu un stāvu, pievienojot šīs vērtības sākotnēji tukšā sarakstā "info", un pēc tam sarakstu "info" pievieno sarakstam "dzīvokļi", kas satur sarakstus ar informāciju par katru individuālo dzīvokli. Sākotnēji vēlējos iekļaut arī sludinājumā norādīto kontaktinformāciju, tomēr tai nav iespējama piekļuve, neizpildot reCAPTCHA pārbaudi, padarot programmu mazāk vērtīgu uzdevuma automatizēšanā. Pēc tam, kad norādītās vērtības ir atrastas un pievienotas sarakstiem, programma atgriežas pie dzīvokļu sludinājumu saraksta un apmeklē nākamo sludinājumu. 

Programmā esmu ievietojusi arī kodu, kas, apskatot individuālo sludinājumu, noklišķina sadaļu "Nosūtīt e-pastu", ailītē "Jūsu e-pasts:" ieraksta "vards.uzvards@gmail.com", ailītē "Jūsu vārds:" ieraksta "Kate Vasiļjeva", ailītē "Jūsu tālrunis:" ievada "29123456" un ailītē "Ziņojuma teksts:" ievada "Labdien! Vai būtu iespējams apskatīt dzīvokli? Ar cieņu, Kate Vasiļjeva", katru rindiņu atdalot.
Kad nepieciešamās vērtības izgūtas un katrs sldinājums ir apskatīts, programma izgūtos un sarakstā ievietotos datus attēlo excel failā.
Projekta iesniegumam pievienoju nelielo video, kurā uzskatāmi attēlota programmas darbība, kā arī ekrānuzņēmumu no programmas izveidotā excel faila.
## Izmantotās bibliotēkas:
Selenium tiek izmantots tīmekļa skrāpēšanai. Tas ļauj vietnē atrast dažādus elementus, iegūt datus un nodrošina mijiedarbību ar tīmekļa lapu, kur webdriver tiek izmantots, lai darbibas īstenotu Chrome pārlūkprogrammā un By tiek izmantots, lai atrastu konkrētus elementus.

Bibliotēka time tiek izmantota, lai konkrētos brīžos uz noteiktu ilgumu nopauzētu programmas darbību un ļautu ielādēties vietnes saturam pirms nākamās darbības veikšanas.

Bibliotēka xlsxwriter ļauj izveidot jaunu excel failu un rediģēt to.
