WITH "checks_all" AS (
    SELECT
        "order"."client_id", SUM("cnt" * "price") as "total"
    FROM
        "order" INNER JOIN "product" ON "order"."id" = "product"."order_id"
    GROUP BY
        "order"."id",
        "order"."client_id"
), "checks_ge_1th" AS (
    SELECT
        "client_id"
    FROM
        "checks_all"
    WHERE
        "total" > 1000
    GROUP BY
        "client_id"
    HAVING
        COUNT(*) >= 2
)
SELECT
    "client_id" as "id", AVG("total") as avg_order
FROM
    "checks_all"
WHERE
    "client_id" in (SELECT "client_id" from "checks_ge_1th")
GROUP BY
    "client_id"
ORDER BY
   "client_id"