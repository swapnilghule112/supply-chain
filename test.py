from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb = BigchainDB("localhost:9984", timeout=None)
alice = generate_keypair()
tx = bdb.transactions.prepare(
    operation="CREATE",
    signers=alice.public_key,
    asset={"data": {"message": "bigchain test on july 12 2020: 16:30!"}},
)
signed_tx = bdb.transactions.fulfill(tx, private_keys=alice.private_key)
bdb.transactions.send_commit(signed_tx)
