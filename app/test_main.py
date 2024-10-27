import datetime

import pytest

from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,"
    "mocked_date,"
    "expected_result", [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 10, 26),
                    "price": 600
                }
            ],
            datetime.date(2024, 10, 27),
            ["salmon"],
            id="test product with expiration date equals yesterday is outdated"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 10, 25),
                    "price": 600
                }
            ],
            datetime.date(2024, 10, 25),
            [],
            id="test product with expiration date equals today is not outdated"
        )
    ]
)
def test_should_return_correct_list_of_outdated_products(
        mocked_date: datetime.date,
        expected_result: list,
        products: list
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.return_value = mocked_date
        assert outdated_products(products) == expected_result
