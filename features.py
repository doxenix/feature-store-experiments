from datetime import timedelta

import pandas as pd

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
)

from feast.types import Float32, Float64, Int64, Int32
from feast import FileSource


user = Entity(name="user", join_keys=["user_id"])

transaction_source = FileSource(
    name="transaction_orders",
    path="orders_data_10f.parquet",
    event_timestamp_column="event_timestamp"
)

orders_fv = FeatureView(
    name="transaction_orders_fv",
    entities=[user],    
    schema=[
        Field(name="total_product_orders_by_user", dtype=Float32),
        Field(name="last_ordered_in", dtype=Float32),
        Field(name="order_number", dtype=Float32),
        Field(name="days_since_prior_order", dtype=Float32),
        Field(name="reorder_propotion_by_user", dtype=Float32),
        Field(name="reorder_percentage", dtype=Float32),
        Field(name="second_time_percent", dtype=Float32),
        Field(name="avg_since_order", dtype=Float32),
        Field(name="total_unique_product_by_user", dtype=Int32),
        Field(name="average_order_size", dtype=Float32),
    ],
    online=True,
    source=transaction_source,
)

transaction_stats_v1 = FeatureService(
    name="transaction_stats_v1",
    features=[orders_fv]
)
