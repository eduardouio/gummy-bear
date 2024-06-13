from django.contrib import admin

from django_ledger.admin.coa import ChartOfAccountsModelAdmin
from django_ledger.admin.entity import EntityModelAdmin
from django_ledger.admin.ledger import LedgerModelAdmin
from django_ledger.models import (
    EntityModel, ChartOfAccountModel, LedgerModel, CustomerModel,
    BillModel, ClosingEntryTransactionModel, AccountModel,
    EstimateModel, InvoiceModel, JournalEntryModel, PurchaseOrderModel,
    VendorModel, ClosingEntryModel, StagedTransactionModel,
    StagedTransactionModel
)


class CustomerModelAdmin(admin.ModelAdmin):
    pass


class BillModelAdmin(admin.ModelAdmin):
    pass


class ClosingEntryTransactionModelAdmin(admin.ModelAdmin):
    pass


class AccountModelAdmin(admin.ModelAdmin):
    pass


class EstimateModelAdmin(admin.ModelAdmin):
    pass


class InvoiceModelAdmin(admin.ModelAdmin):
    pass


class journalEntryModelAdmin(admin.ModelAdmin):
    pass


class purchaseOrderModelAdmin(admin.ModelAdmin):
    pass


class VendorModelAdmin(admin.ModelAdmin):
    pass


class ClosingEntryModelAdmin(admin.ModelAdmin):
    pass


class StagedTransactionModelAdmin(admin.ModelAdmin):
    pass



admin.site.register(EntityModel, EntityModelAdmin)
admin.site.register(ChartOfAccountModel, ChartOfAccountsModelAdmin)
admin.site.register(LedgerModel, LedgerModelAdmin)
admin.site.register(CustomerModel, CustomerModelAdmin)
admin.site.register(BillModel, BillModelAdmin)
admin.site.register(ClosingEntryTransactionModel,
                    ClosingEntryTransactionModelAdmin)
admin.site.register(AccountModel, AccountModelAdmin)
admin.site.register(EstimateModel, EstimateModelAdmin)
admin.site.register(InvoiceModel, InvoiceModelAdmin)
admin.site.register(JournalEntryModel, journalEntryModelAdmin)
admin.site.register(PurchaseOrderModel, purchaseOrderModelAdmin)
admin.site.register(VendorModel, VendorModelAdmin)
admin.site.register(ClosingEntryModel, ClosingEntryModelAdmin)
admin.site.register(StagedTransactionModel, StagedTransactionModelAdmin)

