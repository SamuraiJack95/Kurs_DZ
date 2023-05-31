import os
from DZ_41.models.database import DATABASE_NAME, Session
import create_database as db_creator

from DZ_41.models.customers import Customers, association_tablec
from DZ_41.models.sales import Sales


if __name__ == '__main__':
    db_is_creator = os.path.exists(DATABASE_NAME)
    if not db_is_creator:
        db_creator.create_database()

        session = Session()
        print(session.query().all())

    
