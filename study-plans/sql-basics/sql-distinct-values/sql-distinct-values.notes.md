Final rule:

```
DISTINCT column
→ removes duplicate values
→ NULL is kept once
```



```
COUNT(column)
→ counts non-NULL values
→ ignores NULL
```



```text
COUNT(DISTINCT column)
→ removes duplicates
→ counts the unique non-NULL values
→ ignores NULL
```

And:

```text
COUNT(*)
→ counts every row
→ NULL does not matter
```

The easiest thing to remember is:

> **DISTINCT removes duplicates. COUNT(column) ignores NULL.**



---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---



> **Aggregate functions generally ignore **`NULL`** values.**

- `COUNT(column)` → Ignores `NULL`
- `SUM(column)` → Ignores `NULL`
- `AVG(column)` → Ignores `NULL`
- `MIN(column)` → Ignores `NULL`
- `MAX(column)` → Ignores `NULL`
- `COUNT(DISTINCT column)` → Ignores `NULL` and removes duplicates
- `COUNT(*)` → Counts **all rows**, including rows containing `NULL`

So  main rule to remember is:

> **Aggregate functions ignore NULLs — except **`COUNT(*)`**, which counts rows.**