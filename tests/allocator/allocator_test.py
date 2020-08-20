""" Tests for skale/allocator/allocator.py """

import time
from skale.wallets.web3_wallet import generate_wallet

TEST_VESTING_SLIFF = 6
TEST_TOTAL_VESTING_DURATION = 36
TEST_VESTING_STEP_TIME_UNIT = 2
TEST_VESTING_TIMES = 6
TEST_CAN_DELEGATE = False
TEST_IS_TERMINATABLE = True

POLL_INTERVAL = 2


def _add_test_plan(skale_allocator, wait_for):
    skale_allocator.allocator.add_plan(
        vesting_cliff=TEST_VESTING_SLIFF,
        total_vesting_duration=TEST_TOTAL_VESTING_DURATION,
        vesting_step_time_unit=TEST_VESTING_STEP_TIME_UNIT,
        vesting_times=TEST_VESTING_TIMES,
        can_delegate=TEST_CAN_DELEGATE,
        is_terminatable=TEST_IS_TERMINATABLE,
        wait_for=wait_for
    )
    event = catch_event(skale_allocator.allocator.contract.events.PlanCreated)
    return event.args['id']


def test_is_beneficiary_registered(skale_allocator):
    wallet = generate_wallet(skale_allocator.web3)
    assert not skale_allocator.allocator.is_beneficiary_registered(wallet.address)


def catch_event(event_obj):
    event_filter = event_obj.createFilter(
        fromBlock=0,
        toBlock='latest'
    )
    while True:
        for event in event_filter.get_new_entries():
            return event
        time.sleep(POLL_INTERVAL)


def test_add_plan(skale_allocator):
    plan_id = _add_test_plan(skale_allocator, False)
    assert isinstance(plan_id, int)


# def test_connect_beneficiary_to_plan(skale_allocator):
#     wallet = generate_wallet(skale_allocator.web3)
#     plan_id = _add_test_plan(skale_allocator, False)
