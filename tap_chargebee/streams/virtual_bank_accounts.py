from tap_chargebee.streams.base import BaseChargebeeStream


class VirtualBankAccountsStream(BaseChargebeeStream):
    TABLE = 'virtual_bank_accounts'
    ENTITY = 'virtual_bank_account'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['updated_at']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['updated_at']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def get_url(self):
        return 'https://{}.chargebee.com/api/v2/virtual_bank_accounts'.format(self.config.get('site'))
