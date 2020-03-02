""" Tests for contracts/delegation/delegation_controller.py """

import pytest
from tests.constants import (NOT_EXISTING_ID, D_DELEGATION_ID, D_DELEGATION_INFO, D_VALIDATOR_ID,
                             D_DELEGATION_AMOUNT, D_DELEGATION_PERIOD, DELEGATION_STRUCT_LEN,
                             MONTH_IN_SECONDS)

from skale.contracts.delegation.delegation_controller import FIELDS
from tests.utils import skip_evm_time


def _get_number_of_delegations(skale):
    return skale.delegation_controller._get_delegation_ids_len_by_validator(D_VALIDATOR_ID)


def test_get_raw_not_exist(skale):
    with pytest.raises(ValueError):
        skale.delegation_controller._DelegationController__raw_get_delegation(NOT_EXISTING_ID)


def test_get_raw(skale):
    delegation_struct = skale.delegation_controller._DelegationController__raw_get_delegation(
        D_DELEGATION_ID
    )
    assert len(delegation_struct) == DELEGATION_STRUCT_LEN


def test_get(skale):
    delegation = skale.delegation_controller.get_delegation(D_DELEGATION_ID)
    assert list(delegation.keys()) == FIELDS
    assert [k for k, v in delegation.items() if v is None] == []


def test_delegate(skale):
    num_of_delegations_before = _get_number_of_delegations(skale)
    _delegate_and_activate(skale)
    num_of_delegations_after = _get_number_of_delegations(skale)
    assert num_of_delegations_after == num_of_delegations_before + 1

    delegations = skale.delegation_controller.get_all_delegations_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    assert delegations[-1]['info'] == D_DELEGATION_INFO


def test_get_delegation_ids_by_validator(skale):
    delegation_ids = skale.delegation_controller._get_delegation_ids_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    delegation_ids_len = skale.delegation_controller._get_delegation_ids_len_by_validator(
        D_VALIDATOR_ID
    )
    assert len(delegation_ids) == delegation_ids_len
    latest_delegation = skale.delegation_controller.get_delegation(delegation_ids[-1])
    assert latest_delegation['validator_id'] == D_VALIDATOR_ID


def test_get_all_delegations_by_holder(skale):
    delegations = skale.delegation_controller.get_all_delegations_by_holder(
        skale.wallet.address
    )
    assert all([delegation['address'] == skale.wallet.address for delegation in delegations])


def test_get_all_delegations_by_validator(skale):
    delegations = skale.delegation_controller.get_all_delegations_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    assert all([delegation['validator_id'] == D_VALIDATOR_ID for delegation in delegations])


def test_accept_pending_delegation(skale):
    skale.delegation_controller.delegate(
        validator_id=D_VALIDATOR_ID,
        amount=D_DELEGATION_AMOUNT,
        delegation_period=D_DELEGATION_PERIOD,
        info=D_DELEGATION_INFO,
        wait_for=True
    )
    delegations = skale.delegation_controller.get_all_delegations_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    delegation_id = delegations[-1]['id']
    assert delegations[-1]['status'] == 'PROPOSED'
    skale.delegation_controller.accept_pending_delegation(
        delegation_id,
        wait_for=True
    )
    delegations = skale.delegation_controller.get_all_delegations_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    assert delegations[-1]['id'] == delegation_id
    assert delegations[-1]['status'] == 'ACCEPTED'
    skip_evm_time(skale.web3, MONTH_IN_SECONDS)


def test_cancel_pending_delegation(skale):
    skale.delegation_controller.delegate(
        validator_id=D_VALIDATOR_ID,
        amount=D_DELEGATION_AMOUNT,
        delegation_period=D_DELEGATION_PERIOD,
        info=D_DELEGATION_INFO,
        wait_for=True
    )
    delegations = skale.delegation_controller.get_all_delegations_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    delegation_id = delegations[-1]['id']
    assert delegations[-1]['status'] == 'PROPOSED'
    skale.delegation_controller.cancel_pending_delegation(
        delegation_id,
        wait_for=True
    )
    delegations = skale.delegation_controller.get_all_delegations_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    assert delegations[-1]['id'] == delegation_id
    assert delegations[-1]['status'] == 'CANCELED'
    skip_evm_time(skale.web3, MONTH_IN_SECONDS)


def _delegate_and_activate(skale):
    skale.delegation_controller.delegate(
        validator_id=D_VALIDATOR_ID,
        amount=D_DELEGATION_AMOUNT,
        delegation_period=D_DELEGATION_PERIOD,
        info=D_DELEGATION_INFO,
        wait_for=True
    )
    delegation_ids = skale.delegation_controller._get_delegation_ids_by_validator(
        validator_id=D_VALIDATOR_ID
    )
    skale.delegation_controller.accept_pending_delegation(
        delegation_ids[-1],
        wait_for=True
    )
    skip_evm_time(skale.web3, MONTH_IN_SECONDS)


def test_get_delegated_to_validator_now(skale):
    delegated_amount_before = skale.delegation_controller.get_delegated_to_validator_now(
        D_VALIDATOR_ID
    )
    _delegate_and_activate(skale)
    delegated_amount_after = skale.delegation_controller.get_delegated_to_validator_now(
        D_VALIDATOR_ID
    )
    assert delegated_amount_after == delegated_amount_before + D_DELEGATION_AMOUNT


def test_get_delegated_amount(skale):
    delegated_amount_before = skale.delegation_controller.get_delegated_amount(
        skale.wallet.address
    )
    _delegate_and_activate(skale)
    delegated_amount_after = skale.delegation_controller.get_delegated_amount(
        skale.wallet.address
    )
    assert delegated_amount_after == delegated_amount_before + D_DELEGATION_AMOUNT
