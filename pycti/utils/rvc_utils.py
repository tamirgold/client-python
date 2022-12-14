class RvcUtils:
    @staticmethod
    def stix_observable_opencti_type(observable_type):
        if observable_type in STIX_CYBER_OBSERVABLE_MAPPING:
            return STIX_CYBER_OBSERVABLE_MAPPING[observable_type]
        else:
            return "Unknown"
