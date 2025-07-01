class PropertyUtil:
    @staticmethod
    def get_property_string(filepath='resources/db.properties'):
        full = os.path.abspath(filepath)
        config = configparser.ConfigParser()
        config.read(full)
        db = config['database']

        conn_str = (
            f"DRIVER={db['driver']};"
            f"SERVER={db['server']};"
            f"DATABASE={db['dbname']};"
        )
        if db.get('trusted','yes').lower() == 'yes':
            conn_str += "Trusted_Connection=yes;"
        if 'encrypt' in db:
            conn_str += f"Encrypt={db['encrypt']};"
        if 'trust_server_certificate' in db:
            conn_str += f"TrustServerCertificate={db['trust_server_certificate']};"

        return conn_str
