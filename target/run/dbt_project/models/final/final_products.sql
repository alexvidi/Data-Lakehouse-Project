
  create or replace   view MY_DATABASE.MY_SCHEMA.final_products
  
   as (
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
    FROM MY_DATABASE.MY_SCHEMA.int_products
)

SELECT * FROM final_products
  );

