from src.risk_manager import RiskManager


def test_pip_size_standard_pair():

    manager = RiskManager()

    assert (
        manager.pip_size("EURUSD")
        == 0.0001
    )


def test_pip_size_jpy_pair():

    manager = RiskManager()

    assert (
        manager.pip_size("USDJPY")
        == 0.01
    )


def test_daily_loss_not_exceeded():

    manager = RiskManager()

    manager.starting_equity = 1000

    assert (
        manager.daily_loss_exceeded(995)
        is False
    )


def test_daily_loss_exceeded():

    manager = RiskManager()

    manager.starting_equity = 1000

    assert (
        manager.daily_loss_exceeded(970)
        is True
    )
