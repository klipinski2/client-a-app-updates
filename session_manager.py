# Refactored session management for improved scalability
# File: auth/session_manager.py

class SessionManager:
    def __init__(self, timeout=3600):
        self.active_sessions = {}
        self.timeout = timeout  # Session timeout in seconds

    def create_session(self, user_id):
        """Creates a new session for the given user ID."""
        session_id = self.generate_session_id(user_id)
        self.active_sessions[session_id] = {
            "user_id": user_id,
            "start_time": self.current_time(),
        }
        return session_id

    def validate_session(self, session_id):
        """Validates if the session is active and not expired."""
        session = self.active_sessions.get(session_id)
        if not session:
            return False
        if self.current_time() - session["start_time"] > self.timeout:
            self.end_session(session_id)
            return False
        return True

    def end_session(self, session_id):
        """Ends the session and removes it from active sessions."""
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]

    @staticmethod
    def generate_session_id(user_id):
        """Generates a unique session ID."""
        import hashlib
        import time
        return hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()

    @staticmethod
    def current_time():
        """Returns the current time in seconds."""
        import time
        return int(time.time())
