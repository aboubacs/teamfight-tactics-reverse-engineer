
class OnHitEffect:
    def __init__(self, source, attached_to, expires_at):
        self.source = source
        self.attached_to = attached_to
        self.expires_at = expires_at

    def proc(self, target):
        pass

    def force_expire(self):
        self.expires_at = -1