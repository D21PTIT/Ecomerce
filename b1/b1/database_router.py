class DatabaseRouter:
    """
    Điều hướng database: MySQL cho customer, MongoDB cho book.
    """

    def db_for_read(self, model, **hints):
        """Chỉ định database cho các lệnh đọc"""
        if model._meta.app_label == 'book':
            return 'mongo_db'  # App 'book' dùng MongoDB
        return 'default'  # Mặc định dùng MySQL

    def db_for_write(self, model, **hints):
        """Chỉ định database cho các lệnh ghi"""
        if model._meta.app_label == 'book':
            return 'mongo_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Cho phép quan hệ giữa các database"""
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Chỉ cho phép migrate trên database phù hợp"""
        if app_label == 'book':
            return db == 'mongo_db'
        return db == 'default'
