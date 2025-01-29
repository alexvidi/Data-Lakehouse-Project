WITH final_products AS (
    SELECT
        id,
        product_name,
        price,
        category,
        brand,
        stock,
        stock_level,
        CURRENT_TIMESTAMP AS load_date  
    FROM {{ ref('int_products') }}
)

SELECT * FROM final_products
