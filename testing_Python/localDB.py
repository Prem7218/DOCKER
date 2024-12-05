import pymysql
# 192.168.115.203 <----------> IPV4 Address

class MySQLConnector:
    """Handles MySQL database connection and basic operations."""
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establishes a connection to the MySQL database."""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection to the database was successful!")
        except pymysql.MySQLError as e:
            print("Failed to connect to the database.")
            print(f"Error: {e}")
            self.connection = None

    def close(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection closed successfully.")
        else:
            print("No connection to close.")

    def execute_query(self, query, params=None):
        """Executes a single query and commits changes."""
        if not self.connection:
            print("No connection available.")
            return
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print("Query executed successfully.")
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query):
        """Executes a SELECT query and fetches all results."""
        if not self.connection:
            print("No connection available.")
            return []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")
            return []


class UserManager:
    """Manages user-related database operations."""
    
    def __init__(self, connector):
        self.connector = connector

    def create_table(self):
        """Creates the usernames table if it doesn't exist."""
        query = """
            CREATE TABLE IF NOT EXISTS usernames (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255)
            )
        """
        self.connector.execute_query(query)

    def add_user(self, name):
        """Inserts a new username into the database."""
        query = "INSERT INTO usernames (name) VALUES (%s)"
        self.connector.execute_query(query, (name,))
        print(f"User '{name}' added to the database.")

    def list_users(self):
        """Fetches all usernames from the database."""
        query = "SELECT name FROM usernames"
        results = self.connector.fetch_all(query)
        if results:
            return [row[0] for row in results]
        return []


class App:
    """Main application logic."""
    
    def __init__(self):
        # Configure database connection details
        self.connector = MySQLConnector(
            # localhost
            # ipv4 of container or that conatiner: 172.17.0.3 
            # docker network: mysqldb
            host="host.docker.internal",
            user="root",
            password="Pass@123PRM",
            database="userinfo"
        )
        self.user_manager = UserManager(self.connector)

    def run(self):
        """Runs the application."""
        self.connector.connect()
        self.user_manager.create_table()

        while True:
            print("\n1. Add a user")
            print("2. List all users")
            print("3. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter a username: ")
                self.user_manager.add_user(name)
            elif choice == "2":
                users = self.user_manager.list_users()
                if users:
                    print("Users in the database:")
                    for user in users:
                        print(user)
                else:
                    print("No users found in the database.")
            elif choice == "3":
                print("Exiting the application...")
                break
            else:
                print("Invalid choice. Please try again.")

        self.connector.close()

if __name__ == "__main__":
    app = App()
    app.run()
