WITH raw_products AS (
    SELECT
        id,
        title AS product_name,
        price,
        category,
        brand,
        stock
    FROM {{ source('my_database', 'PRODUCTS') }}
)

SELECT * FROM raw_products
