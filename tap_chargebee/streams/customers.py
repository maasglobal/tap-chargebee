from tap_chargebee.streams.base import BaseChargebeeStream


class CustomersStream(BaseChargebeeStream):
    TABLE = 'customers'
    ENTITY = 'customer'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['updated_at']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['updated_at']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def get_url(self):
        return 'https://{}.chargebee.com/api/v2/customers'.format(self.config.get('site'))
