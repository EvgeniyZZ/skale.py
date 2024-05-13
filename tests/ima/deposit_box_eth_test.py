from tests.constants import (DEFAULT_SCHAIN_ID, DEFAULT_SCHAIN_NAME)
from skale.skale_ima import SkaleIma
from skale.utils.web3_utils import init_web3
from tests.constants import ETH_PRIVATE_KEY
from skale.wallets import Web3Wallet
from skale.utils.account_tools import send_eth
import os
import logging


ETH_AMOUNT = 0.001

def bytes_to_int(value):
        return int.from_bytes(bytearray(value), 'little')


def skale_ima():
    rpc = os.environ['MAINNET_ENDPOINT']
#    path = os.environ['DATA_DIR']
    pk = os.environ['ETH_PRIVATE_KEY']
    alias = os.environ['ALIAS']
    web3 = init_web3(rpc)
    ima = SkaleIma(endpoint=rpc, alias_or_address=alias, wallet=Web3Wallet(pk, web3))
    return ima

def test_deposit():
    ima = skale_ima()
    schain_name=os.environ['SCHAIN_MSG']
    amount = ETH_AMOUNT
    value = ima.web3.to_wei(amount, 'ether')
    res = ima.deposit_box_eth.deposit(schain_name, value=value)
    logging.info(res)
    assert res



def test_direct_deposit():
    ima = skale_ima()
    schain_name = os.environ[f'SCHAIN_NAME']
    amount = ETH_AMOUNT
    value = ima.web3.to_wei(amount, 'ether')
    receiver = "0xb04a7f2Cd74Eb624Df4BD8bed8f7034B5Aed89C0"
    assert ima.deposit_box_eth.deposit_direct(schain_name, receiver)


def test_is_active():
    ima = skale_ima()
    schain_name = os.environ[f'SCHAIN_NAME']
    res = ima.deposit_box_eth.is_active_transfers(schain_name)
    logging.info(res)
    assert res

def test_disable_active_eth_transfers():
    ima = skale_ima()
    schain_name = "spanish-smug-auva"
    assert ima.deposit_box_eth.disable_active_eth_transfers(schain_name)


def test_enable_active_eth_transfers():
    ima = skale_ima()
    schain_name = os.environ[f'SCHAIN_NAME']
    assert ima.deposit_box_eth.enable_active_eth_transfers(schain_name)

