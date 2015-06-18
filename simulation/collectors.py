
class DataCollector(object):
    client_incoming = []
    client_outgoing = []
    client_outgoing_count = 0

    @staticmethod
    def sync_clients(incoming):
        if DataCollector.client_incoming:
            incoming = incoming + DataCollector.client_incoming[-1]
        DataCollector.client_incoming.append(incoming)
        DataCollector.client_outgoing.append(DataCollector.client_outgoing_count)

    @staticmethod
    def client_left():
        DataCollector.client_outgoing_count = DataCollector.client_outgoing_count + 1

    @staticmethod
    def reset():
        DataCollector.client_incoming = []
        DataCollector.client_outgoing = []
        DataCollector.client_outgoing_count = 0
