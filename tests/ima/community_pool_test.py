from tests.constants import (DEFAULT_SCHAIN_ID, DEFAULT_SCHAIN_NAME)
from skale.skale_ima import SkaleIma
from skale.utils.web3_utils import init_web3
from tests.constants import ETH_PRIVATE_KEY
from skale.wallets import Web3Wallet
from skale.utils.account_tools import send_eth
import os
import logging


ETH_AMOUNT = 0.001


# def skale_ima():
#     rpc = os.environ['MAINNET_ENDPOINT']
# #    path = os.environ['DATA_DIR']
#     pk = os.environ['ETH_PRIVATE_KEY']
#     alias = os.environ['ALIAS']
#     web3 = init_web3(rpc)
#     ima = SkaleIma(endpoint=rpc, alias_or_address=alias, wallet=Web3Wallet(pk, web3))
#     return ima


# def test_check_user_balance():
#     ima = skale_ima()
#     schain_name = os.environ['SCHAIN_NAME']
#     address = os.environ['TEST_ADDRESS']
#     logging.info(schain_name)
#     logging.info(address)
#     res = ima.community_pool.check_user_balance(schain_name,address)
#     logging.info(res)
#     assert res



