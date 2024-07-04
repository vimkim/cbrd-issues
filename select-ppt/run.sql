select
  h.host_year,
  o.host_nation
from
  history h
  inner join olympic o on h.host_year = o.host_year
where
  o.host_year > 1950;
