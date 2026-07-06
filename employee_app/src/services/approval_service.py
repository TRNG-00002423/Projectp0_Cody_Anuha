from repositories.approval_repository import ApprovalRepository
from models.approval import Approval

class ApprovalService:
    def get_all_approvals_from_user_id(self, user_id : int):
        ar = ApprovalRepository()
        return ar.get_all_approvals_from_user_id(user_id)

    def add_approval(self, approval : Approval):
        ar = ApprovalRepository()
        ar.add_or_update_approval(approval)