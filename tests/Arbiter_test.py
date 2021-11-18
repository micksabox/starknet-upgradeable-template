"""Arbiter.cairo test file."""

import pytest
import asyncio
from starkware.starknet.testing.starknet import Starknet
from starkware.starkware_utils.error_handling import StarkException
from starkware.starknet.definitions.error_codes import StarknetErrorCode
from utils.Signer import Signer

# Initialize a signer with a private key
# used during the test
signer = Signer(123456789987654321)

# Using scope='module' requires  a redefinition of event_loop
@pytest.fixture(scope='module')
def event_loop():
    return asyncio.new_event_loop()

@pytest.fixture(scope='module')
async def arbiter_factory():
    # Create a new Starknet class that simulates the StarkNet
    # system.
    starknet = await Starknet.empty()

    # Deploy the owner account contract.
    account = await starknet.deploy(
        "contracts/Account.cairo",
        constructor_calldata=[signer.public_key]
    )

    # Must call initialize on the account until
    # this.address available for constructor
    await account.initialize(account.contract_address).invoke()

    # Deploy the arbiter contract.
    arbiter = await starknet.deploy(
        "contracts/Arbiter.cairo",
        constructor_calldata=[account.contract_address],
    )
    return starknet, account, arbiter

# The testing library uses python's asyncio. So the following
# decorator and the ``async`` keyword are needed.
@pytest.mark.asyncio
async def test_set_controller(arbiter_factory):
    """Test set controller"""

    _,account,arbiter = arbiter_factory

    mock_controller_address = 123456789

    await signer.send_transaction(
        account=account,
        to=arbiter.contract_address,
        selector_name="set_address_of_controller",
        calldata=[mock_controller_address],
        nonce=None
    )

    # Setup a signer that is not the admin
    non_admin_signer = Signer(432432143989)

    try:
        await non_admin_signer.send_transaction(
            account=account,
            to=arbiter.contract_address, 
            selector_name='set_address_of_controller', 
            calldata=[mock_controller_address], 
            nonce=None)
        assert False
    except StarkException as err:
        _, error = err.args
        assert error['code'] == StarknetErrorCode.TRANSACTION_FAILED
