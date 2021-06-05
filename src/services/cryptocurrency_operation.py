import decimal

from django.db import models

from domain.cryptocurrencie.models import Cryptocurrencie
from domain.user.models import User
from views.cryptocurrencie.serializer.cryptocurrencie import CryptocurrencyOperationTypeChoices


class ComunicationChoices(models.TextChoices):
    BUYER_HAS_NO_THIS_CRYPTOCURRENCY = 'O vendedor não possui essa criptomoeda para pode vende-la'
    BUYER_INSUFFIENT_AMOUNT_OF_CRYPTOCURRENCIES = 'O vendedor não possui a quantidade de criptomoedas sufiente para ' \
                                                  'concluir a venda'
    BUYER_DOES_NOT_HAVE_ENOUGH_BALANCE = 'Você não possui saldo para realizar a compra'

    SELLER_HAS_NO_THIS_CRYPTOCURRENCY = 'Você não possui essa criptomoeda para pode vende-la'
    SELLER_INSUFFIENT_AMOUNT_OF_CRYPTOCURRENCIES = 'Você não possui a quantidade de criptomoedas sufiente para ' \
                                                   'concluir a venda'
    SELLER_DOES_NOT_HAVE_ENOUGH_BALANCE = 'O vendedor não possui saldo para realizar a compra'

    PURCHASE_COMPLETED = 'PURCHASE_COMPLETED'

    @classmethod
    def has_no_this_cryptocurrency(cls, operation_type: str):
        if operation_type == CryptocurrencyOperationTypeChoices.BUY:
            return cls.BUYER_HAS_NO_THIS_CRYPTOCURRENCY

        return cls.SELLER_HAS_NO_THIS_CRYPTOCURRENCY

    @classmethod
    def insuffient_amount_of_cryptocurrencies(cls, operation_type: str):
        if operation_type == CryptocurrencyOperationTypeChoices.BUY:
            return cls.BUYER_INSUFFIENT_AMOUNT_OF_CRYPTOCURRENCIES

        return cls.SELLER_INSUFFIENT_AMOUNT_OF_CRYPTOCURRENCIES

    @classmethod
    def does_not_have_enough_balance(cls, operation_type: str):
        if operation_type == CryptocurrencyOperationTypeChoices.BUY:
            return cls.BUYER_DOES_NOT_HAVE_ENOUGH_BALANCE

        return cls.SELLER_DOES_NOT_HAVE_ENOUGH_BALANCE


class CryptocurrencyOperationService:
    @staticmethod
    def execute(
            buyer: User,
            seller: User,
            cryptocurrencie: Cryptocurrencie,
            amount_of_cryptocurrencies: decimal.Decimal,
            operation_type: str
    ):
        cryptocurrencie_seller = seller.wallet_set.filter(cryptocurrencie=cryptocurrencie).first()

        if not cryptocurrencie_seller:
            return False, ComunicationChoices.has_no_this_cryptocurrency(operation_type=operation_type)

        elif not cryptocurrencie_seller.has_enough_cryptocurrencies_for_sale(sale_quantity=amount_of_cryptocurrencies):
            return False, ComunicationChoices.insuffient_amount_of_cryptocurrencies(operation_type=operation_type)

        transaction_amount = cryptocurrencie.transaction_amount(amount=amount_of_cryptocurrencies)

        if not buyer.has_balance_for_purchase(purchase_amount=transaction_amount):
            return False, ComunicationChoices.does_not_have_enough_balance(operation_type=operation_type)

        cryptocurrencie_buyer, _ = buyer.wallet_set.get_or_create(cryptocurrencie=cryptocurrencie)

        cryptocurrencie_buyer.credit_cryptocurrencie(amount=amount_of_cryptocurrencies)
        cryptocurrencie_buyer.save()

        buyer.debit_balance(amount=transaction_amount)
        buyer.save()

        cryptocurrencie_seller.debit_cryptocurrencie(amount=amount_of_cryptocurrencies)
        cryptocurrencie_seller.save()

        seller.credit_balance(amount=transaction_amount)
        seller.save()

        return True, ComunicationChoices.PURCHASE_COMPLETED
