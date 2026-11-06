import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (existing behaviour, must not change)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit(self):
        """Passing service='standard' must return the same result as the default."""
        self.assertEqual(
            shipping_quote(2, "local", service="standard"),
            shipping_quote(2, "local"),
        )

    # ------------------------------------------------------------------
    # Express service ($7 surcharge on top of standard)
    # ------------------------------------------------------------------
    def test_express_local(self):
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_surcharge_is_seven(self):
        """Express surcharge is always $7 regardless of weight or zone."""
        for zone in ("local", "regional"):
            for weight in (1, 5, 10.5):
                with self.subTest(zone=zone, weight=weight):
                    diff = (
                        shipping_quote(weight, zone, service="express")
                        - shipping_quote(weight, zone, service="standard")
                    )
                    self.assertAlmostEqual(diff, 7.0)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
