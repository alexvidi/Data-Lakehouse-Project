WITH cleaned_products AS (
    SELECT DISTINCT  -- 
        id,
        UPPER(product_name) AS product_name,
        ROUND(price, 2) AS price,
        category,
        brand,
        stock,
        CASE 
            WHEN stock > 50 THEN 'High Stock'
            WHEN stock BETWEEN 20 AND 50 THEN 'Medium Stock'
            ELSE 'Low Stock'
        END AS stock_level
    FROM {{ ref('stg_products') }}
)

SELECT * FROM cleaned_products

