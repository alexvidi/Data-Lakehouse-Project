
  create or replace   view MY_DATABASE.MY_SCHEMA.stg_products
  
   as (
    WITH raw_products AS (
    SELECT
        id,
        title AS product_name,
        price,
        category,
        brand,
        stock
    FROM MY_DATABASE.MY_SCHEMA.PRODUCTS
)

SELECT * FROM raw_products
  );

