def generate_response(complaint_text, department, priority, retrieved_context):
    response = f"""
Dear Sir/Madam,

We acknowledge receipt of your complaint regarding the {department.replace('-', ' ')} issue.

{retrieved_context}

Based on the details provided, your complaint has been marked as {priority} priority and forwarded to the concerned department for necessary action.

Please note that this response has been AI-assisted and reviewed by authorized personnel.

Regards,
Grievance Redressal Team
"""
    return response.strip()
