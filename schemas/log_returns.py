import pandera.pandas as pa


schema_log_returns = pa.DataFrameSchema(
    {
        'log_return': pa.Column(
            float,
            checks=[
                pa.Check.greater_than(-1),
                pa.Check.less_than(1),
            ],
            nullable=False,
        )
    },
    index=pa.Index(
        pa.DateTime,
        name='Date',
        checks=[
            pa.Check.in_range('2021-01-01', '2021-12-31'),
            pa.Check(lambda idx: idx.is_monotonic_increasing, element_wise=False)
        ]
    ),
    strict=True,
    coerce=True,

)