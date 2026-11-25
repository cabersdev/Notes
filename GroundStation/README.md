# Indice di studio — Ground Station
## Manuale per la progettazione di sistemi di acquisizione, trasporto e analisi di telemetria
---

## Parte I — Il sistema ground station

1. **Che cos'è una ground station**
2. **Tassonomia dei sistemi**: full-scale, small mission, portable, reti distribuite; criteri di scala e di complessità
3. **Requisiti e vincoli**: affidabilità, latenza, jitter, throughput, osservabilità, riproducibilità, sicurezza, costo
4. **Il ciclo di vita**: progettazione, sviluppo, validazione, operazione, manutenzione, dismissione
5. **Modelli di riferimento**: architetture a strati, a servizi, event-driven, data-centric; quando adottarli e quando no

---

## Parte II — Il dato e la sua catena

6. **Dalla grandezza fisica al valore digitale**: sensore, condizionamento, conversione, calibrazione; catena dell'incertezza
7. **Modulazione e canale**: famiglie di modulazione, capacità del canale, probabilità di errore; il rumore come fenomeno statistico
8. **Dal segnale al frame**: ricezione, demodulazione, sincronizzazione, framing; il frame come unità di dato
9. **Protocolli di framing**: standard spaziali, radioamatoriali, custom; criteri di scelta e confronto
10. **Integrità del dato**: rilevamento e correzione degli errori; CRC, checksum, FEC; codici concatenati
11. **Frammentazione, riassemblaggio e perdite**: sequenze, contatori, strategie di gestione; il dato mancante come categoria statistica
12. **Tempo e sincronizzazione**: timestamp, fonti di tempo, latenza, jitter, skew; allineamento multi-sorgente
13. **Incertezza del dato**: fonti, propagazione, dichiarazione; dal dato grezzo alla stima con intervallo

---

## Parte III — Architetture per la ground station

14. **Dal monolite ai servizi**: accoppiamento, coesione, confini; quando un monolite è la scelta giusta
15. **Architetture event-driven**: eventi, comandi, query; disaccoppiamento temporale e spaziale
16. **Publish/subscribe**: modello, semantica, garanzie; il broker come componente critico
17. **Code e log distribuiti**: message queue, log append-only, partizionamento; confronto con pub/sub
18. **Data pipeline**: ingestion, processing, storage, serving; batch vs stream; lambda e kappa architecture
19. **Pattern di resilienza**: retry, circuit breaker, backpressure, dead letter queue, idempotenza
20. **Consistenza e garanzie**: at-most-once, at-least-once, exactly-once; costi e compromessi

---

## Parte IV — Protocolli e middleware di comunicazione

21. **Criteri di scelta di un protocollo**: latenza, throughput, affidabilità, complessità, ecosistema
22. **MQTT**: modello pub/sub, topic, QoS, retained, sessioni, LWT; quando è la scelta giusta e quando no
23. **AMQP**: code, exchange, routing; confronto con MQTT
24. **Kafka**: log distribuito, partizioni, consumer group; il secondo miglio della pipeline
25. **Redis Pub/Sub e Streams**: latenza, persistenza, consumer group
26. **ZeroMQ e DDS**: pattern di messaggistica, contesti real-time, applicazioni critiche
27. **REST, gRPC, WebSocket**: comunicazione sincrona, streaming, controllo; quando servono
28. **Protocolli di serializzazione**: testo, JSON, binario, schema; impatto su banda, latenza, evoluzione
29. **Confronto trasversale**: mappa decisionale tra i protocolli; criteri per non scegliere per moda

---

## Parte V — Persistenza e visualizzazione

30. **Storage per telemetria**: file, colonnari, time-series, documenti; criteri di scelta
31. **Time-series database**: modello dei dati, indici temporali, retention, downsampling, compressione
32. **Schema e versionamento del dato**: evoluzione senza rotture, compatibilità, migrazioni
33. **Visualizzazione real-time**: dashboard, console, allarmi; il Time Conductor e l'allineamento temporale
34. **Visualizzazione storica e analitica**: query, aggregazioni, report; dal dato alla decisione
35. **Integrazione con strumenti esterni**: API, export, interoperabilità; evitare i silos

