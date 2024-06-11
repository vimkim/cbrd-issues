CREATE view a_view (
    "ID", "PHONE", "EXTRA"
) AS
SELECT
id,
phone,
NULL AS extra
FROM a_tbl;

