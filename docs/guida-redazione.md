# Guida per la redazione — Clean Air Litigation Database

Guida operativa per chi inserisce e aggiorna i casi. Non serve alcuna competenza tecnica: si lavora da un pannello web con moduli a campi.

## Come si entra

1. Aprire `https://<indirizzo del sito>/admin/` nel browser.
2. Accedere con la propria email e password (l'invito arriva per email; il login con Google/Microsoft è disponibile se abilitato).
3. Nella colonna di sinistra c'è l'unica raccolta, **Cases**: l'elenco di tutte le schede.

## Aggiungere un caso

1. Cliccare **New Case**.
2. Compilare i campi (sotto, il significato di ciascuno).
3. Cliccare **Publish → Publish now**.

La pubblicazione è immediata: entro circa un minuto il sito si rigenera da solo con il nuovo caso. Non c'è una fase di bozza: ogni salvataggio pubblicato va online.

## Il significato dei campi

| Campo | Che cosa scrivere |
|---|---|
| URL slug | L'identificativo dell'indirizzo web della scheda, in minuscolo con trattini (es. `commission-v-italy-pm10`). Si sceglie una volta e **non si cambia più**: link e citazioni dipendono da questo. |
| Case name | Il nome completo del caso come deve apparire sul sito. |
| Filing year | L'anno in cui è stato avviato il primo procedimento. |
| Status | Testo libero mostrato sulla scheda (es. `Decided`, `Pending`, `Decided — execution pending`). Il filtro per stato raggruppa in base alle parole: usare `pending` per i pendenti e `enforcement`/`execution` per le fasi esecutive. |
| Geography → Country | Il paese dei fatti, in inglese, col nome usato dalla mappa (es. `Italy`, `United Kingdom`). |
| Geography → Country code | Il codice numerico a 3 cifre che aggancia il caso alla mappa: **è l'unico campo delicato**. La tabella completa è in [`codici-paesi.md`](codici-paesi.md). I più frequenti: Italia 380, Francia 250, Germania 276, Regno Unito 826, Belgio 056, Spagna 724, Paesi Bassi 528, Polonia 616, Stati Uniti 840. |
| Forum → Type | Chi decide: corti nazionali (`Domestic courts`), Corte di giustizia UE o Corte EDU. Per i casi CGUE/CEDU il paese resta quello dei fatti: il caso compare sia sulla mappa sia nel pannello delle corti internazionali. |
| Forum → Deciding bodies | Descrizione libera dell'autorità o delle autorità (es. «Court of Justice of the European Union (Grand Chamber), on a reference from …»). |
| Docket number(s) | Numero/i di ruolo o di ricorso. |
| At issue | Una o due frasi: di che cosa tratta il caso. |
| Abstract | L'abstract originale della redazione. |
| Topics | Parole chiave tematiche, una per riga (es. `PM10`, `Air quality plans`). |
| Proceedings | Una riga per passaggio processuale, in ordine cronologico: data (GG/MM/AAAA), organo, atto, esito, e — se disponibile — il link al testo dell'atto. |
| Sources | Le fonti del caso: citazione completa e, se disponibile, il link (EUR-Lex, HUDOC, ArianeWeb, climatecasechart, siti delle corti…). |

## Correggere o eliminare un caso

Dall'elenco **Cases** si apre la scheda, si modifica e si ripubblica. **Delete entry** elimina la scheda (e il caso sparisce dal sito al rebuild). Non cambiare mai lo slug di una scheda già pubblicata: si romperebbero i link già citati.

## Se qualcosa va storto

- Il pannello segnala in rosso i campi non validi e non lascia pubblicare finché non sono corretti.
- Se una scheda pubblicata contenesse comunque un errore strutturale, il sito **non** si aggiorna e resta online l'ultima versione buona: nessun errore redazionale può «rompere» il sito. In quel caso segnalare l'ultima modifica fatta a chi gestisce il repository.