---

## Parte VI — Deployment e infrastruttura

36. **Dal server dedicato all'edge**: modelli di deployment, vincoli di risorse, tolleranza ai guasti
37. **Sistemi operativi per ground station**: scelte, stabilità, compatibilità, tooling, sicurezza
38. **Containerizzazione**: isolamento, riproducibilità, immagini, registry; limiti e costi
39. **Orchestrazione**: Compose, Kubernetes, swarm; quando servono e quando sono overkill
40. **Supervisione dei servizi**: init system, restart policy, dipendenze, logging di sistema
41. **Gestione della configurazione**: file, segreti, ambienti; separazione tra codice e configurazione
42. **Hardware per ground station**: single-board computer, server, SDR, periferiche; scelte e compromessi
43. **Riproducibilità dell'ambiente**: dall'ambiente “che funziona” all'ambiente ricostruibile

---

## Parte VII — Osservabilità e affidabilità

44. **Logging strutturato**: livelli, contesto, correlazione, formati; dal log al dato interrogabile
45. **Metriche**: cosa misurare, con quale granularità, con quale costo
46. **Tracing distribuito**: seguire una richiesta attraverso i servizi; strumenti e pattern
47. **Health check e readiness**: distinguere “vivo” da “pronto”; impatto sul deployment
48. **SLO, SLI, error budget**: definire l'affidabilità in modo misurabile
49. **Test di resilienza**: caos engineering, fault injection, scenari di guasto; validare l'ipotesi di robustezza
50. **Replay e post-mortem**: ricostruire una sessione, analizzare un incidente, imparare dal fallimento

---

## Parte VIII — Statistica e modelli per la telemetria

51. **Il dato come variabile aleatoria**: modelli probabilistici, verifica delle assunzioni, robustezza
52. **Stima**: massima verosimiglianza, stimatori, proprietà; dal campione al parametro
53. **Statistiche mobili e finestre**: media, varianza, scelta della finestra; effetto su latenza e potenza
54. **Test d'ipotesi e decisioni**: test unilaterali, intervalli di confidenza, scelta di α, potenza
55. **Monitoraggio sequenziale**: multiple testing, correzioni, carte di controllo (EWMA, CUSUM), ARL
56. **Anomaly detection**: metodi statistici, basati su modello, machine learning; interpretabilità e contesto operativo
57. **Valutazione delle decisioni**: confusion matrix, precision/recall/F1, ROC-AUC, latenza di rilevamento, chattering
58. **Ground truth e validazione**: scenari controllati, simulazione, dati sintetici; come si valida una regola
59. **Dati mancanti**: meccanismi di missingness, bias, strategie di imputazione e di analisi
60. **Dal dato alla decisione**: il ponte tra statistica e operazioni; documentare l'incertezza

---

## Parte IX — Sicurezza

61. **Superficie di attacco di una ground station**: link radio, rete, servizi, supply chain
62. **Autenticazione e autorizzazione**: chi può fare cosa, su quale canale
63. **Cifratura**: link, trasporto, dati a riposo; costi e limiti
64. **Sicurezza dei protocolli**: ACL, certificati, rotazione delle chiavi; configurazioni sicure di default
65. **Validazione dei comandi**: perché un comando malformato è un rischio; difese e verifiche
66. **Monitoraggio e auditing**: rilevare un'anomalia di sicurezza; log come prova

---

## Parte X — Casi di studio e sintesi

67. **Ground station per missioni real-time**: pattern, tecnologie, lezioni apprese
68. **Ground station per missioni store-and-forward**: pattern, tecnologie, lezioni apprese
69. **Reti distribuite di ground station**: coordinamento, eterogeneità, qualità del dato
70. **Framework di mission control**: quando adottarli, quando scrivere custom; criteri di valutazione
71. **Anti-pattern ricorrenti**: monoliti, logging assente, allarmi senza isteresi, dati mancanti ignorati, over-engineering
72. **Principi guida trasversali**: separazione dei livelli, componenti standard, complessità solo dove è specifica, statistica come parte dell'architettura
73. **Mappa delle decisioni**: una sintesi dei criteri di scelta emersi in tutto il manuale