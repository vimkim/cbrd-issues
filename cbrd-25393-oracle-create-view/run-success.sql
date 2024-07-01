CREATE view a_view (
    "ID", "PHONE", "EXTRA" varchar
) AS
SELECT
id,
phone,
NULL AS extra
FROM a_tbl;

