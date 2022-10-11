import io
import json

from factory import faker, transactions_faker

with io.open("bulkData.file", "w+", buffering=20*(1024**2)) as file:    
    for i in range(1, int(1e3)): 
        user = dict(
            id=int(i),
            name=str(faker.name()),
            email=str(faker.email()),
            address=str(faker.address()),
            transactions=transactions_faker
        )

        file.writelines(json.dumps(user))
