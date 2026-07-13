select
    s.size,
    c.color
from
    (values
        ('Small'),
        ('Medium'),
        ('Large')
    ) AS s(size)
cross join
    (values
        ('Red'),
        ('Blue'),
        ('Green')
    ) as c(color);