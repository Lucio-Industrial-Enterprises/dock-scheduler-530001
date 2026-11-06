# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in USD.

| Parameter | Values | Notes |
|-----------|--------|-------|
| `weight_kg` | positive float | parcel weight |
| `zone` | `"local"`, `"regional"` | delivery zone |
| `service` | `"standard"` *(default)*, `"express"` | express adds a flat $7.00 surcharge |

Unknown zones or services raise `ValueError`.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```bash
# Standard quote – 3 kg to regional zone
python -m warehouse.cli 3 regional
# $12.50

# Express quote – same parcel
python -m warehouse.cli 3 regional --service express
# $19.50
```
