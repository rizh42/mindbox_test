from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

def get_products_with_categories(
    products_df: DataFrame,
    categories_df: DataFrame,
    product_category_links_df: DataFrame
) -> DataFrame:
    
    products_with_categories = (
        products_df.join(
            product_category_links_df,
            on="product_id",
            how="left"
        )
        .join(
            categories_df,
            on="category_id",
            how="left"
        )
        .select(
            col("product_name"),
            col("category_name")
        )
    )
    
    return products_with_categories

def get_products_with_categories_alternative(
    products_df: DataFrame,
    categories_df: DataFrame,
    product_category_links_df: DataFrame
) -> DataFrame:
    product_category_pairs = (
        product_category_links_df.join(
            products_df,
            on="product_id",
            how="inner"
        )
        .join(
            categories_df,
            on="category_id",
            how="inner"
        )
        .select(
            col("product_name"),
            col("category_name")
        )
    )
    
    products_without_categories = (
        products_df.join(
            product_category_links_df,
            on="product_id",
            how="left_anti" 
        )
        .select(
            col("product_name"),
            lit("No Category").alias("category_name")
        )
    )
    
    return product_category_pairs.union(products_without_categories)