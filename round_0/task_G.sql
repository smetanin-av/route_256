SELECT
   "order".client_id, "order".id as order_id
FROM
   "order"
WHERE
   EXTRACT(MONTH FROM "order".created_at) = 9 AND
   EXISTS (
       SELECT null
       FROM product
       WHERE product.order_id = "order".id AND product.price > 200
       LIMIT 1
   )
ORDER BY
   "order".client_id,
   "order".id