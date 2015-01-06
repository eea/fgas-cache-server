from datetime import date

from factory.alchemy import SQLAlchemyModelFactory
from factory import SubFactory, post_generation

from fcs import models


class CountryFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Country
        sqlalchemy_session = models.db.session

    code = 'c'
    name = 'n'
    type = 't'


class AddressFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Address
        sqlalchemy_session = models.db.session

    country = SubFactory(CountryFactory)

    street = 's'
    number = 'n'
    city = 'c'
    zipcode = 'z'


class RepresentativeFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.EuLegalRepresentativeCompany
        sqlalchemy_session = models.db.session

    name = 'n'
    vatnumber = 'vat'
    contact_first_name = 'first'
    contact_last_name = 'last'
    contact_email = 'email'
    address = SubFactory(AddressFactory)


class BusinessProfileFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.BusinessProfile
        sqlalchemy_session = models.db.session


class OldCompanyFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.OldCompany
        sqlalchemy_session = models.db.session

    external_id = '100'
    name = 'old_company_name'
    country_code = 'RO'
    account = 'account'
    vat_number = 'account'
    eori = 'account'
    active = True
    website = 'website'
    date_registered = date(2015, 1, 1)
    valid = True


class UndertakingFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Undertaking
        sqlalchemy_session = models.db.session

    name = 'n'
    website = 'w'
    phone = 'p'
    domain = 'd'
    status = 's'
    date_created = date(2015, 1, 1)
    date_updated = date(2015, 1, 1)
    undertaking_type = 'FGASUndertaking'
    vat = 'v'
    types = 't'
    oldcompany_verified = True
    oldcompany_account = 'oldcompany_account'
    oldcompany_extid = 100
    address = SubFactory(AddressFactory)
    represent = SubFactory(RepresentativeFactory)
    businessprofile = SubFactory(BusinessProfileFactory)
    oldcompany = SubFactory(OldCompanyFactory)

    @post_generation
    def contact_persons(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for cp in extracted:
                self.contact_persons.add(cp)


class OldCompanyLinkFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.OldCompanyLink
        sqlalchemy_session = models.db.session

    verified = True
    date_added = date(2015, 1, 1)
    date_verified = date(2015, 1, 1)

    undertaking = SubFactory(UndertakingFactory)
    oldcompany = SubFactory(OldCompanyFactory)