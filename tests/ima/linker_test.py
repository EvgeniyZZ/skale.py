from tests.constants import (DEFAULT_SCHAIN_ID, DEFAULT_SCHAIN_NAME)
from skale.skale_ima import SkaleIma
from skale.utils.web3_utils import init_web3
from tests.constants import ETH_PRIVATE_KEY
from skale.wallets import Web3Wallet
from skale.utils.account_tools import send_eth
import os
import logging


ETH_AMOUNT = 0.001


def skale_ima():
    rpc = os.environ['MAINNET_ENDPOINT']
#    path = os.environ['DATA_DIR']
    pk = os.environ['ETH_PRIVATE_KEY']
    alias = os.environ['ALIAS']
    web3 = init_web3(rpc)
    ima = SkaleIma(endpoint=rpc, alias_or_address=alias, wallet=Web3Wallet(pk, web3))
    return ima


def bytes_to_int(value):
        return int.from_bytes(bytearray(value), 'little')


# def test_is_not_killed() -> bool:
#     ima = skale_ima()
#     res = ima.linker.is_not_killed('SCHAIN_MSG')
#     get_address = ima.instance.address
#     logging.info(get_address)
#     logging.info(res)
#     assert res


# def test_get_my_eth():
#     ima = skale_ima()
#     assert ima.deposit_box_eth.get_my_eth()


# def test_has_role():
#     ima = skale_ima()
#     role = ima.linker.linker_role()
#     logging.info(role)
#     address = os.environ['ADDRESS']
#     logging.info(address)
#     res = ima.linker.has_role(role, address)
#     logging.info(res)
#     assert res


# def test_grant_role():
#    ima = skale_ima()
#    role = ima.linker.linker_role()
#    address = os.environ['ADDRESS']
#    assert ima.deposit_box_eth.grant_role(role,address)
#######
#DepositBoxERC20
#######

# def test_add_erc20_token_by_owner():
#     ima = skale_ima()
#     schain_name = os.environ['SCHAIN_NAME']
#     address = os.environ['TOKEN_ADDRESS']
#     logging.info(schain_name)
#     logging.info(address)
#     res = ima.deposit_box_erc20.add_erc20_token(schain_name, address)
#     assert res

# def test_arbiter_role():
#     ima = skale_ima()
#     res = ima.deposit_box_erc20.arbiter_role()
#     logging.info(res)
#     assert res


# def test_admin_role():
#     ima = skale_ima()
#     res = ima.deposit_box_erc20.admin_role()
#     logging.info(res)
#     assert res

# def test_role_member_count():
#     ima = skale_ima()
#     role = ima.deposit_box_erc20.admin_role()
#     res = ima.deposit_box_erc20.get_role_member(role, 3)
#     logging.info(res)
#     assert res

# def test_grant_arbiter_role():
#     ima = skale_ima()
#     role = ima.deposit_box_erc20.arbiter_role()
#     address = os.environ['ADDRESS']
#     res = ima.deposit_box_erc20.grant_role(role, address)
#     logging.info(res)
#     assert res


# def test_has_arbiter_role():
#     ima = skale_ima()
#     role = ima.deposit_box_erc20.arbiter_role()
#     address = os.environ['ADDRESS']
#     res = ima.deposit_box_erc20.has_arbiter_role(role, address)
#     logging.info(res)
#     assert res


# def test_is_trusted():
#     ima = skale_ima()
#     schain_name = os.environ['SCHAIN_NAME']
#     address = os.environ['ADDRESS']
#     aaa = ima.instance.address
#     logging.info(aaa)
#     res =  ima.deposit_box_erc20.is_receiver_trusted(schain_name, address)
#     logging.info(res)
#     assert not True
