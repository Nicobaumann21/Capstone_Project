# F Datenqualität & NULL-Handling (Pflicht)

Mindestens **eine Query oder Analyse** muss zeigen:

- wie NULL-Werte entstehen
- wie sie korrekt gefiltert, ersetzt oder gezählt werden
- warum dies in echten Datenbanken relevant ist

# **F Datenqualität & NULL-Handling**

In echten Datenbanken tauchen NULL-Werte häufig auf. Sie entstehen z. B., weil:

- Daten noch nicht erfasst wurden (`leave_date` für aktive Mitarbeiter)
- Ein Fremdschlüssel noch nicht gesetzt wurde (`assignee_id` bei unassigned Tasks)
- Optionaler Input fehlt (`industry` bei manchen Kunden)

NULL ist **kein Wert**, sondern ein **Fehler-/Leerzustand**. Viele Aggregationen und JOINs müssen damit umgehen.

---

## **1. Beispiel: NULL-Werte erkennen**

### **Problemstellung:**

Wir wollen herausfinden, wie viele Mitarbeiter **noch keinem Team zugeordnet sind** und wie viele Tasks **keinen Assignee haben**.

```sql
EXPLAIN ANALYZE

SELECT COUNT(*) AS num_employees_without_team
FROM employees
WHERE team_id IS NULL;

```

### **Step by Step Erklärung:**

1. **COUNT(*)** zählt alle Zeilen, die das Kriterium erfüllen.
2. **IS NULL** filtert explizit NULL-Werte.
3. **Warum wichtig:**
    - NULLs in `team_id` → Mitarbeiter werden in Team-Reports fehlen
    - NULLs in `assignee_id` → Tasks werden nicht korrekt zugeordnet

### **Workload & Performance:**

- `employees`: 
- `tasks`: 
- Vollständiger Scan nötig, da keine Filterung möglich ohne Index auf NULL-Spalte
- Erwartete Dauer: einige Millisekunden bis Sekunden

```sql
Aggregate  (cost=394.02..394.03 rows=1 width=8) (actual time=0.679..0.680 rows=1 loops=1)
  ->  Seq Scan on employees  (cost=0.00..394.02 rows=1 width=0) (actual time=0.676..0.676 rows=0 loops=1)
        Filter: (team_id IS NULL)
        Rows Removed by Filter: 20202
Planning Time: 0.051 ms
Execution Time: 0.697 ms
```

Wie haben Keine NULL werte bei Mitarbeiter ohne Teams weshalb ich beispielsweise ein Paar einsetze um zu zeigen wie man Filtern kann 

```sql
INSERT INTO employees (name, team_id)
VALUES
  ('Test1', NULL),
  ('Test2', NULL),
  ('Test3', NULL),
  ('Test4', NULL),
  ('Test5', NULL);

```

```sql
Aggregate  (cost=394.02..394.03 rows=1 width=8) (actual time=0.600..0.601 rows=1 loops=1)
  ->  Seq Scan on employees  (cost=0.00..394.02 rows=1 width=0) (actual time=0.596..0.596 rows=5 loops=1)
        Filter: (team_id IS NULL)
        Rows Removed by Filter: 20202
Planning Time: 0.050 ms
Execution Time: 0.617 
```

---

## **Schritt 3: NULL-Werte filtern**

Nur die Mitarbeiter ohne Team anzeigen:

```sql
SELECT *
FROM employees
WHERE team_id IS NULL;

```

- `IS NULL` filtert explizit die fehlenden Werte
- Ergebnis: die 5 Test-Mitarbeiter

---

## **Schritt 4: NULL-Werte zählen**

Anzahl der Mitarbeiter ohne Team:

```sql
SELECT COUNT(*) AS num_employees_without_team
FROM employees
WHERE team_id IS NULL;

```

- Zeigt `5` an
- So erkennt man sofort, wie viele Daten „fehlen“

---

## **Schritt 5: NULL-Werte ersetzen**

Mitarbeiter ohne Team einem Default-Team zuweisen (z. B. Team 1):

```sql
UPDATE employees
SET team_id = 1
WHERE team_id IS NULL;

```

- Danach gibt es **keine NULL-Werte mehr**
- Prüfen:

```sql
SELECT *
FROM employees
WHERE team_id IS NULL;

```

Ergebnis = **0 Zeilen**

---

## **Schritt 6: Warum das wichtig ist**

- **Datenqualität:** NULL-Werte können Analysen verfälschen, z. B. Summen oder Durchschnittswerte.
- **Business-Logik:** Manche Prozesse (z. B. Zuweisung von Aufgaben) dürfen keine NULLs enthalten.
- **Reports & Dashboards:** Fehlen von NULL-Handling kann falsche Zahlen liefern.


