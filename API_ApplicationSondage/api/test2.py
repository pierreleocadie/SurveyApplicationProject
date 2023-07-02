from dao import ConstituentDAO

with ConstituentDAO() as constituent_dao:
    print(constituent_dao.get_id("Dupont", "Jean", "1990-01-01", "1 rue de la Paix", "75000", "Paris", "0123456789"))