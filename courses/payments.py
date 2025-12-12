import uuid

def mock_payment_processing(user_id: uuid.UUID, course_id: uuid.UUID, amount: float) -> bool:
    return {
        "status" : "success",
        "payment_id": str(uuid.uuid4())
    }